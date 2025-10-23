# Daily Folder System - Documentation

## 🎯 Overview

This is the **Daily Folder System** - an organizational structure for capturing daily team activities, standup meetings, individual role notes, and detailed deep-dive documents all in one centralized, date-organized location.

---

## 📂 Folder Structure

```
docs/notes/YYYY/MM/YYYY.MM.DD/
├── standup.md              # Daily standup meeting notes
├── director.md             # Director's daily notes
├── product-owner.md        # Product Owner's daily notes
├── architect.md            # Architect's daily notes
├── developer.md            # Developer's daily notes
├── designer.md             # Designer's daily notes
├── qa-engineer.md          # QA Engineer's daily notes
├── domain-expert.md        # Domain Expert's daily notes
├── [team-member].md        # Additional team member notes
└── deep-dives/             # Detailed analysis documents
    ├── [topic-1].md
    ├── [topic-2].md
    └── ...
```

---

## 🗂️ File Types Explained

### `standup.md` - Daily Standup Meeting

**Purpose**: Capture the daily standup meeting with all team updates

**Key Sections**:
- Meeting info (date, time, attendees)
- Sprint overview and metrics
- Each role's yesterday/today/blockers
- Action items and decisions
- Next standup info

**Updated**: During or immediately after standup  
**Owner**: Director (facilitator)

**Use this for**:
- Team synchronization
- Tracking daily progress
- Identifying blockers
- Recording action items

---

### Role-Specific Files (e.g., `designer.md`, `developer.md`)

**Purpose**: Individual role's daily work log and notes

**Key Sections**:
- Session overview (who, when, what)
- Accomplishments for the day
- Technical details or designs created
- Issues worked on
- Next steps

**Updated**: Throughout the day or end of day  
**Owner**: The role (Designer, Developer, etc.)

**Use this for**:
- Personal work tracking
- Detailed technical notes
- Sharing context with team
- Knowledge capture

---

### `deep-dives/` - Detailed Analysis Documents

**Purpose**: In-depth documentation of specific topics, decisions, or investigations

**Examples**:
- Architecture design documents
- Implementation strategies
- Technical spike results
- Research findings
- Complex problem analysis
- Design system definitions

**Updated**: When deep analysis is needed  
**Owner**: Lead role for that topic

**Use this for**:
- Complex topics needing detailed explanation
- Cross-role collaboration documents
- Reference documentation
- Decision records

---

## 📝 Naming Conventions

### Daily Folders
```
YYYY.MM.DD/
```
- Use dots as separators
- Always use 4-digit year, 2-digit month, 2-digit day
- Examples: `2025.10.22/`, `2025.12.31/`

### Role Files
```
[role-name].md
```
- Lowercase with hyphens
- Match role names from `/docs/roles/`
- Examples: `designer.md`, `product-owner.md`, `qa-engineer.md`

### Team Member Files
```
[username].md
```
- Use team member's username or identifier
- Lowercase, no spaces
- Examples: `bpc.md`, `johndoe.md`, `jane-smith.md`

### Deep Dive Documents
```
[topic-name].md
```
- Descriptive kebab-case names
- Clear topic identification
- Examples: 
  - `accessibility-implementation-strategy.md`
  - `8px-grid-spacing-system.md`
  - `database-migration-plan.md`
  - `authentication-architecture.md`

---

## 🔄 Daily Workflow

### Morning (Before Standup)

1. **Create today's folder** (if not exists)
   ```bash
   mkdir -p docs/notes/2025/10/2025.10.22
   mkdir -p docs/notes/2025/10/2025.10.22/deep-dives
   ```

2. **Copy role file templates** (if needed)
   - Use templates from an existing day or create from scratch
   - Each role starts with empty template ready to fill

3. **Review yesterday's notes**
   - Check your role file from previous day
   - Prepare "yesterday" update for standup

### During Standup (9:00 AM)

1. **Director updates `standup.md`**
   - Fill in each role's updates
   - Record blockers and action items
   - Note decisions made

