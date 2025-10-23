# Quick Reference: create-epic.py Testing

## Prerequisites Setup

```bash
# 1. Install GitHub CLI (if needed)
# Visit: https://cli.github.com/

# 2. Authenticate with GitHub
gh auth login

# 3. Install Python dependencies
pip install pyyaml
```

## Test Commands (In Order)

### Step 1: Dry Run (Validate Format)
```bash
python3 scripts/create-epic.py test-epic.md --repo wclaytor/alpine-beats --dry-run
```
**Expected**: Shows preview of what would be created (no actual issues)

### Step 2: Create Issues
```bash
python3 scripts/create-epic.py test-epic.md --repo wclaytor/alpine-beats
```
**Expected**: Creates 1 epic + 2 child issues in GitHub

### Step 3: Verify Issues Created
```bash
# Using verification script
./scripts/verify-issues.sh wclaytor/alpine-beats test

# Or manually with gh CLI
gh issue list --repo wclaytor/alpine-beats --label test
```
**Expected**: Shows the 3 created issues with 'test' label

## What Gets Created

| Issue | Title | Labels | Type |
|-------|-------|--------|------|
| Epic | "Epic: Test Epic for Script Validation" | epic, test | Epic |
| Child 1 | "TEST-001: First Test Child Issue" | test, child-issue | Task |
| Child 2 | "TEST-002: Second Test Child Issue" | test, child-issue | Task |

## View Created Issues

```bash
# List all test issues
gh issue list --repo wclaytor/alpine-beats --label test --state all

# View specific issue (replace NUMBER)
gh issue view NUMBER --repo wclaytor/alpine-beats

# View epic issue in browser
gh issue view NUMBER --repo wclaytor/alpine-beats --web
```

## Clean Up Test Issues

```bash
# Close a single issue
gh issue close NUMBER --repo wclaytor/alpine-beats

# Close all test issues at once
gh issue list --repo wclaytor/alpine-beats --label test --json number --jq '.[].number' | \
  xargs -I {} gh issue close {} --repo wclaytor/alpine-beats
```

## Troubleshooting

| Problem | Solution |
|---------|----------|
| "gh CLI is not authenticated" | Run `gh auth login` |
| "gh CLI is not installed" | Install from https://cli.github.com/ |
| "No module named 'yaml'" | Run `pip install pyyaml` |
| Can't create issues | Check repo permissions with `gh repo view wclaytor/alpine-beats` |

## File Locations

- **Test input**: `test-epic.md`
- **Script**: `scripts/create-epic.py`
- **Verification**: `scripts/verify-issues.sh`
- **Full docs**: `docs/CREATE-EPIC-USAGE.md`
- **Test README**: `TEST-EPIC-README.md`

## Success Criteria Checklist

After running the script, verify:

- [ ] Epic issue created with title "Epic: Test Epic for Script Validation"
- [ ] TEST-001 issue created
- [ ] TEST-002 issue created
- [ ] TEST-002 references TEST-001 as dependency
- [ ] Epic updated with links to child issues
- [ ] All issues have 'test' label
- [ ] Child issues reference parent epic
