# NOTES Template Guide

## Purpose

This template defines the standard format for adding entries to the notes system. All team members—whether human developers, AI assistants (Claude, GitHub Copilot), or specific roles working on issues—should follow this format to maintain consistency and knowledge sharing across the project.

## 📅 Note Dating & Git Source of Truth

### Default Behavior: Current Date
**When creating notes, AI assistants should use the current date by default** unless the user explicitly requests a different date.

### User-Requested Past Dates
Users may request notes with past dates for legitimate reasons:
- "Let me add a note about what I did last Thursday"
- Documenting work that was completed but not yet noted
- Filling in gaps in project history
- Migrating old notes to the new system

**When a user requests a past date, honor that request.** Users are operating on their own timeline and we respect their documentation needs.

### Git as Source of Truth
**Git commit timestamps are the authoritative record** of when notes were actually created and added to the repository. This provides:
- ✅ **Transparency**: Anyone can see when documentation was written
- ✅ **Accountability**: Version control shows the real timeline
- ✅ **Non-disputable record**: Git history cannot be altered without trace
- ✅ **Flexibility for users**: Note dates reflect event dates, Git shows documentation dates

**Key Principle**: The note filename date represents **when events occurred**. The Git commit date shows **when the note was documented**. Both are valid and important pieces of information.

### For AI Assistants
- **Default**: Use current date (today) when creating notes
- **User specifies date**: Use the date the user requests
- **No backdating without user request**: Don't create past-dated notes on your own initiative
- **Trust Git**: Let version control handle the documentation timeline

## Why We Keep Notes

- 📚 **Knowledge Transfer**: Share what we learned with future team members
- 🔍 **Decision Tracking**: Document why we made specific choices
- 🎯 **Progress Visibility**: Show what's actually happening in the project
- 🐛 **Problem Solving**: Record solutions to challenges for future reference
- 🤝 **Team Alignment**: Keep everyone informed about changes and developments
- 📈 **Project History**: Build a narrative of the project's evolution

## When to Add a Note

Add a note when:
- ✅ Completing a significant feature or milestone
- ✅ Making important architectural or design decisions
- ✅ Discovering and solving complex problems
- ✅ Completing a sprint or major work session
- ✅ Making changes that affect multiple parts of the system
- ✅ Establishing new patterns, policies, or standards
- ✅ Learning something valuable that others should know
- ✅ Closing GitHub issues that involved significant work

Don't add notes for:
- ❌ Trivial typo fixes or formatting changes
- ❌ Routine maintenance unless it reveals insights
- ❌ Work-in-progress unless documenting a decision point
- ❌ Every single commit (notes should be meaningful summaries)

## Standard Note Format

```markdown
## YYYY-MM-DD | Brief Descriptive Title

### Session Overview
**Participants**: [Who worked on this - roles, team members, AI assistants]  
**Duration**: [Time span or "Quick update" or "Multi-day sprint"]  
**Focus**: [One-line summary of what this session was about]

### What We Accomplished

[Describe the key achievements, organized with subheadings if multiple areas]

#### 1. **Achievement Category 1**
[Details about what was accomplished in this area]

#### 2. **Achievement Category 2**
[Details about what was accomplished in this area]

### Key Findings

[If applicable - important discoveries, insights, or learnings]

**Strengths Identified**:
- ✅ [What worked well]
- ✅ [Positive patterns discovered]

**Issues Discovered**:
- ⚠️ [Problems found]
- ⚠️ [Technical debt identified]

**Opportunities**:
- 💡 [Ideas for improvement]
- 💡 [Future enhancements]

### Technical Decisions Made

[If applicable - document significant technical choices]

**Decision**: [What was decided]  
**Rationale**: [Why this choice was made]  
**Alternatives Considered**: [Other options and why they weren't chosen]  
**Impact**: [How this affects the system]

### Implementation Details

[If applicable - code patterns, configurations, or technical specifics]

```[language]
// Example code or configuration
```

### Quality & Testing

[If applicable - testing approach, quality checks performed]

- [ ] Unit tests added/updated
- [ ] Integration tests performed
- [ ] Accessibility validated
- [ ] Performance benchmarked
- [ ] Cross-browser tested
- [ ] Documentation updated

### Issues & Tickets

[Reference related GitHub issues or tickets]

**Related Issues**: #123, #456  
**Closed Issues**: #789  
**New Issues Created**: #101

### Next Steps

[What needs to happen next]

**Immediate**:
1. [Action item 1]
2. [Action item 2]

**Short-term** (next session/sprint):
1. [Action item 3]
2. [Action item 4]

**Long-term** (future work):
1. [Action item 5]
2. [Action item 6]

### Lessons Learned

[Reflections and insights for continuous improvement]

**What Worked Well**:
- [Success pattern 1]
- [Success pattern 2]

**Challenges Encountered**:
- [Challenge 1 and how it was addressed]
- [Challenge 2 and resolution]

**For Next Time**:
- [Improvement idea 1]
- [Improvement idea 2]

### Resources Referenced

[Documentation, links, or resources used]

**Internal Documentation**:
- `/docs/path/to/file.md` - Description
- `/skills/skill-name/SKILL.md` - Purpose

**External Resources**:
- [Link Title](URL) - Brief description

### Metrics (Optional)

[If relevant - quantifiable outcomes]

- **Lines of Code**: Added X, Modified Y, Deleted Z
- **Files Changed**: N files
- **Test Coverage**: X%
- **Performance**: Improved by X%
- **Time Spent**: X hours

---

**Status**: [✅ Complete | 🚧 In Progress | ⏸️ Paused | 🔄 Ongoing]  
**Next Review**: [When or what triggers next review]

---
```

