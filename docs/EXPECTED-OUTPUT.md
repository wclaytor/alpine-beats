# Expected Issue Output Examples

This document shows what the created issues will look like after running `create-epic.py` on `test-epic.md`.

## Epic Issue (Example #123)

### Title
```
Epic: Test Epic for Script Validation
```

### Labels
- `epic`
- `test`

### Body
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

---

## Child Issue #1 (Example #124)

### Title
```
TEST-001: First Test Child Issue
```

### Labels
- `test`
- `child-issue`

### Body
```markdown
**Parent Epic:** #123
**Type:** task
**Priority:** P1
**Story Points:** 2
**Sprint:** 1

---

### TEST-001: First Test Child Issue

**Description:**
This is the first test child issue to validate the create-epic.py script.

**Acceptance Criteria:**
- [ ] Issue is created successfully
- [ ] Issue is linked to parent epic
- [ ] Issue has proper labels and metadata

**Technical Notes:**
- This is a test issue
- No actual implementation required

---
*Part of #123*
```

### Comments
The script also adds a comment to link back to the epic:
```
Linked to parent epic #123
```

---

## Child Issue #2 (Example #125)

### Title
```
TEST-002: Second Test Child Issue
```

### Labels
- `test`
- `child-issue`

### Body
```markdown
**Parent Epic:** #123
**Type:** task
**Priority:** P2
**Story Points:** 3
**Sprint:** 1
**Dependencies:** #124

---

### TEST-002: Second Test Child Issue

**Description:**
This is the second test child issue to validate the create-epic.py script.
This issue depends on TEST-001 to test dependency linking.

**Acceptance Criteria:**
- [ ] Issue is created successfully
- [ ] Issue is linked to parent epic
- [ ] Dependency on TEST-001 is properly referenced
- [ ] Issue has proper labels and metadata

**Technical Notes:**
- This is a test issue with a dependency
- No actual implementation required

---
*Part of #123*
```

### Comments
The script adds a comment linking back to the epic:
```
Linked to parent epic #123
```

### Note about Dependencies
The `**Dependencies:** #124` line shows that TEST-002 depends on TEST-001 (issue #124). The script automatically converts the ticket ID (TEST-001) to the actual issue number (#124) when creating TEST-002.

---

## Relationship Diagram

```
Epic #123: Test Epic for Script Validation
├── Child #124: TEST-001: First Test Child Issue
│   └── No dependencies
└── Child #125: TEST-002: Second Test Child Issue
    └── Depends on: #124 (TEST-001)
```

## GitHub Issue List View

When you run `gh issue list --repo wclaytor/alpine-beats --label test`, you'll see:

```
#125  TEST-002: Second Test Child Issue                    test, child-issue  about 1 minute ago
#124  TEST-001: First Test Child Issue                     test, child-issue  about 1 minute ago
#123  Epic: Test Epic for Script Validation                epic, test         about 1 minute ago
```

## Epic Checkboxes Functionality

The epic issue (#123) contains checkboxes for each child issue:

```markdown
## Child Issues
- [ ] #124 - TEST-001
- [ ] #125 - TEST-002
```

Users can check these boxes in the GitHub UI as child issues are completed. The checkbox status can be manually updated and doesn't automatically sync with issue close status.

## Cross-References

GitHub automatically creates cross-references between issues:

1. **Epic → Child**: The epic body contains `#124` and `#125`, creating links
2. **Child → Epic**: Each child body contains `#123`, creating a back-link
3. **Dependencies**: TEST-002 contains `#124`, showing it depends on TEST-001

These appear in the GitHub UI timeline as "mentioned in" notifications.

## Viewing in GitHub Web Interface

### Epic Issue View
- Click on the issue number to open it
- See the "Child Issues" section with checkboxes
- View "mentioned in" references from child issues
- See labels: `epic`, `test`

### Child Issue View
- See "Parent Epic: #123" at the top of the body
- See metadata: Type, Priority, Story Points, Sprint
- See dependencies (for TEST-002)
- View "mentioned in" reference from the epic
- See labels: `test`, `child-issue`

## Issue Metadata Summary

| Issue | Number | Type | Priority | Points | Sprint | Labels | Dependencies |
|-------|--------|------|----------|--------|--------|--------|--------------|
| Epic | #123 | Epic | - | - | - | epic, test | - |
| TEST-001 | #124 | task | P1 | 2 | 1 | test, child-issue | None |
| TEST-002 | #125 | task | P2 | 3 | 1 | test, child-issue | #124 |

## How to Use These Issues

1. **Track Progress**: Check off boxes in the epic as child issues complete
2. **Discuss Features**: Comment on individual issues for specific discussions
3. **Manage Dependencies**: TEST-002 can't be started until TEST-001 is complete
4. **Filter and Search**: Use labels to filter: `label:test` or `label:epic`
5. **Plan Sprints**: Both child issues are in Sprint 1

## Additional Script Features

The script also:
- Adds appropriate labels to all issues
- Links issues bidirectionally (epic ↔ child)
- Converts ticket IDs to issue numbers in dependencies
- Updates the epic after creating all child issues
- Adds comments to establish relationships
- Includes metadata in structured format
- Preserves markdown formatting from the input file

---

**Note**: The actual issue numbers (#123, #124, #125) will vary based on your repository's issue count. The script reports the actual issue numbers it creates in its output.