2. **Each role reports**:
   - Yesterday's accomplishments
   - Today's plan
   - Any blockers

### Throughout Day

1. **Update your role file**
   - Add notes as you work
   - Document decisions
   - Capture learnings

2. **Create deep-dives as needed**
   - Start a deep-dive doc when:
     - Topic needs detailed analysis
     - Multiple roles collaborating
     - Creating reference material
     - Documenting complex decisions

### End of Day

1. **Finalize your role file**
   - Ensure accomplishments documented
   - Set status (Complete, In Progress, etc.)
   - Note next steps

2. **Finalize deep-dives**
   - Complete any deep-dive docs started
   - Ensure clear status and next steps
   - Link from role files if needed

---

## 🎭 Role-Specific Guidelines

### 🎯 Director (`director.md`)

**Focus**: Coordination, facilitation, tracking

**Daily Must-Haves**:
- Team status summary
- Blockers identified and resolved
- Sprint progress metrics
- Coordination activities

**Deep-Dives You Might Create**:
- Sprint planning documents
- Retrospective summaries
- Risk management plans

---

### 📚 Product-Owner (`product-owner.md`)

**Focus**: Requirements, priorities, value

**Daily Must-Haves**:
- User stories worked on
- Requirements defined
- Priorities adjusted
- Stakeholder feedback

**Deep-Dives You Might Create**:
- Feature requirement documents
- Roadmap planning
- User research findings

---

### 🏗️ Architect (`architect.md`)

**Focus**: Technical design, decisions, architecture

**Daily Must-Haves**:
- Architecture work completed
- Technical decisions made
- Design artifacts created
- Technical reviews performed

**Deep-Dives You Might Create**:
- Architecture design documents
- Technical decision records (ADRs)
- System integration plans
- Performance strategies

---

### 💻 Developer (`developer.md`)

**Focus**: Implementation, code, technical execution

**Daily Must-Haves**:
- Features implemented
- Code written/reviewed
- Tests created
- Bugs fixed

**Deep-Dives You Might Create**:
- Implementation strategies
- Refactoring plans
- Performance optimization docs
- Code pattern documentation

---

### 🎨 Designer (`designer.md`)

**Focus**: UI/UX, visual design, accessibility

**Daily Must-Haves**:
- Design work completed
- Specs created/updated
- Accessibility checks
- Component designs

**Deep-Dives You Might Create**:
- Design system specifications
- Accessibility strategies
- UI pattern libraries
- User flow documentation

---

### 🧪 QA-Engineer (`qa-engineer.md`)

**Focus**: Testing, quality, validation

**Daily Must-Haves**:
- Tests executed
- Bugs found/filed
- Quality validations
- Test metrics

**Deep-Dives You Might Create**:
- Test strategies
- Bug investigation reports
- Quality improvement plans
- Testing frameworks

---

### 🎓 Domain-Expert (`domain-expert.md`)

**Focus**: Business rules, domain knowledge, compliance

**Daily Must-Haves**:
- Domain models reviewed
- Business rules validated
- Terminology defined
- Compliance checks

**Deep-Dives You Might Create**:
- Domain model documentation
- Business rules catalog
- Compliance requirements
- Industry standards guides

---

## 📊 Deep-Dive Document Guidelines

### When to Create a Deep-Dive

Create a deep-dive document when:
- ✅ Topic is complex and needs detailed explanation
- ✅ Multiple roles need to collaborate on understanding
- ✅ Decision needs thorough documentation
- ✅ Creating reference material for future use
- ✅ Investigation or spike work completed
- ✅ Establishing patterns or standards

Don't create a deep-dive for:
- ❌ Simple updates or quick notes (use role files)
- ❌ Routine daily activities
- ❌ Topics already covered in existing docs
- ❌ Work-in-progress without conclusions

### Deep-Dive Template Structure