## Role-Specific Note Guidelines

Different roles focus on different aspects. Here's what each role should emphasize in their notes:

### 🎯 Director Notes

**Focus**: Coordination, planning, progress tracking

**Emphasize**:
- Sprint planning and retrospective summaries
- Team coordination activities
- Risk management and mitigation
- Milestone completion
- Cross-role collaboration facilitation
- Blockers removed and how

**Example Title**: "Sprint 3 Planning & Retrospective Summary"

**Key Sections**:
- Session Overview (who participated, what was planned)
- What We Accomplished (sprint goals, velocity)
- Issues & Tickets (sprint backlog, completed work)
- Next Steps (next sprint planning)
- Lessons Learned (process improvements)

### 📚 Product-Owner Notes

**Focus**: Requirements, user stories, business value

**Emphasize**:
- User story creation and refinement
- Feature prioritization decisions
- Stakeholder feedback and requirements
- Acceptance criteria definition
- Release planning
- Value delivery

**Example Title**: "User Authentication Feature Requirements Defined"

**Key Sections**:
- What We Accomplished (stories created, requirements gathered)
- Key Findings (user needs discovered)
- Technical Decisions Made (feature scope, priorities)
- Issues & Tickets (related stories and epics)
- Next Steps (development handoff)

### 🏗️ Architect Notes

**Focus**: System design, technical decisions, architecture

**Emphasize**:
- Architecture designs and blueprints
- Technology stack decisions
- Data model and flow design
- Performance and security strategies
- Technical feasibility assessments
- Integration patterns

**Example Title**: "Multi-Canvas Rendering Architecture Designed"

**Key Sections**:
- What We Accomplished (architecture designed)
- Technical Decisions Made (detailed ADRs)
- Implementation Details (patterns, code structure)
- Quality & Testing (performance considerations)
- Resources Referenced (technical documentation)

### 💻 Developer Notes

**Focus**: Implementation, code quality, technical execution

**Emphasize**:
- Features implemented
- Code patterns applied
- Performance optimizations
- Bug fixes and troubleshooting
- Testing completed
- Technical challenges solved

**Example Title**: "Audio Sequencer Refactored with Web Audio API Scheduling"

**Key Sections**:
- What We Accomplished (code implemented)
- Implementation Details (code samples, patterns)
- Quality & Testing (tests written, validation)
- Issues & Tickets (closed issues)
- Lessons Learned (technical insights)

### 🎨 Designer Notes

**Focus**: UI/UX design, visual systems, accessibility

**Emphasize**:
- Design specifications created
- UI component designs
- Accessibility compliance
- Theme and color systems
- Responsive layouts
- User interaction patterns

**Example Title**: "Control Panel UI System Designed with WCAG AA Compliance"

**Key Sections**:
- What We Accomplished (designs created)
- Implementation Details (design specs, components)
- Quality & Testing (accessibility validated)
- Resources Referenced (design systems, guidelines)

### 🧪 QA-Engineer Notes

**Focus**: Testing, quality validation, bug reporting

**Emphasize**:
- Test plans and strategies
- Testing results and findings
- Bugs discovered and reported
- Quality validations performed
- Cross-browser/device testing
- Performance benchmarks

**Example Title**: "Authentication Feature Testing Complete - 3 Issues Found"

**Key Sections**:
- What We Accomplished (testing completed)
- Key Findings (bugs, issues, passes)
- Quality & Testing (detailed results)
- Issues & Tickets (bugs filed)
- Next Steps (fixes needed)

### 🎓 Domain-Expert Notes

**Focus**: Domain knowledge, business rules, compliance

**Emphasize**:
- Domain models defined
- Business rules documented
- Industry standards and compliance
- Terminology and glossary updates
- Domain-specific validations
- Regulatory requirements

**Example Title**: "Music Production Domain Glossary Established"

