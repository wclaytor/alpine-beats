# Skills Inventory

This document provides a comprehensive overview of all skills available in the template project, organized by category and their relationship to the seven-role development methodology.

## Skills by Category

### Core Skills (Infrastructure)
Skills that support the creation and management of other skills.

| Skill | Description | Primary Roles |
|-------|-------------|---------------|
| **skill-creator** | Tools and guidance for creating new skills | All Roles |
| **template-skill** | A template for building custom skills | All Roles |

### Development & Planning
Skills that support project planning, requirements, and development workflow.

| Skill | Description | Primary Roles |
|-------|-------------|---------------|
| **user-story-generator** | Create well-structured user stories with acceptance criteria and success metrics | Product-Owner, Director |
| **sprint-planning** | Guide effective sprint planning sessions including goal setting, story selection, and capacity planning | Director, Product-Owner |
| **moscow-analysis** | MoSCoW prioritization for requirements, features, and tasks during planning sessions | Product-Owner, Director |

### Architecture & Documentation
Skills that support technical design, decision-making, and documentation.

| Skill | Description | Primary Roles |
|-------|-------------|---------------|
| **technical-decision-record** | Document architectural decisions with ADRs including context, rationale, and consequences | Architect, Developer |
| **api-documentation** | Create comprehensive, developer-friendly API documentation following OpenAPI/REST best practices | Developer, Architect |
| **alpine-js** | Guide for creating interactive web applications using Alpine.js, a lightweight JavaScript framework | Developer, Architect, Designer |
| **alpine-audio-master** | Guide for creating single-file PWA audio applications using Alpine.js and Web Audio API for sound synthesis | Developer, Architect, Designer |
| **pwa-master** | Guide for creating and maintaining Progressive Web Apps (PWAs) that are installable on Android and iOS, with Alpine.js integration | Developer, Architect, Designer |

### Quality & Review
Skills that support code quality, testing, and review processes.

| Skill | Description | Primary Roles |
|-------|-------------|---------------|
| **code-review-checklist** | Comprehensive checklists and guidelines for conducting thorough, constructive code reviews | QA-Engineer, Developer |
| **accessibility-audit** | Ensure WCAG 2.1 Level AA compliance and inclusive design for digital products | Designer, QA-Engineer |

### Design & Creativity
Skills that support visual design, creativity, and presentation.

| Skill | Description | Primary Roles |
|-------|-------------|---------------|
| **theme-master** | Comprehensive theme creation, documentation, and application toolkit combining professional theme styling with visual Markdown documentation using LaTeX + HTML techniques | Designer |
| **algorithmic-art** | Create algorithmic art using p5.js with seeded randomness and interactive parameter exploration | Designer, Developer |
| **theme-factory** (LEGACY) | Generate and manage theme systems with curated font and color palettes - replaced by theme-master | Designer |
| **markdown-theme-factory** (LEGACY) | Document themes with native Markdown rendering - replaced by theme-master | Designer, Developer |

## Skills by Role

This table shows which skills are most relevant to each of the seven roles in the development methodology.

### Director (Project Orchestrator)
- sprint-planning
- moscow-analysis
- user-story-generator
- skill-creator

### Product-Owner (Product Strategy Specialist)
- user-story-generator
- sprint-planning
- moscow-analysis
- skill-creator

### Architect (Technical Blueprint Specialist)
- technical-decision-record
- api-documentation
- alpine-js
- alpine-audio-master
- pwa-master
- skill-creator
- template-skill

### Developer (Application Development Specialist)
- alpine-js
- alpine-audio-master
- pwa-master
- api-documentation
- code-review-checklist
- technical-decision-record
- algorithmic-art
- skill-creator

### Designer (UI/UX Specialist)
- theme-master
- accessibility-audit
- alpine-js
- alpine-audio-master
- pwa-master
- algorithmic-art
- skill-creator

### QA-Engineer (Quality Assurance Specialist)
- code-review-checklist
- accessibility-audit
- user-story-generator (for reviewing acceptance criteria)
- skill-creator

### Domain-Expert (Subject Matter Specialist)
- technical-decision-record (for documenting domain decisions)
- user-story-generator (for reviewing domain accuracy in stories)
- skill-creator (for creating domain-specific skills like business rules catalogs, compliance checklists, domain glossaries)

## Skills by Use Case

### Starting a New Project
1. **sprint-planning** - Plan your first sprint
2. **user-story-generator** - Create initial user stories
3. **moscow-analysis** - Prioritize features
4. **technical-decision-record** - Document key architectural decisions
5. **theme-master** - Establish visual design system and documentation
6. **pwa-master** - Set up Progressive Web App foundation (if building installable app)

### Feature Development Workflow
1. **user-story-generator** - Define the feature requirements
2. **moscow-analysis** - Prioritize within the feature
3. **technical-decision-record** - Document technical approach
4. **api-documentation** - Document any new APIs
5. **code-review-checklist** - Review the implementation
6. **accessibility-audit** - Ensure inclusive design

