# Testing create-epic.py Script

This document describes the test setup for the `create-epic.py` script that creates GitHub issues from structured markdown files.

## Test Files

### test-epic.md

A minimal test input file containing:
- **1 Epic**: "Test Epic for Script Validation"
- **2 Child Issues**: TEST-001 and TEST-002
- **Demonstrates**: Issue creation, linking, dependencies, and metadata

## Quick Start

### 1. Prerequisites

Ensure you have:
- Python 3.6+ installed
- GitHub CLI (`gh`) installed
- GitHub CLI authenticated: `gh auth login`
- PyYAML package: `pip install pyyaml`

### 2. Test with Dry Run

First, validate the input file format without creating actual issues:

```bash
cd /path/to/alpine-beats
python3 scripts/create-epic.py test-epic.md --repo wclaytor/alpine-beats --dry-run
```

Expected output shows what would be created:
```
📚 Parsing test-epic.md
🎯 Creating Epic: Epic: Test Epic for Script Validation
  [DRY RUN] Would create epic with title: Epic: Test Epic for Script Validation

📋 Creating 2 tickets...
📝 Creating TEST-001: First Test Child Issue
  [DRY RUN] Would create ticket TEST-001
...
```

### 3. Create Actual Issues

Once the dry run looks good, create real issues:

```bash
python3 scripts/create-epic.py test-epic.md --repo wclaytor/alpine-beats
```

The script will:
1. ✅ Create the epic issue
2. ✅ Create TEST-001 child issue
3. ✅ Create TEST-002 child issue (with dependency on TEST-001)
4. ✅ Link child issues back to the epic
5. ✅ Update epic with checkboxes for child issues

### 4. Verify Issues Were Created

Use the provided verification script:

```bash
./scripts/verify-issues.sh wclaytor/alpine-beats test
```

Or manually verify with `gh` CLI:

```bash
# List all issues
gh issue list --repo wclaytor/alpine-beats --limit 10

# View the epic (replace NUMBER with actual issue number)
gh issue view NUMBER --repo wclaytor/alpine-beats

# List issues with 'test' label
gh issue list --repo wclaytor/alpine-beats --label test --state all
```

## Test File Structure

### Epic Definition

```yaml
---
epic:
  title: "Epic: Test Epic for Script Validation"
  labels: ["epic", "test"]
  milestone: ""
  description: |
    This is a test epic created to validate the create-epic.py script functionality.
---
```

### Child Issue Definition

```yaml
---
ticket:
  id: TEST-001
  title: First Test Child Issue
  type: task
  priority: P1
  points: 2
  sprint: 1
  labels: ["test", "child-issue"]
  assignee: ""
  dependencies: []
---

### TEST-001: First Test Child Issue

**Description:**
Issue description...

**Acceptance Criteria:**
- [ ] Criterion 1
- [ ] Criterion 2
```

## What Gets Created

When you run the script on `test-epic.md`, it creates:

### Epic Issue

- **Title**: "Epic: Test Epic for Script Validation"
- **Labels**: epic, test
- **Body**: Contains description and a list of child issues
- **Child Issues Section**: Updated with checkboxes linking to TEST-001 and TEST-002

Example epic body:
```markdown
This is a test epic created to validate the create-epic.py script functionality.

Success Criteria:
- Script successfully parses the markdown file
- Epic issue is created in GitHub
- Child issues are created and linked to the epic

## Child Issues
- [ ] #124 - TEST-001
- [ ] #125 - TEST-002
```

### Child Issue: TEST-001

- **Title**: "TEST-001: First Test Child Issue"
- **Labels**: test, child-issue
- **Body**: Includes:
  - Parent Epic: #123
  - Type: task
  - Priority: P1
  - Story Points: 2
  - Sprint: 1
  - Full description with acceptance criteria
  - Link back to parent epic

### Child Issue: TEST-002

- **Title**: "TEST-002: Second Test Child Issue"
- **Labels**: test, child-issue
- **Body**: Includes:
  - Parent Epic: #123
  - Type: task
  - Priority: P2
  - Story Points: 3
  - Sprint: 1
  - Dependencies: #124 (TEST-001)
  - Full description with acceptance criteria
  - Link back to parent epic

## Verification Checklist

After running the script, verify:

- [ ] Epic issue was created with correct title and labels
- [ ] TEST-001 child issue was created
- [ ] TEST-002 child issue was created
- [ ] TEST-002 shows dependency on TEST-001 (references #124)
- [ ] Epic issue was updated with links to both child issues
- [ ] Both child issues reference the parent epic
- [ ] All issues have the 'test' label
- [ ] Issue metadata (priority, points, sprint) is correct

## Cleaning Up Test Issues

After testing, you may want to close the test issues:

```bash
# Close individual issues
gh issue close NUMBER --repo wclaytor/alpine-beats

# Or close all issues with 'test' label
gh issue list --repo wclaytor/alpine-beats --label test --json number --jq '.[].number' | \
  xargs -I {} gh issue close {} --repo wclaytor/alpine-beats
```

## Troubleshooting

### Script fails with authentication error

**Solution**: Ensure `gh auth login` has been run and completed successfully

### Issues are not created

**Solution**: 
1. Check your GitHub permissions - you need write access to the repository
2. Verify the repository name is correct: `wclaytor/alpine-beats`
3. Check if there are API rate limits: wait a few minutes and try again

### Dry run works but actual creation fails

**Solution**: 
1. Verify gh CLI authentication: `gh auth status`
2. Check repository permissions: `gh repo view wclaytor/alpine-beats`
3. Review script output for specific error messages

## Advanced Usage

### Using with a different repository

```bash
python3 scripts/create-epic.py test-epic.md --repo username/repo-name
```

### Creating your own test file

1. Copy `test-epic.md` to a new file
2. Update the epic and ticket definitions
3. Run with `--dry-run` first to validate
4. Create actual issues

## Script Improvements

The `create-epic.py` script was improved to:

1. **Skip authentication in dry-run mode**: You can now validate input files without authenticating with GitHub
2. **Better error messages**: Clear feedback about what's happening
3. **Dependency linking**: Automatically converts ticket IDs to issue numbers
4. **Epic updates**: Automatically updates the epic with links to all child issues

## Next Steps

1. ✅ Test the script with the provided test file
2. ✅ Verify issues were created correctly
3. Create your own markdown files for real epics and features
4. Use the same format for your project planning

## More Information

- **Detailed usage guide**: See `docs/CREATE-EPIC-USAGE.md`
- **Example with many tickets**: See `docs/features/tickets-example.md`
- **GitHub CLI docs**: https://cli.github.com/manual/
