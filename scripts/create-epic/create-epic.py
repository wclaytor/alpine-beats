#!/usr/bin/env python3
"""
GitHub Issue Creator from Markdown with YAML Frontmatter
Reusable script for creating GitHub issues from structured markdown documents.
Uses GitHub CLI (gh) for API interactions.
"""

import argparse
import yaml
import re
import sys
import json
import subprocess
from typing import Dict, List, Any, Optional
from pathlib import Path
from datetime import datetime
import time


class GitHubIssueCreator:
    def __init__(self, repo: str, dry_run: bool = False):
        """
        Initialize the GitHub Issue Creator.
        
        Args:
            repo: Repository in format "owner/repo"
            dry_run: If True, don't actually create issues
        """
        self.repo = repo
        self.dry_run = dry_run
        self.created_issues = {}  # Map ticket IDs to issue numbers
        if not dry_run:
            self._verify_gh_cli()
        
    def _verify_gh_cli(self):
        """Verify that gh CLI is installed and authenticated."""
        try:
            result = subprocess.run(
                ['gh', 'auth', 'status'],
                capture_output=True,
                text=True,
                check=False
            )
            if result.returncode != 0:
                print("❌ Error: gh CLI is not authenticated")
                print("Please run: gh auth login")
                sys.exit(1)
        except FileNotFoundError:
            print("❌ Error: gh CLI is not installed")
            print("Please install it from: https://cli.github.com/")
            sys.exit(1)
    
    def _run_gh_command(self, args: List[str], input_data: str = None) -> Optional[Dict]:
        """
        Run a gh command and return the JSON output.
        
        Args:
            args: Command arguments (excluding 'gh')
            input_data: Optional stdin data
            
        Returns:
            Parsed JSON response or None on error
        """
        cmd = ['gh'] + args
        
        if self.dry_run:
            print(f"  [DRY RUN] Would run: {' '.join(cmd)}")
            return None
        
        try:
            result = subprocess.run(
                cmd,
                input=input_data,
                capture_output=True,
                text=True,
                check=True
            )
            
            if result.stdout.strip():
                return json.loads(result.stdout)
            return {}
            
        except subprocess.CalledProcessError as e:
            print(f"  ❌ Command failed: {' '.join(cmd)}")
            print(f"  Error: {e.stderr}")
            return None
        except json.JSONDecodeError as e:
            print(f"  ❌ Failed to parse JSON response: {e}")
            print(f"  Output: {result.stdout}")
            return None
    
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
        
        body = f"{epic_data['description']}\n\n## Child Issues\n*Will be updated with ticket links*"
        
        # Build gh issue create command
        args = [
            'issue', 'create',
            '--repo', self.repo,
            '--title', epic_data['title'],
            '--body', body,
            '--json', 'number'
        ]
        
        # Add labels
        if epic_data.get('labels'):
            for label in epic_data['labels']:
                args.extend(['--label', label])
        
        # Add milestone
        if epic_data.get('milestone'):
            args.extend(['--milestone', epic_data['milestone']])
        
        if self.dry_run:
            print(f"  [DRY RUN] Would create epic with title: {epic_data['title']}")
            return 999
        
        response = self._run_gh_command(args)
        
        if response and 'number' in response:
            issue_number = response['number']
            print(f"  ✅ Created Epic: #{issue_number}")
            return issue_number
        else:
            print(f"  ❌ Failed to create epic")
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
        
        # Build gh issue create command
        args = [
            'issue', 'create',
            '--repo', self.repo,
            '--title', title,
            '--body', body,
            '--json', 'number'
        ]
        
        # Add labels
        if ticket.get('labels'):
            for label in ticket['labels']:
                args.extend(['--label', label])
        
        # Add milestone
        if ticket.get('milestone'):
            args.extend(['--milestone', ticket['milestone']])
        
        # Add assignee
        if ticket.get('assignee'):
            args.extend(['--assignee', ticket['assignee']])
        
        if self.dry_run:
            print(f"  [DRY RUN] Would create ticket {ticket_id}")
            self.created_issues[ticket_id] = 1000 + len(self.created_issues)
            return self.created_issues[ticket_id]
        
        response = self._run_gh_command(args)
        
        if response and 'number' in response:
            issue_number = response['number']
            print(f"  ✅ Created: #{issue_number}")
            self.created_issues[ticket_id] = issue_number
            time.sleep(0.3)  # Small delay to avoid rate limiting
            return issue_number
        else:
            print(f"  ❌ Failed to create {ticket_id}")
            return None
    
    def update_epic_with_tickets(self, epic_number: int):
        """Update the epic with links to all created tickets."""
        print(f"🔄 Updating Epic #{epic_number} with ticket links...")
        
        if self.dry_run:
            print("  [DRY RUN] Would update epic with ticket links")
            return
        
        # Get current epic body
        view_args = [
            'issue', 'view', str(epic_number),
            '--repo', self.repo,
            '--json', 'body'
        ]
        
        response = self._run_gh_command(view_args)
        
        if not response or 'body' not in response:
            print(f"  ❌ Failed to fetch epic")
            return
        
        current_body = response['body']
        
        # Build ticket list with task checkboxes
        ticket_list = []
        for ticket_id, issue_number in sorted(self.created_issues.items()):
            ticket_list.append(f"- [ ] #{issue_number} - {ticket_id}")
        
        # Update body
        updated_body = current_body.replace(
            "*Will be updated with ticket links*",
            "\n".join(ticket_list)
        )
        
        # Update the issue
        edit_args = [
            'issue', 'edit', str(epic_number),
            '--repo', self.repo,
            '--body', updated_body
        ]
        
        result = subprocess.run(
            ['gh'] + edit_args,
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            print(f"  ✅ Updated Epic with {len(self.created_issues)} ticket links")
        else:
            print(f"  ❌ Failed to update epic: {result.stderr}")
    
    def link_issue_to_epic(self, issue_number: int, epic_number: int, ticket_id: str):
        """
        Create a link between a child issue and the epic using GitHub's issue references.
        This uses a comment to establish the relationship.
        """
        if self.dry_run:
            print(f"  [DRY RUN] Would link #{issue_number} to epic #{epic_number}")
            return
        
        # Add a comment to the child issue referencing the epic
        comment_body = f"Linked to parent epic #{epic_number}"
        
        comment_args = [
            'issue', 'comment', str(issue_number),
            '--repo', self.repo,
            '--body', comment_body
        ]
        
        self._run_gh_command(comment_args)
    
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
            issue_number = self.create_ticket(ticket, epic_number)
            if issue_number and epic_number:
                self.link_issue_to_epic(issue_number, epic_number, ticket['id'])
        
        # Update epic with ticket links
        if epic_number and self.created_issues:
            self.update_epic_with_tickets(epic_number)
        
        # Summary
        print(f"\n✅ Summary:")
        print(f"  - Epic: #{epic_number}" if epic_number else "  - No epic created")
        print(f"  - Tickets created: {len(self.created_issues)}")
        
        if not self.dry_run and epic_number:
            print(f"\n🔗 View Epic: https://github.com/{self.repo}/issues/{epic_number}")


def main():
    parser = argparse.ArgumentParser(
        description='Create GitHub issues from structured markdown using gh CLI',
        epilog='Requires gh CLI to be installed and authenticated (gh auth login)'
    )
    parser.add_argument('file', help='Path to markdown file with tickets')
    parser.add_argument('--repo', required=True, help='GitHub repo (owner/repo)')
    parser.add_argument('--dry-run', action='store_true', help='Preview without creating')
    
    args = parser.parse_args()
    
    # Verify file exists
    if not Path(args.file).exists():
        print(f"❌ Error: File not found: {args.file}")
        sys.exit(1)
    
    # Create issues
    creator = GitHubIssueCreator(args.repo, args.dry_run)
    creator.create_issues_from_file(args.file)


if __name__ == '__main__':
    main()