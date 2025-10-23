# Using create-epic.py Script

## Overview

The `create-epic.py` script creates GitHub issues from structured markdown files with YAML frontmatter. It uses the GitHub CLI (`gh`) to interact with the GitHub API.

## Prerequisites

1. **GitHub CLI (gh)**: Must be installed and authenticated
   ```bash
   # Install gh CLI (if not already installed)
   # See: https://cli.github.com/
   
   # Authenticate with GitHub
   gh auth login
   ```

2. **Python 3**: Required to run the script
   ```bash
   python3 --version  # Should be 3.6 or higher
   ```

3. **Required Python packages**: PyYAML
   ```bash
   pip install pyyaml
   ```

## Test Input File Format

The script expects a markdown file with YAML frontmatter blocks. See `test-epic.md` for a complete example.

### Epic Frontmatter

```yaml
---
epic:
  title: "Epic: Your Epic Title"
  labels: ["epic", "feature"]
  milestone: "Sprint 1"
  description: |
    Epic description goes here.
    Can be multi-line.
---
```

### Child Issue (Ticket) Frontmatter

```yaml
---
ticket:
  id: TICKET-001
  title: Issue Title
  type: task
  priority: P1
  points: 3
  sprint: 1
  labels: ["feature", "backend"]
  assignee: "username"
  dependencies: ["TICKET-000"]  # Optional, references other ticket IDs
---

### TICKET-001: Issue Title

**Description:**
Detailed description of the issue.

**Acceptance Criteria:**
- [ ] Criterion 1
- [ ] Criterion 2
```

## Usage

### 1. Dry Run (Preview Mode)

Test your input file without creating actual issues:

```bash
python3 scripts/create-epic.py test-epic.md \
  --repo wclaytor/alpine-beats \
  --dry-run
```

Expected output:
```
📚 Parsing test-epic.md
🎯 Creating Epic: Epic: Test Epic for Script Validation
  [DRY RUN] Would create epic with title: Epic: Test Epic for Script Validation

📋 Creating 2 tickets...
📝 Creating TEST-001: First Test Child Issue
  [DRY RUN] Would create ticket TEST-001
  [DRY RUN] Would link #1000 to epic #999
📝 Creating TEST-002: Second Test Child Issue
  [DRY RUN] Would create ticket TEST-002
  [DRY RUN] Would link #1001 to epic #999
🔄 Updating Epic #999 with ticket links...
  [DRY RUN] Would update epic with ticket links

✅ Summary:
  - Epic: #999
  - Tickets created: 2
```

### 2. Create Actual Issues

Once satisfied with the dry run, create real issues:

```bash
python3 scripts/create-epic.py test-epic.md \
  --repo wclaytor/alpine-beats
```

Expected output:
```
📚 Parsing test-epic.md
🎯 Creating Epic: Epic: Test Epic for Script Validation
  ✅ Created Epic: #123

📋 Creating 2 tickets...
📝 Creating TEST-001: First Test Child Issue
  ✅ Created: #124
📝 Creating TEST-002: Second Test Child Issue
  ✅ Created: #125
🔄 Updating Epic #123 with ticket links...
  ✅ Updated Epic with 2 ticket links

✅ Summary:
  - Epic: #123
  - Tickets created: 2

🔗 View Epic: https://github.com/wclaytor/alpine-beats/issues/123
```

### 3. Verify Issues Were Created

Use the `gh` CLI to verify the issues:

```bash
# List recent issues
gh issue list --repo wclaytor/alpine-beats --limit 10

# View the epic issue
gh issue view 123 --repo wclaytor/alpine-beats

# View a child issue
gh issue view 124 --repo wclaytor/alpine-beats

# View issues with specific label
gh issue list --repo wclaytor/alpine-beats --label test
```

## Test File Description

The `test-epic.md` file contains:

1. **One Epic**: "Test Epic for Script Validation"
   - Title: "Epic: Test Epic for Script Validation"
   - Labels: epic, test
   - Description with success criteria

2. **Two Child Issues**:
   - **TEST-001**: First Test Child Issue
     - Type: task
     - Priority: P1
     - Points: 2
     - Labels: test, child-issue
     - No dependencies
   
   - **TEST-002**: Second Test Child Issue
     - Type: task
     - Priority: P2
     - Points: 3
     - Labels: test, child-issue
     - Depends on: TEST-001

## Features Demonstrated

1. **Epic Creation**: Creates a parent epic issue
2. **Child Issue Creation**: Creates linked child issues
3. **Dependency Tracking**: TEST-002 depends on TEST-001
4. **Labels**: Issues are tagged with appropriate labels
5. **Metadata**: Priority, points, sprint information
6. **Linking**: Epic is updated with links to all child issues
7. **Cross-referencing**: Child issues link back to the epic

## Troubleshooting

### Issue: "gh CLI is not authenticated"

**Solution**: Run `gh auth login` to authenticate with GitHub

### Issue: "FileNotFoundError: gh"

**Solution**: Install GitHub CLI from https://cli.github.com/

### Issue: "No module named 'yaml'"

**Solution**: Install PyYAML: `pip install pyyaml`

### Issue: Rate limiting errors

**Solution**: The script includes a small delay between issue creation. If you hit rate limits, wait a few minutes and try again.

## Script Improvements Made

1. **Dry-run authentication fix**: The script now skips GitHub CLI authentication check when running in `--dry-run` mode, allowing you to validate your input file format without being authenticated.

## Next Steps

1. Authenticate with GitHub: `gh auth login`
2. Run the script in dry-run mode to validate your input file
3. Run the script to create actual issues
4. Verify the issues using `gh issue list` and `gh issue view`
5. Create your own markdown files following the same format

## Example Commands

```bash
# Validate test file format
python3 scripts/create-epic.py test-epic.md --repo wclaytor/alpine-beats --dry-run

# Create issues from test file
python3 scripts/create-epic.py test-epic.md --repo wclaytor/alpine-beats

# List all issues
gh issue list --repo wclaytor/alpine-beats

# View specific issue
gh issue view <issue-number> --repo wclaytor/alpine-beats

# Search for test issues
gh issue list --repo wclaytor/alpine-beats --label test
```
