# Role Collaboration Guide

## 🎯 Overview

This document defines how the seven core roles in our development methodology collaborate to create exceptional applications. The Director orchestrates collaboration across all roles, ensuring effective coordination and successful delivery. Each role has specific responsibilities, clear interfaces, and defined collaboration patterns that ensure quality, efficiency, and user satisfaction.

## 🏗️ Role System Architecture

### **Complete Role Ecosystem**
```
              Director (Orchestration & Coordination)
                            ↓
        ┌───────────────────┼───────────────────┐
        ↓                   ↓                   ↓
   Product-Owner       Domain-Expert       Architect
    (Strategy)       (Domain Knowledge)   (Blueprint)
        ↓                   ↓                   ↓
        └───────────────────┼───────────────────┘
                            ↓
                    ┌───────┴───────┐
                    ↓               ↓
                Designer        Developer
              (Experience)   (Implementation)
                    ↓               ↓
                    └───────┬───────┘
                            ↓
                      QA-Engineer
                      (Validation)
```

### **Role Hierarchy and Dependencies**
```
Orchestration Level:  Director (Facilitates & Coordinates)
                         ↓
Strategic Level:    Product-Owner ←→ Domain-Expert
                         ↓               ↓
Specification Level: Architect ←→ Designer  
                         ↓           ↓
Implementation Level: Developer (guided by Domain-Expert)
                         ↓
Validation Level:   QA-Engineer (validates domain rules with Domain-Expert)
```

## 🔄 Core Collaboration Patterns

### **Pattern 1: Project Initiation Flow**
```
0. Director → Coordinates team formation, establishes collaboration framework
1. Product-Owner → Defines vision, requirements, and success criteria
2. Domain-Expert → Validates domain accuracy, defines business rules and terminology
3. Architect → Creates technical blueprint and system design
4. Designer → Develops UI/UX specifications aligned with architecture
5. Developer → Implements code following specs and domain rules
6. QA-Engineer → Validates against all role requirements including domain rules
7. Director → Facilitates reviews and ensures alignment
```

### **Pattern 2: Feature Development Cycle**
```
Director: "Facilitates sprint planning and coordinates team"
        ↓
Product-Owner: "We need offline recipe filtering"
        ↓
Domain-Expert: "Validates recipe taxonomy, dietary restrictions, defines filter rules"
        ↓
Architect: "Single-page reactive filter with localStorage, domain model design"
        ↓
Designer: "Mobile-first filter UI with domain-appropriate labels and terminology"
        ↓
Developer: "Implements reactive filtering with business rules from Domain-Expert"
        ↓
QA-Engineer: "Tests offline functionality, validates business rules with Domain-Expert"
        ↓
Product-Owner: "Validates user value and business impact"
        ↓
Director: "Coordinates review, removes blockers, tracks progress"
```

### **Pattern 3: Quality Feedback Loop**
```
QA-Engineer finds issue → Developer fixes → Domain-Expert validates business logic
                                              ↓
                     Architect reviews design impact if needed
                                              ↓
                     Designer adjusts UX ← QA-Engineer retests
                                              ↓
                                    Product-Owner approves
                                              ↓
                              Director tracks resolution and updates status
```

### **Pattern 4: Skills-Enhanced Workflow**
Skills augment role-based collaboration by providing structured guidance, templates, and best practices:

```
Director: "Uses sprint-planning skill to facilitate planning session"
        ↓
Product-Owner: "Uses user-story-generator skill to create well-formed stories"
        ↓
Architect: "Uses technical-decision-record skill to document design choices"
        ↓
Designer: "Uses accessibility-audit and theme-factory skills for design"
        ↓
Developer: "Uses api-documentation skill for API creation"
        ↓
QA-Engineer: "Uses code-review-checklist and accessibility-audit skills"
        ↓
Product-Owner: "Validates against acceptance criteria from user stories"
        ↓
Director: "Uses retrospectives to identify new skills to create"
```

