#!/usr/bin/env python3
"""
GitHub Issue Creator from Markdown with YAML Frontmatter
Reusable script for creating GitHub issues from structured markdown documents.
"""

import argparse
import yaml
import re
import sys
from typing import Dict, List, Any
from pathlib import Path
import requests
from datetime import datetime
import time

class GitHubIssueCreator:
    def __init__(self, token: str, repo: str, dry_run: bool = False):
        """
        Initialize the GitHub Issue Creator.
        
        Args:
            token: GitHub personal access token
            repo: Repository in format "owner/repo"
            dry_run: If True, don't actually create issues
        """
        self.token = token
        self.repo = repo
        self.dry_run = dry_run
        self.base_url = f"https://api.github.com/repos/{repo}"
        self.headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json"
        }
        self.created_issues = {}  # Map ticket IDs to issue numbers
        
    def parse_markdown_with_frontmatter(self, file_path: str) -> Dict[str, Any]:
        """Parse markdown file with YAML frontmatter blocks."""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract epic frontmatter
        epic_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
        epic_data = {}
        if epic_match:
            epic_yaml = epic_match.group(1)
            epic_data = yaml.safe_load(epic_yaml).get('epic', {})
        
        # Extract all ticket frontmatters and content
        tickets = []
        pattern = r'---\nticket:(.*?)\n---\n(.*?)(?=---\nticket:|$)'
        matches = re.findall(pattern, content, re.DOTALL)
        
        for yaml_content, markdown_content in matches:
            ticket_data = yaml.safe_load(f"ticket:{yaml_content}")['ticket']
            ticket_data['content'] = markdown_content.strip()
            tickets.append(ticket_data)
        
        return {
            'epic': epic_data,
            'tickets': tickets
        }
    
    def create_epic(self, epic_data: Dict[str, Any]) -> int:
        """Create the epic issue."""
        print(f"🎯 Creating Epic: {epic_data['title']}")
        
        if self.dry_run:
            print("  [DRY RUN] Would create epic")
            return 999
        
        body = f"{epic_data['description']}\n\n## Child Issues\n*Will be updated with ticket links*"
        
        issue_data = {
            "title": epic_data['title'],
            "body": body,
            "labels": epic_data.get('labels', []),
            "milestone": self._get_or_create_milestone(epic_data.get('milestone'))
        }
        
        response = requests.post(
            f"{self.base_url}/issues",
            json=issue_data,
            headers=self.headers
        )
        
        if response.status_code == 201:
            issue_number = response.json()['number']
            print(f"  ✅ Created Epic: #{issue_number}")
            return issue_number
        else:
            print(f"  ❌ Failed to create epic: {response.text}")
            sys.exit(1)
    
    def create_ticket(self, ticket: Dict[str, Any], epic_number: int) -> int:
        """Create a single ticket issue."""
        ticket_id = ticket['id']
        title = f"{ticket_id}: {ticket['title']}"
        
        print(f"📝 Creating {ticket_id}: {ticket['title']}")
        
        # Build the issue body
        body_parts = [
            f"**Parent Epic:** #{epic_number}",
            f"**Type:** {ticket.get('type', 'task')}",
            f"**Priority:** {ticket.get('priority', 'P2')}",
            f"**Story Points:** {ticket.get('points', '?')}",
            f"**Sprint:** {ticket.get('sprint', '?')}",
        ]
        
        # Add dependencies with links
        if ticket.get('dependencies'):
            deps = []
            for dep_id in ticket['dependencies']:
                if dep_id in self.created_issues:
                    deps.append(f"#{self.created_issues[dep_id]}")
                else:
                    deps.append(dep_id)
            body_parts.append(f"**Dependencies:** {', '.join(deps)}")
        
        body_parts.append(f"\n---\n\n{ticket['content']}")
        body_parts.append(f"\n---\n*Part of #{epic_number}*")
        
        body = "\n".join(body_parts)
        
        if self.dry_run:
            print(f"  [DRY RUN] Would create ticket {ticket_id}")
            self.created_issues[ticket_id] = 1000 + len(self.created_issues)
            return self.created_issues[ticket_id]
        
        issue_data = {
            "title": title,
            "body": body,
            "labels": ticket.get('labels', []),
            "milestone": self._get_or_create_milestone(ticket.get('milestone'))
        }
        
        # Add assignee if specified
        if ticket.get('assignee'):
            issue_data['assignees'] = [ticket['assignee']]
        
        response = requests.post(
            f"{self.base_url}/issues",
            json=issue_data,
            headers=self.headers
        )
        
        if response.status_code == 201:
            issue_number = response.json()['number']
            print(f"  ✅ Created: #{issue_number}")
            self.created_issues[ticket_id] = issue_number
            time.sleep(0.5)  # Rate limiting
            return issue_number
        else:
            print(f"  ❌ Failed to create {ticket_id}: {response.text}")
            return None
    
    def update_epic_with_tickets(self, epic_number: int):
        """Update the epic with links to all created tickets."""
        print(f"🔄 Updating Epic #{epic_number} with ticket links...")
        
        if self.dry_run:
            print("  [DRY RUN] Would update epic with ticket links")
            return
        
        # Get current epic body
        response = requests.get(
            f"{self.base_url}/issues/{epic_number}",
            headers=self.headers
        )
        
        if response.status_code != 200:
            print(f"  ❌ Failed to fetch epic: {response.text}")
            return
        
        current_body = response.json()['body']
        
        # Build ticket list
        ticket_list = []
        for ticket_id, issue_number in sorted(self.created_issues.items()):
            ticket_list.append(f"- [ ] #{issue_number} - {ticket_id}")
        
        # Update body
        updated_body = current_body.replace(
            "*Will be updated with ticket links*",
            "\n".join(ticket_list)
        )
        
        # Update the issue
        response = requests.patch(
            f"{self.base_url}/issues/{epic_number}",
            json={"body": updated_body},
            headers=self.headers
        )
        
        if response.status_code == 200:
            print(f"  ✅ Updated Epic with {len(self.created_issues)} ticket links")
        else:
            print(f"  ❌ Failed to update epic: {response.text}")
    
    def _get_or_create_milestone(self, milestone_title: str) -> int:
        """Get milestone number, creating if necessary."""
        if not milestone_title:
            return None
        
        # Check existing milestones
        response = requests.get(
            f"{self.base_url}/milestones",
            headers=self.headers
        )
        
        if response.status_code == 200:
            for milestone in response.json():
                if milestone['title'] == milestone_title:
                    return milestone['number']
        
        # Create new milestone
        if not self.dry_run:
            response = requests.post(
                f"{self.base_url}/milestones",
                json={"title": milestone_title},
                headers=self.headers
            )
            if response.status_code == 201:
                return response.json()['number']
        
        return None
    
    def create_issues_from_file(self, file_path: str):
        """Main method to create all issues from a markdown file."""
        print(f"📚 Parsing {file_path}")
        data = self.parse_markdown_with_frontmatter(file_path)
        
        # Create epic
        epic_number = None
        if data.get('epic'):
            epic_number = self.create_epic(data['epic'])
        
        # Create tickets
        print(f"\n📋 Creating {len(data['tickets'])} tickets...")
        for ticket in data['tickets']:
            self.create_ticket(ticket, epic_number)
        
        # Update epic with ticket links
        if epic_number and self.created_issues:
            self.update_epic_with_tickets(epic_number)
        
        # Summary
        print(f"\n✅ Summary:")
        print(f"  - Epic: #{epic_number}" if epic_number else "  - No epic created")
        print(f"  - Tickets created: {len(self.created_issues)}")
        
        if not self.dry_run:
            print(f"\n🔗 View Epic: https://github.com/{self.repo}/issues/{epic_number}")


def main():
    parser = argparse.ArgumentParser(
        description='Create GitHub issues from structured markdown'
    )
    parser.add_argument('file', help='Path to markdown file with tickets')
    parser.add_argument('--repo', required=True, help='GitHub repo (owner/repo)')
    parser.add_argument('--token', help='GitHub token (or set GITHUB_TOKEN env var)')
    parser.add_argument('--dry-run', action='store_true', help='Preview without creating')
    
    args = parser.parse_args()
    
    # Get token
    token = args.token or os.environ.get('GITHUB_TOKEN')
    if not token:
        print("❌ Error: GitHub token required (--token or GITHUB_TOKEN env var)")
        sys.exit(1)
    
    # Create issues
    creator = GitHubIssueCreator(token, args.repo, args.dry_run)
    creator.create_issues_from_file(args.file)


if __name__ == '__main__':
    import os
    main()