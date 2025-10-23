# Skills Directory

## What are Skills?

In this project, a *Skill* is a modular, self-contained package that captures a specific capability, workflow or expertise—so that our AI agent (or system) can invoke that capability when needed, rather than rely purely on ad-hoc prompts or code fragments.

Each Skill is represented as a folder containing:
- A metadata file (typically `SKILL.md`) where the Skill’s name, description and instructions live.
- Optionally, supporting resources (scripts, data files, templates, reference docs) used by the Skill.

The benefit of using Skills is that you can:
- **Encapsulate domain knowledge** (e.g., formatting, business rules, brand guidelines, data-analysis workflow).
- **Reuse** that encapsulated knowledge across different tasks, contexts or projects.
- **Maintain** Skills separately (versioning, testing, updating) rather than scattering logic in prompts or code.
- **Compose** multiple Skills when complex workflows span different domains.

## How to Use the Skills Directory

### 1. Organising Skills  
Place each Skill in its own top-level folder under this directory. E.g.:

```
skills/ ├─ my-skill-one/ │    SKILL.md │    helper_script.py ├─ my-other-skill/ │    SKILL.md │    template.docx │    README.md └─ …
```

### 2. The `SKILL.md` File  
Each folder must contain a `SKILL.md` file which begins with front-matter metadata and then the instructions, examples and guidelines that the system (agent) should follow when that Skill is triggered. For example:

```markdown
---
name: my-skill-one
description: Performs X and Y tasks according to our team’s workflow
---

# My Skill One

## Purpose
Describe what this skill does, when it should be used.

## Instructions
Step-by-step instructions (or guidelines) for how the agent should carry out the task.

## Examples
- Example input → expected output
- Example usage scenario

## Notes / Guidelines
Special rules, exceptions, edge-cases to watch out for.
```

3. Triggering Skills

When the agent receives a user request (or system event), it should scan the available Skills and determine if one (or more) is relevant. Upon selection, the agent loads the relevant Skill’s instructions and resources and executes accordingly.

4. Versioning & Maintenance

Because Skills are modular:

Track changes to each Skill folder (you may treat each as its own “mini-module” in version control).

Keep example usage and test cases updated within each Skill.

If a Skill becomes large/complex, you can split its supporting files (scripts, templates, reference documentation) into sub-folders and have the SKILL.md link to them.


Safety & Governance

Since Skills may contain scripts or logic that the agent executes:

Only install or enable Skills that are well reviewed and tested.

Document what each Skill does, what dependencies it has, and any external resources it touches.

Periodically audit Skills to ensure they remain aligned with your team’s policies, workflows and data-security practices.


Where Your Skills Live

In this repository, you’ll find the skills/ directory. Inside it, each sub-directory is one Skill you or your team has created or imported.
Below is a list of the Skills currently in this project (you will fill this out):

Skill Name	Folder Name	Description

Example Skill One	example-skill-one	A demonstration Skill for X
Example Skill Two	example-skill-two	Handles Y workflow for our team
…		


(Add additional rows as you add more Skills.)

Getting Started

1. Clone or pull this repository to your local machine.


2. Navigate to the skills/ directory and inspect existing Skills.


3. To add a new Skill:

Create a new folder under skills/.

Add a SKILL.md file with front-matter and instructions.

Add any additional supporting files (scripts, templates, reference docs).

(Optional) Update this README table with the new Skill.



4. Incorporate the new Skill into your agent/workflow so that it can trigger when appropriate.



Contributing to Skills

Use meaningful names for Skills (lower-case, hyphens rather than spaces).

Write clear description metadata—this helps the agent decide when the Skill is relevant.

Provide well-defined examples in each Skill so behavior is predictable.

When modifying a Skill, update example scenarios and tests accordingly.

Add a version note or changelog inside the Skill folder if major changes are made.


Licence / Usage

(Add your project’s licence / usage terms here as appropriate.)