**Key Points About Skills:**
- **Skills are tools, not replacements** - They augment role expertise, not replace it
- **Example skills are starting points** - Projects should create custom skills for their domain
- **Skills capture institutional knowledge** - They preserve team practices and standards
- **Skills enable consistency** - They standardize approaches across similar tasks
- **Create skills for repeated work** - If you do it twice, consider making it a skill

## 🔧 Integrating Skills into Collaboration

### When to Use Skills in Collaboration

**During Planning:**
- **sprint-planning**: Facilitate planning sessions consistently
- **moscow-analysis**: Guide prioritization discussions
- **user-story-generator**: Ensure stories follow team standards

**During Design & Architecture:**
- **technical-decision-record**: Document decisions systematically
- **api-documentation**: Create consistent API documentation
- **theme-factory**: Establish visual design systems

**During Implementation:**
- **code-review-checklist**: Standardize review processes
- **accessibility-audit**: Ensure WCAG compliance
- **api-documentation**: Document as you build

**During Quality Assurance:**
- **code-review-checklist**: Thorough, consistent reviews
- **accessibility-audit**: Comprehensive accessibility validation
- Project-specific testing skills (create your own!)

### Creating Project-Specific Skills

As teams collaborate, they develop unique patterns and practices. Capture these as skills:

1. **Identify repeatable processes**: What does your team do repeatedly?
2. **Document the pattern**: Create a skill with step-by-step guidance
3. **Include templates**: Add checklists, templates, or reference materials
4. **Share with team**: Make skills accessible in the `/skills/` directory
5. **Iterate and improve**: Update skills based on team feedback

**Example Custom Skills to Consider:**
- Domain-specific validation checklists
- Project-specific deployment procedures
- Custom API design patterns
- Team code review standards
- Industry compliance checklists
- Performance optimization workflows
- Security review procedures

### Skills vs. Role Documentation

**Role Documentation** (`/docs/roles/`):
- Defines responsibilities and collaboration patterns
- Describes **what** each role does and **how** roles work together
- Applies broadly across all projects using this template

**Skills** (`/skills/`):
- Provides actionable, step-by-step guidance for specific tasks
- Captures **how** to accomplish specific activities
- Should be customized for your project's unique needs
- Examples included are starting points, not final solutions

**Use both together**: Role documentation provides the framework; skills provide the tools.

## 🎯 Role-Specific Collaboration Interfaces

### **Domain-Expert Collaboration**

#### **→ To Product-Owner**
- **Input**: Domain model validation, business rule definitions, terminology corrections
- **Format**: Domain glossary, business rules catalog, compliance requirements
- **Example**: "User stories should use 'patient encounter' not 'visit' per HIPAA terminology"

#### **→ To Architect**
- **Input**: Domain model specifications, business rule logic, data validation requirements
- **Format**: Domain entity definitions, business rules documentation, compliance constraints
- **Example**: "Order aggregate must enforce inventory reservation within same transaction boundary"

#### **→ To Designer**
- **Input**: Domain terminology, workflow accuracy guidance, compliance UI requirements
- **Format**: Terminology guide, workflow validation, regulatory UI constraints
- **Example**: "Consent forms must include specific language per GDPR Article 7 requirements"

#### **→ To Developer**
- **Input**: Business logic clarifications, validation rules, domain-specific implementation guidance
- **Format**: Business rule specifications, edge case documentation, domain logic examples
- **Example**: "Tax calculation must handle multi-state nexus rules per Wayfair decision"

#### **→ To QA-Engineer**
- **Input**: Domain-specific test scenarios, business rule validation criteria, compliance checklists
- **Format**: Domain test cases, regulatory validation requirements, business logic tests
- **Example**: "Test that refund calculations follow partial refund rules and applicable tax adjustments"

#### **← From All Roles**
- **Output**: Domain questions, terminology clarifications, business rule validation requests
- **Format**: Questions in issues/PRs, requirements reviews, implementation feedback
- **Frequency**: Ongoing throughout development cycle, especially during requirements and implementation phases

### **Product-Owner Collaboration**

#### **→ To Architect**
- **Input**: Business requirements, user scenarios, success metrics
- **Format**: `Requirements.md`, user stories, acceptance criteria
- **Example**: "Users need to find vegan camping recipes quickly on mobile devices with spotty internet"