### Quality & Compliance
1. **code-review-checklist** - Conduct thorough code reviews
2. **accessibility-audit** - Ensure WCAG 2.1 AA compliance
3. **api-documentation** - Maintain accurate documentation
4. **technical-decision-record** - Document quality standards

### Design & User Experience
1. **theme-master** - Create, document, and apply professional themes with visual examples
2. **accessibility-audit** - Ensure inclusive design
3. **algorithmic-art** - Create generative art and visualizations
4. **user-story-generator** - Ensure user needs are captured
5. **pwa-master** - Design installable app experience with proper icons and splash screens

### Architecture & Technical Design
1. **technical-decision-record** - Document architectural decisions
2. **api-documentation** - Design and document APIs
3. **code-review-checklist** - Review architectural patterns
4. **sprint-planning** - Plan technical work
5. **pwa-master** - Design PWA architecture with offline-first patterns and service workers
6. **alpine-js** - Implement reactive UI components for PWAs

### Project Management & Planning
1. **sprint-planning** - Facilitate planning sessions
2. **moscow-analysis** - Prioritize requirements
3. **user-story-generator** - Create actionable stories
4. **code-review-checklist** - Ensure quality standards

## Skill Descriptions

### skill-creator
**Purpose:** Guide for creating effective skills  
**When to Use:** When users want to create a new skill or update an existing skill that extends Claude's capabilities with specialized knowledge, workflows, or tool integrations.  
**Key Features:**
- Step-by-step skill creation process
- Best practices for skill design
- Templates and examples
- Scripts for initialization and packaging

### template-skill
**Purpose:** Template for building custom skills  
**When to Use:** As a starting point when creating a new skill from scratch.  
**Key Features:**
- Basic SKILL.md structure
- Example front-matter metadata
- Placeholder for instructions

### user-story-generator
**Purpose:** Create well-structured user stories  
**When to Use:** Defining requirements, creating backlog items, or translating feature requests into actionable user stories.  
**Key Features:**
- User story templates (standard, bug fix, technical debt, spike)
- Acceptance criteria guidelines
- Story sizing recommendations
- Integration with team workflows

### sprint-planning
**Purpose:** Guide effective sprint planning sessions  
**When to Use:** Planning sprints, facilitating planning meetings, or helping teams establish sprint planning practices.  
**Key Features:**
- Complete sprint planning process
- Capacity and velocity calculation
- Sprint goal definition
- Story selection and breakdown
- Sprint planning agenda template

### moscow-analysis
**Purpose:** MoSCoW prioritization analysis  
**When to Use:** Teams need to categorize and prioritize items into Must have, Should have, Could have, and Won't have categories.  
**Key Features:**
- MoSCoW methodology explanation
- Facilitation techniques
- Output templates
- Integration with planning processes

### technical-decision-record
**Purpose:** Document architectural decisions with ADRs  
**When to Use:** Making significant architectural decisions, selecting technologies, or documenting design decisions that impact the system.  
**Key Features:**
- ADR templates (standard and detailed)
- Status lifecycle management
- Example ADRs
- Best practices for writing and maintaining ADRs

### api-documentation
**Purpose:** Create comprehensive API documentation  
**When to Use:** Documenting APIs, creating API specifications, or ensuring API documentation is complete and usable.  
**Key Features:**
- REST API documentation structure
- OpenAPI specification examples
- Endpoint documentation templates
- Best practices for developer experience

### code-review-checklist
**Purpose:** Comprehensive code review guidelines  
**When to Use:** Reviewing pull requests, providing code feedback, or establishing code review standards.  
**Key Features:**
- Comprehensive review checklist
- Feedback best practices
- Language-specific considerations
- Review process guidelines

### accessibility-audit
**Purpose:** Ensure WCAG 2.1 Level AA compliance  
**When to Use:** Conducting accessibility reviews, ensuring inclusive design, or validating WCAG compliance.  
**Key Features:**
- WCAG 2.1 comprehensive checklist
- Testing methods (automated and manual)
- ARIA best practices
- Accessibility audit report template

### markdown-theme-factory (LEGACY)
**Purpose:** Document themes with native Markdown rendering  
**Status:** LEGACY - Replaced by theme-master  
**When to Use:** Use **theme-master** instead for comprehensive theme creation and documentation.  
**Key Features:**
- LaTeX + HTML rendering for pixel-perfect color swatches
- Full visual examples with actual theme colors  
- WCAG 2.1 AA accessibility validation and documentation
- 10 pre-built example themes
- Comprehensive color rendering technical guide

**Note:** This skill has been superseded by **theme-master** which combines theme creation, application, and documentation capabilities.