```markdown
# Deep Dive: [Topic Name]

## 📋 Overview
**Date**: YYYY.MM.DD
**Lead**: [Role Name]
**Participants**: [Roles/People]
**Duration**: [Time]
**Status**: [Complete/In Progress/Draft]

## 🎯 Objective
[What are we trying to understand/solve/document?]

## [Analysis Sections]
[Your content organized by topic]

## 💻 Technical Specifications
[If applicable - code, configs, specs]

## 📊 Metrics/Measurements
[If applicable - before/after, benchmarks]

## 🚧 Risks & Mitigation
[If applicable - risks and how to handle]

## 📝 Action Items
[Next steps, owners, timelines]

## 🔗 Resources
[Links to docs, tools, references]

## 📅 Next Review
[When to revisit this topic]

**Document Status**: [Status]
**Last Updated**: [Date]
**Owner**: [Role]
```

### Linking Deep-Dives

**From Role Files**:
```markdown
See deep-dive: [Topic Name](./deep-dives/topic-name.md)
```

**From Standup**:
```markdown
**Deep-Dives Created Today**:
- [Accessibility Strategy](./deep-dives/accessibility-implementation-strategy.md)
- [8px Grid System](./deep-dives/8px-grid-spacing-system.md)
```

---

## 🔍 Finding Information

### By Date
```
docs/notes/2025/10/2025.10.22/
```
Navigate to specific date folder to see all activities

### By Role
Search across dates:
```bash
# Find all Designer notes
find docs/notes -name "designer.md"

# Find Designer notes in October
find docs/notes/2025/10 -name "designer.md"
```

### By Topic
Search in deep-dives:
```bash
# Find accessibility-related deep-dives
find docs/notes -path "*/deep-dives/*" -name "*accessibility*"

# Search content
grep -r "accessibility" docs/notes/*/*/deep-dives/
```

### By Standup Meeting
```bash
# Find all standups in October
find docs/notes/2025/10 -name "standup.md"
```

---

## 🤝 Collaboration Patterns

### Single-Role Work
**Scenario**: Developer implementing a feature

**Workflow**:
1. Update `developer.md` throughout day
2. Reference issues/tickets
3. Document technical decisions
4. No deep-dive needed (straightforward work)

---

### Multi-Role Collaboration
**Scenario**: Designer and Developer working on UI system

**Workflow**:
1. **Designer** creates deep-dive document
2. Both update their role files referencing the deep-dive
3. **Director** notes collaboration in standup
4. Deep-dive becomes source of truth

---

### Complex Problem Solving
**Scenario**: Performance issue requiring investigation

**Workflow**:
1. **QA-Engineer** identifies issue, notes in `qa-engineer.md`
2. **Architect** investigates, creates deep-dive document
3. **Developer** implements solution, references deep-dive
4. **QA-Engineer** validates, updates their file
5. **Director** tracks progress in standup

---

## 💡 Best Practices

### Do's ✅

- **Create folder at start of day**
- **Update role files as you work** (not just end of day)
- **Link between documents** (role files ↔ deep-dives ↔ standup)
- **Use clear, descriptive names** for deep-dives
- **Keep standup focused** (detailed stuff goes in role files)
- **Create deep-dives proactively** (when complexity emerges)
- **Reference issues/tickets** (connect to GitHub)
- **Include code examples** in technical docs
- **Set clear status** on all documents

### Don'ts ❌

- **Don't skip documenting** even "small" days
- **Don't duplicate content** (link instead)
- **Don't create deep-dives for simple topics** (use role files)
- **Don't forget to update standup** (it's the daily record)
- **Don't use vague names** ("notes.md", "stuff.md")
- **Don't leave documents without status**
- **Don't write novels** (be concise, scannable)
- **Don't forget cross-references** (help people navigate)

---

## 🗓️ Monthly/Yearly Organization

### Folder Hierarchy
```
docs/notes/
├── 2025/
│   ├── 10/                    # October 2025
│   │   ├── 2025.10.01/
│   │   ├── 2025.10.02/
│   │   ├── ...
│   │   └── 2025.10.31/
│   ├── 11/                    # November 2025
│   └── 12/                    # December 2025
└── 2026/
    ├── 01/
    └── ...
```

### Archive Strategy