#### **→ To Designer**
- **Input**: User personas, brand guidelines, accessibility requirements
- **Format**: Design briefs, user research, competitive analysis
- **Example**: "Target users are outdoor enthusiasts aged 25-45 who prioritize sustainability"

#### **← From QA-Engineer**
- **Output**: Quality reports, user acceptance test results, performance metrics
- **Format**: Test reports, user feedback analysis, KPI dashboards
- **Example**: "Recipe search performs under 100ms with 95% user satisfaction"

### **Architect Collaboration**

#### **→ To Developer**
- **Input**: `Architecture.md`, technical specifications, performance requirements
- **Format**: System design documents, API specs, data models
- **Example**: "Use Alpine.js reactive filtering with localStorage persistence, optimize for mobile"

#### **→ To Designer**
- **Input**: Technical constraints, performance guidelines, platform limitations
- **Format**: Technical constraints document, feasibility analysis
- **Example**: "Single HTML file constraint means no external image assets, use Bootstrap Icons"

#### **← From QA-Engineer**
- **Output**: Architecture validation reports, performance analysis, scalability feedback
- **Format**: Technical quality reports, performance benchmarks
- **Example**: "Current architecture handles 1000+ recipes with <200ms filter response"

### **Designer Collaboration**

#### **→ To Developer**
- **Input**: Design specifications, component library, responsive breakpoints
- **Format**: `Design-System.md`, Figma files, style guides
- **Example**: "Mobile-first card layout with 16px padding, Tailwind responsive classes"

#### **← From QA-Engineer**
- **Output**: Usability test results, accessibility audit findings, design validation
- **Format**: UX test reports, accessibility compliance reports
- **Example**: "Navigation passes WCAG 2.1 AA standards, 98% mobile usability score"

#### **↔ With Architect**
- **Collaboration**: Feasibility discussions, technical constraint resolution
- **Format**: Joint design sessions, constraint documentation
- **Example**: "Offline-first design patterns that work with Alpine.js reactivity"

### **Developer Collaboration**

#### **← From Architect**
- **Input**: Technical blueprints, system requirements, performance targets
- **Format**: `Architecture.md`, technical specifications
- **Example**: "Implement reactive search with debounced input, localStorage caching"

#### **← From Designer**
- **Input**: UI specifications, component designs, interaction patterns
- **Format**: Design system documentation, component specifications
- **Example**: "Search input with Bootstrap search icon, Tailwind focus states"

#### **→ To QA-Engineer**
- **Output**: Implemented features, code documentation, test scenarios
- **Format**: Code commits, feature documentation, implementation notes
- **Example**: "Recipe filter implemented with x-model binding and computed properties"

### **QA-Engineer Collaboration**

#### **← From All Roles**
- **Architect**: Technical requirements and performance standards
- **Designer**: UX requirements and accessibility standards  
- **Developer**: Implementation details and test scenarios
- **Product-Owner**: Business requirements and acceptance criteria

#### **→ To All Roles**
- **Quality Reports**: Validation results, issue identification, improvement recommendations
- **Format**: Test reports, bug reports, quality metrics dashboards
- **Frequency**: Continuous integration, sprint reviews, release validation

### **Director Collaboration**

#### **→ To All Roles**
- **Coordination**: Sprint planning, daily standups, retrospectives, and cross-role alignment
- **Status Updates**: Project progress, milestone tracking, blocker resolution
- **Facilitation**: Decision-making sessions, conflict resolution, priority alignment
- **Format**: Meeting agendas, status reports, decision logs, risk registers
- **Example**: "Coordinating architecture review with Architect, Designer, and Developer to align on performance optimization approach"

#### **← From All Roles**
- **Product-Owner**: Vision, priorities, requirements, stakeholder feedback
- **Architect**: Technical constraints, feasibility assessments, risk analysis
- **Designer**: Design complexity, implementation considerations, usability insights
- **Developer**: Progress updates, effort estimates, technical challenges, capacity
- **QA-Engineer**: Quality metrics, test results, release readiness, risk reports