### theme-master
**Purpose:** Comprehensive theme creation, documentation, and application toolkit  
**When to Use:** Creating themes for any artifact (presentations, documents, design systems), documenting themes visually in GitHub Markdown, or applying professional themes systematically.  
**Key Features:**
- **Theme Application**: Apply 10 pre-built professional themes or create custom themes for presentations, documents, dashboards, etc.
- **Visual Documentation**: Create stunning theme documentation in GitHub Markdown using LaTeX + HTML techniques
- **Accessibility**: Built-in WCAG 2.1 AA compliance validation and contrast ratio testing
- **10 Pre-Built Themes**: Industry-specific color palettes and typography systems
- **Custom Generation**: Create themes on-the-fly based on requirements
- **Code-Ready Exports**: CSS variables, SCSS, implementation examples
- **Designer Role Integration**: Specifically designed for the Designer role with complete handoff documentation
- **Color Theory**: Support for analogous, complementary, and triadic color schemes
- **Multi-Purpose**: Works for presentations, websites, documents, dashboards, design systems, and more

**Why Use This:** Theme Master combines the best of theme creation and documentation in one skill, replacing both theme-factory and markdown-theme-factory with a unified, comprehensive approach.

### theme-factory (LEGACY)
**Purpose:** Generate and manage theme systems  
**Status:** LEGACY - Replaced by theme-master  
**When to Use:** Use **theme-master** instead for comprehensive theme capabilities.  
**Key Features:**
- 10 pre-set professional themes
- Color palette and font pairings
- Custom theme generation

**Note:** This skill has been superseded by **theme-master** which provides all theme-factory capabilities plus visual documentation and enhanced features.

### algorithmic-art
**Purpose:** Create algorithmic art using p5.js  
**When to Use:** Users request creating art using code, generative art, algorithmic art, flow fields, or particle systems.  
**Key Features:**
- Algorithmic philosophy creation
- p5.js implementation guidance
- Interactive artifact creation
- Seeded randomness patterns

### alpine-js
**Purpose:** Guide for creating interactive web applications using Alpine.js  
**When to Use:** Building lightweight, reactive interfaces, adding interactivity to static pages, or creating component-based UIs without heavy JavaScript frameworks.  
**Key Features:**
- Comprehensive directive reference (x-data, x-bind, x-on, x-model, etc.)
- Component patterns and best practices
- Common UI patterns (modals, dropdowns, tabs, accordions, forms)
- Performance optimization techniques
- Accessibility guidelines for interactive components
- Integration with backend frameworks (Laravel, Django, Rails)
- Testing strategies for Alpine components

### alpine-audio-master
**Purpose:** Guide for creating single-file PWA audio applications using Alpine.js and Web Audio API  
**When to Use:** Building audio synthesis applications, music tools, sound generators, or any PWA that requires professional-grade audio capabilities with offline support, reactive UI, and zero build process.  
**Key Features:**
- Web Audio API integration with oscillators, effects, and audio routing
- Alpine.js reactive components for audio control
- Single-file PWA architecture with inline service worker and manifest
- Touch and keyboard input handling for cross-device support
- Ready-to-use template (`alpine-audio-pwa-template.html`)
- Comprehensive reference guide (`Alpine-Audio-PWA.md`)
- Examples: synthesizers, drum machines, effects processors, sound generators
- Performance optimization and audio quality best practices
- Deployment guidance for GitHub Pages and static hosting

### pwa-master
**Purpose:** Guide for creating and maintaining Progressive Web Apps (PWAs)  
**When to Use:** Building installable web applications with offline capability, native app-like experiences, or cross-platform apps that work on Android and iOS.  
**Key Features:**
- Both single-file (preferred) and separate files PWA approaches
- Web app manifest specifications and configuration
- Service worker patterns (cache strategies, background sync, push notifications)
- iOS-specific considerations and meta tags
- Alpine.js integration examples (primary use case)
- Icon generation and management
- Offline-first data management patterns
- Installation prompt handling
- Testing and debugging guidance

## Creating Your Own Skills

To create a new skill for your specific needs:

1. **Use the skill-creator**: Consult the skill-creator skill for guidance
2. **Start with template-skill**: Copy the template as a starting point
3. **Define the purpose**: Clearly articulate what the skill does and when to use it
4. **Follow the structure**: Use the SKILL.md format with front-matter metadata
5. **Add examples**: Include concrete examples of skill usage
6. **Test thoroughly**: Validate the skill works as intended
7. **Document clearly**: Make instructions clear and actionable

## Updating This Document

When adding new skills:
1. Add entry to appropriate category table
2. Add to "Skills by Role" section
3. Add to relevant "Skills by Use Case" sections
4. Add detailed description in "Skill Descriptions" section
5. Update the main README.md if needed

## Contributing

When contributing new skills to this template:
- Follow the established skill structure
- Provide comprehensive documentation
- Include practical examples
- Align with the seven-role methodology
- Consider which roles will use the skill
- Test the skill thoroughly before submitting