**Keep Forever**:
- All daily folders (they're source of truth)
- All standup notes
- All deep-dives

**Optional Monthly Summaries**:
Create `docs/notes/2025/10/README.md` with:
- Month overview
- Major accomplishments
- Key decisions
- Links to important deep-dives

**Optional Yearly Summaries**:
Create `docs/notes/2025/README.md` with:
- Year in review
- Major milestones
- Team growth
- Links to pivotal documents

---

## 🚀 Getting Started

### For New Projects

1. **Create base structure**:
   ```bash
   mkdir -p docs/notes/$(date +%Y)/$(date +%m)/$(date +%Y.%m.%d)/deep-dives
   ```

2. **Copy this README** to `docs/notes/README.md`

3. **Create role file templates**

4. **Start your first standup**

### For Existing Projects

1. **Create folder structure** for today

2. **Migrate relevant notes** from existing `NOTES.md`

3. **Start using system** going forward

4. **Keep old system** as reference (don't delete)

---

## 🛠️ Automation Ideas

### Shell Script: Create Today's Folder
```bash
#!/bin/bash
# scripts/create-daily-folder.sh

TODAY=$(date +%Y.%m.%d)
YEAR=$(date +%Y)
MONTH=$(date +%m)
DAILY_PATH="docs/notes/$YEAR/$MONTH/$TODAY"

mkdir -p "$DAILY_PATH/deep-dives"

# Copy templates if desired
# cp docs/notes/templates/*.md "$DAILY_PATH/"

echo "Created: $DAILY_PATH"
```

### Git Alias: Commit Daily Notes
```bash
# Add to .gitconfig
[alias]
    note = !git add docs/notes && git commit -m "docs: update daily notes $(date +%Y.%m.%d)"
```

---

## 📈 Benefits of This System

### For Individuals
- 🎯 **Clear structure** - Know where to put what
- 📝 **Daily rhythm** - Build documentation habit
- 🔍 **Easy retrieval** - Find information by date
- 🧠 **Knowledge capture** - Don't lose insights

### For Teams
- 🤝 **Transparency** - See what everyone's working on
- 📊 **Tracking** - Clear history of progress
- 🔄 **Collaboration** - Shared deep-dives enable alignment
- 📚 **Onboarding** - New members can read history

### For Projects
- 📖 **Documentation** - Built-in knowledge base
- 🎓 **Learning** - Capture lessons as you go
- 🚀 **Velocity** - Reduce duplicate work
- 🏆 **Quality** - Better decisions with documented context

---

## 🆘 Troubleshooting

**Q: What if multiple people have the same role?**  
A: Use `[role]-[name].md` format (e.g., `developer-john.md`, `developer-jane.md`)

**Q: What if I miss a day?**  
A: No problem! Create the folder when you return, note in standup that it's a catch-up

**Q: Can I create folders for weekends?**  
A: Optional - only if work happened. Otherwise skip.

**Q: What about holidays?**  
A: Skip - no folder needed if no work done

**Q: Should every role have a file every day?**  
A: No - only create files for roles that did work that day

**Q: What if a deep-dive spans multiple days?**  
A: Keep it in the day it started, update status as you work. Reference from later days.

**Q: Can deep-dives reference other deep-dives?**  
A: Yes! Use relative paths: `[Other Topic](../2025.10.20/deep-dives/other-topic.md)`

---

## 📚 Examples

See `docs/notes/2025/10/2025.10.22/` for a complete example day including:
- ✅ Standup with all roles
- ✅ Role-specific files (Designer, Director, bpc)
- ✅ Deep-dive documents (Accessibility, 8px Grid)
- ✅ Proper linking and cross-references
- ✅ Clear status and next steps

---

## 🔄 System Evolution

This system will evolve! Update this README when:
- You discover better patterns
- You add new file types
- You create useful automation
- You find better ways to organize

**Version**: 1.0  
**Created**: 2025.10.22  
**Last Updated**: 2025.10.22  
**Owner**: Director + Team

---

**This documentation is part of the Role-Based Project Template system.**  
**See main project README and `/docs/roles/` for more context.**