**Key Sections**:
- What We Accomplished (domain knowledge captured)
- Technical Decisions Made (business rules)
- Implementation Details (domain models)
- Resources Referenced (industry standards)

## GitHub Copilot Integration

When GitHub Copilot works on issues, it should:

1. **Start with Context**: Reference the issue number and title
2. **Document the Journey**: Describe the approach taken
3. **Capture Decisions**: Explain why specific choices were made
4. **Share Insights**: Document any discoveries or learnings
5. **List Actions**: Be specific about what files were changed
6. **Connect the Dots**: Reference related issues or documentation

**Example Copilot Note Entry**:

```markdown
## 2025-10-22 | Implement Toast Notification System (Issue #42)

### Session Overview
**Participants**: GitHub Copilot (Developer role)  
**Duration**: 45 minutes  
**Focus**: Adding user feedback notifications to the application

### What We Accomplished

#### 1. **Created Toast Notification Component**

Implemented an Alpine.js-based toast notification system for user feedback.

**Files Modified**:
- `index.html` - Added toast component and Alpine.js state management
- `styles.css` - Added toast styling with animations

**Features Implemented**:
- Success, error, warning, and info toast types
- Auto-dismiss after 3 seconds (configurable)
- Queue system for multiple toasts
- Accessible with ARIA labels
- Mobile-responsive positioning

### Implementation Details

\```javascript
// Alpine.js toast component
function toastManager() {
    return {
        toasts: [],
        show(message, type = 'info', duration = 3000) {
            const id = Date.now();
            this.toasts.push({ id, message, type });
            setTimeout(() => this.dismiss(id), duration);
        },
        dismiss(id) {
            this.toasts = this.toasts.filter(t => t.id !== id);
        }
    }
}
\```

### Quality & Testing

- [x] Component works across all toast types
- [x] Tested on Chrome, Firefox, Safari
- [x] Screen reader announces toast messages
- [x] Mobile responsive (tested on iPhone, Android)
- [x] No console errors or warnings

### Issues & Tickets

**Closed Issues**: #42  
**Related Issues**: #38 (Export Settings needs toast feedback)

### Next Steps

**Immediate**:
1. Integrate toast notifications with export settings feature (#38)
2. Add toasts to randomize button actions
3. Update documentation with toast usage examples

### Lessons Learned

**What Worked Well**:
- Alpine.js makes state management simple for this use case
- CSS animations provide smooth user experience
- Queue system prevents toast overload

**Challenges Encountered**:
- Initial positioning conflicted with control panel on mobile
- Solution: Added z-index management and tested thoroughly

**For Next Time**:
- Consider extracting toast component to reusable skill
- Document toast types and usage in design system

---

**Status**: ✅ Complete | Ready for integration  
**Next Review**: After integration with export settings feature
```

## AI Assistant Guidelines

### For Claude

When adding notes to `NOTES.md`:

1. **Use the template structure** from this document
2. **Identify your role context** (which role were you acting as?)
3. **Be specific about changes**: List files modified, decisions made
4. **Capture the why**: Don't just say what, explain why
5. **Think about future readers**: What would help someone understand this later?
6. **Keep it scannable**: Use headings, bullets, emojis for visual organization
7. **Link to resources**: Reference docs, issues, external resources
8. **Be honest about challenges**: Document problems and solutions

### For GitHub Copilot

When working on issues:

1. **Reference the issue number** in your note title
2. **Document your approach**: How did you solve the problem?
3. **List all changes**: Files created, modified, deleted
4. **Include code samples**: Show key patterns or implementations
5. **Note testing performed**: What did you validate?
6. **Create follow-up items**: What still needs to be done?
7. **Tag related issues**: Connect the work to the larger context

### For Other AI Agents

1. **Identify yourself**: Make it clear who/what created this note
2. **State your role**: Were you acting as Developer, Designer, etc.?
3. **Follow the template**: Use the structure defined here
4. **Be consistent**: Match the format of existing notes
5. **Add value**: Don't just log actions, share insights and knowledge

## Markdown Formatting Guidelines

### Required Elements

- **Date in ISO format**: `YYYY-MM-DD`
- **Level 2 heading for entry**: `## YYYY-MM-DD | Title`
- **Level 3 headings for sections**: `### Section Name`
- **Proper list formatting**: Consistent bullets (`-` or `*`)
- **Horizontal rule separator**: `---` between entries

### Optional Enhancements

- **Emojis for visual scanning**: Use role icons (🎯📚🏗️💻🎨🧪🎓)
- **Status indicators**: ✅ ❌ ⚠️ 💡 🔄 🚧
- **Code blocks with language**: \`\`\`javascript or \`\`\`bash
- **Bold for emphasis**: `**Important point**`
- **Links to issues**: `#123` or `[Issue Title](#123)`
- **Internal links**: `[File Path](/path/to/file.md)`