#### **Key Orchestration Activities**
- **Sprint Planning**: Facilitate consensus on sprint goals and team commitments
- **Blocker Resolution**: Track and coordinate removal of impediments across roles
- **Risk Management**: Identify project risks early and coordinate mitigation strategies
- **Stakeholder Communication**: Translate technical progress to business-friendly updates
- **Process Improvement**: Facilitate retrospectives and implement continuous improvements

## 🚀 Collaboration Workflows

### **Workflow 1: New Feature Development**

```
Day 0: Director facilitates sprint planning (uses sprint-planning skill)
       Product-Owner prioritizes features (uses moscow-analysis skill)
Day 1: Product-Owner defines user story (uses user-story-generator skill)
Day 1: Domain-Expert validates domain accuracy, defines business rules (uses business-rule-catalog skill)
Day 2: Architect creates technical approach incorporating domain model (uses technical-decision-record skill)
Day 2: Designer creates UI specifications with domain terminology (references accessibility-audit skill)
Day 3-5: Developer implements feature following domain rules (follows ADRs, domain specs)
       Domain-Expert provides ongoing clarification on business logic
       Director tracks progress, removes blockers
Day 6: QA-Engineer validates and tests including domain rules (uses code-review-checklist, domain-test-scenarios skills)
       Domain-Expert validates business logic correctness
Day 7: Product-Owner accepts or requests changes (validates against acceptance criteria)
Day 7: Director coordinates review and updates project status
       Team reflects on repeatable patterns to capture as new skills
```

### **Workflow 2: Bug Resolution**

```
QA-Engineer identifies issue → Creates detailed bug report
        ↓
Director triages with team → Coordinates resolution approach
        ↓
Domain-Expert reviews → Validates if business logic issue
        ↓
Architect reviews → Determines if architectural change needed
        ↓
Designer reviews → Determines if UX change needed
        ↓
Developer implements fix → Updates implementation
        ↓
Domain-Expert validates → Confirms business rules are correct
        ↓
QA-Engineer retests → Validates resolution
        ↓
Product-Owner approves → Issue closed
        ↓
Director updates tracking and communicates status
```

### **Workflow 3: Performance Optimization**

```
QA-Engineer identifies performance issue
        ↓
Director coordinates optimization planning session (uses sprint-planning skill)
        ↓
Domain-Expert assesses if performance impacts business rules or compliance requirements
        ↓
Architect analyzes system bottlenecks (documents findings with technical-decision-record skill)
        ↓
Developer optimizes implementation while maintaining business logic integrity
        ↓
Designer adjusts UX if needed (loading states, progressive disclosure)
        ↓
Domain-Expert validates optimizations don't compromise business rules
        ↓
QA-Engineer validates improvements (uses custom performance testing skill if available)
        ↓
Product-Owner confirms user impact improvement
        ↓
Director documents learnings and updates metrics
Team considers creating performance-optimization skill for future use
```

### **Workflow 4: Compliance & Regulatory Implementation**

```
Product-Owner identifies new compliance requirement (e.g., GDPR, HIPAA)
        ↓
Director coordinates compliance planning session with all roles
        ↓
Domain-Expert analyzes compliance requirements and defines specific rules (creates compliance-requirements skill)
        ↓
Product-Owner prioritizes compliance work with Domain-Expert input (uses moscow-analysis)
        ↓
Domain-Expert documents business rules and validation requirements (uses business-rule-catalog skill)
        ↓
Architect designs technical implementation for compliance (uses technical-decision-record for audit trails, encryption)
        ↓
Designer creates compliant UI elements (consent forms, privacy notices) with Domain-Expert validation
        ↓
Developer implements compliance features following domain rules and architecture
        ↓
Domain-Expert reviews implementation for regulatory accuracy
        ↓
QA-Engineer validates compliance with domain-specific test scenarios (uses compliance-checklist skill)
        ↓
Domain-Expert performs final compliance validation and signs off
        ↓
Product-Owner confirms business impact and regulatory readiness
        ↓
Director ensures compliance documentation is complete and communicates status
```

## 📋 Communication Standards

### **Documentation Requirements**
- **All Decisions**: Must be documented in role-specific markdown files
- **Cross-Role Decisions**: Documented by primary decision maker with cc: to affected roles
- **Change Requests**: Must include impact analysis for all affected roles

### **Meeting Cadence**
- **Daily Standups**: All roles coordinate progress (facilitated by Director, 15 min)
- **Weekly Design Reviews**: Architect ↔ Designer ↔ Developer (coordinated by Director)
- **Sprint Planning**: All roles participate in planning and estimation (facilitated by Director)
- **Sprint Reviews**: Demo and stakeholder feedback (coordinated by Director)
- **Retrospectives**: All roles contribute to process improvement (facilitated by Director)

### **Escalation Path**
```
Technical Issues: Developer → Architect → Director → Product-Owner
UX Issues: Designer → Director → Product-Owner
Quality Issues: QA-Engineer → Architect → Director → Product-Owner
Scope Issues: Any Role → Director → Product-Owner
Resource/Timeline Issues: Any Role → Director (coordinates resolution)
Cross-Role Conflicts: Affected Roles → Director (facilitates resolution)
```

## 🎯 Success Metrics

### **Collaboration Effectiveness Indicators**
- **Handoff Quality**: Requirements clear enough for next role to execute without clarification
- **Rework Frequency**: Less than 10% of deliverables require major rework
- **Cross-Role Understanding**: Each role understands constraints and capabilities of others
- **Decision Speed**: Technical and design decisions made within 24 hours
- **Blocker Resolution**: Director resolves blockers within 1 day
- **Meeting Effectiveness**: Meetings have clear outcomes and action items

### **Project Success Indicators**
- **Quality**: Zero critical bugs, 95%+ user satisfaction
- **Performance**: All Alpine.js apps load under 2 seconds, work offline
- **Usability**: 90%+ task completion rate, WCAG 2.1 AA compliance
- **Business Value**: Clear ROI, user adoption targets met
- **Delivery Predictability**: Sprint commitments consistently met (>80% completion rate)

## 🔧 Tools and Templates

### **Collaboration Tools**
- **GitHub Issues**: Cross-role discussion and decision tracking
- **Markdown Documentation**: All specifications and decisions
- **Code Reviews**: Multi-role participation in technical decisions
- **Design System**: Shared component library and style guide
- **Skills**: Reusable workflows, templates, and guidance for common tasks

### **Standard Templates**
- **Feature Request**: Product-Owner → All Roles communication template
- **Technical Specification**: Architect → Developer handoff template
- **Design Specification**: Designer → Developer handoff template  
- **Quality Report**: QA-Engineer → All Roles feedback template
- **Bug Report**: QA-Engineer → Developer issue template

**Note**: Many of these templates are available as skills in the `/skills/` directory. Teams should adapt existing skills or create custom skills for their specific template needs.

## 📚 Best Practices

### **Communication Excellence**
1. **Assume Positive Intent**: All feedback focused on improving the product
2. **Be Specific**: Include examples, screenshots, and clear acceptance criteria
3. **Document Decisions**: All important decisions captured in markdown files
4. **Regular Check-ins**: Proactive communication prevents surprises

### **Quality Focus**
1. **Definition of Done**: Must satisfy all role requirements before completion
2. **Continuous Feedback**: Issues identified and addressed immediately
3. **User-Centered**: All decisions evaluated against user value and experience
4. **Performance Priority**: Alpine.js optimization is everyone's responsibility

### **Continuous Improvement**
1. **Retrospectives**: Regular process evaluation and improvement
2. **Knowledge Sharing**: Cross-role learning and skill development
3. **Tool Evolution**: Regularly evaluate and improve collaboration tools
4. **Pattern Documentation**: Successful patterns documented for reuse
5. **Skills Creation**: Capture repeatable processes as skills for team consistency
6. **Skills Refinement**: Continuously update skills based on team feedback and learning

---

This collaboration guide ensures our seven-role system—with the Director orchestrating collaboration—creates exceptional applications through clear communication, defined responsibilities, effective coordination, continuous quality focus, and reusable skills that capture team knowledge and best practices.