### Formatting Don'ts

- ❌ Don't use inconsistent heading levels
- ❌ Don't forget closing code block markers
- ❌ Don't use tabs (use spaces for indentation)
- ❌ Don't break list formatting (consistent bullets)
- ❌ Don't forget separators between entries
- ❌ Don't use HTML unless necessary
- ❌ Don't create broken internal links

## Examples by Complexity

### Minimal Note (Quick Update)

```markdown
## 2025-10-23 | Fixed Typography Bug in Mobile View

### Session Overview
**Participants**: Developer  
**Duration**: 15 minutes  
**Focus**: Resolving CSS text overflow issue on mobile devices

### What We Accomplished

Fixed text overflow in navigation menu on screens below 480px width.

**Files Modified**: `styles.css`  
**Change**: Added `text-overflow: ellipsis` to `.nav-item`

### Issues & Tickets

**Closed Issues**: #67

---

**Status**: ✅ Complete

---
```

### Standard Note (Feature Work)

```markdown
## 2025-10-23 | Implemented Preset Save/Load System

### Session Overview
**Participants**: Developer + Product-Owner  
**Duration**: 3 hours  
**Focus**: Adding preset management to control panel

### What We Accomplished

#### 1. **Preset Storage System**
Implemented LocalStorage-based preset management allowing users to save and load their favorite configurations.

**Features Added**:
- Save current settings as named preset
- Load presets from dropdown menu
- Delete unwanted presets
- Import/Export presets as JSON

#### 2. **UI Enhancements**
Added preset controls to control panel with clear visual feedback.

### Implementation Details

\```javascript
// Preset management with LocalStorage
savePreset(name) {
    const preset = {
        tempo: this.tempo,
        mode: this.mode,
        theme: this.theme,
        // ... other settings
    };
    localStorage.setItem(`preset_${name}`, JSON.stringify(preset));
    this.loadPresetList();
}
\```

### Quality & Testing

- [x] Presets persist across sessions
- [x] Export/Import works correctly
- [x] UI updates when preset loaded
- [x] Error handling for storage quota

### Issues & Tickets

**Closed Issues**: #45  
**Related Issues**: #38 (Export Settings)

### Next Steps

**Immediate**:
1. Add default presets ("Focus", "Party", "Ambient")
2. Add preset sharing via URL parameters

---

**Status**: ✅ Complete  
**Next Review**: After user feedback on preset UX

---
```

### Comprehensive Note (Major Feature or Sprint)

Use the full template structure shown at the beginning of this document, including all relevant sections.

## Validation Checklist

Before adding your note to `NOTES.md`, verify:

- [ ] Date is in YYYY-MM-DD format
- [ ] Title is clear and descriptive
- [ ] Session Overview is complete
- [ ] At least one "What We Accomplished" section
- [ ] All code blocks have closing markers
- [ ] All links are valid (test internal links)
- [ ] Consistent bullet point style
- [ ] Separator (---) at the end of entry
- [ ] No broken Markdown formatting
- [ ] Status indicator included
- [ ] Entry adds value (not just noise)

## Integration with Tools

### GitHub Issues

Reference notes in issue comments:
```markdown
Work completed - see notes: [2025-10-23 Entry](../NOTES.md#2025-10-23--title)
```

### Pull Requests

Link to notes in PR descriptions:
```markdown
Implementation details documented in project notes:
- [NOTES.md Entry for 2025-10-23](../NOTES.md)
```

### Commit Messages

Reference notes in detailed commits:
```
feat: implement preset save/load system

See NOTES.md entry for 2025-10-23 for full implementation details and rationale.

Closes #45
```

## Maintaining NOTES.md

### Periodic Reviews

- **Monthly**: Review notes for patterns and insights
- **Quarterly**: Archive old notes to dated files if needed
- **Annually**: Create year-in-review summary

### Archive Strategy (Optional)

If `NOTES.md` becomes too large:

1. Create `/docs/notes/` directory
2. Move old notes to `/docs/notes/NOTES-YYYY.md`
3. Keep current quarter in main `NOTES.md`
4. Add links to archived notes

---

## Quick Reference

**Minimum Requirements**:
- Date + Title (Level 2 heading)
- Session Overview
- What We Accomplished
- Status indicator
- Separator (---)

**Recommended Additions**:
- Implementation details or code samples
- Issues & tickets references
- Next steps
- Lessons learned

**Role-Specific Focus**:
- Director: Coordination, planning
- Product-Owner: Requirements, value
- Architect: Technical decisions, design
- Developer: Implementation, code
- Designer: UI/UX, accessibility
- QA-Engineer: Testing, quality
- Domain-Expert: Business rules, compliance

---

*This template is a living document. Update it as you discover better patterns for knowledge sharing and documentation.*
