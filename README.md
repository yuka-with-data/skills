# Skills
This repository contains reusable AI agent Skills designed for integration within my broader project ecosystem.

These Skills are actively used as operational capability layers alongside tools, MCP servers, APIs, and application backends across my AI and agent-based projects.

The goal of this repository is to:
- demonstrate practical AI agent Skill structures and workflows
- provide reusable Skill templates and reference implementations
- standardize reusable Skill patterns across projects
- showcase portable Skills compatible with modern agent runtimes
- serve as a reference resource for future Skill development

Some production Skills may be implemented directly inside their respective projects or MCP ecosystems, while this repository primarily focuses on:
- reusable examples
- templates
- demonstrations
- shared Skill patterns

## Skill Specification
The Skill structure and conventions used in this repository are inspired by and generally follow the Skill specification and ecosystem guidance provided by:
- [Agent Skills](https://agentskills.io/)

The repository is designed to remain lightweight, modular, and adaptable across different agent ecosystem such as:
- Claude
- Codex
- MCP-based systems
- other open-source, Skill-compatible frameworks

## What a Skill is
Skills are modular compatibility packages that help AI agent perform specific tasks more reliably and consistently. 

A Skill provides:
- structured instructions
- operational guidance
- activation context
- optional helper references or scripts
- reusable workflows for specialized domains

A Skill is ***NOT***:
- a full application
- a standalone backend service
- the main execusion engine of an AI Agent project

Skills are designed to improve how AI Agents:
- understand tasks
- select tools
- follow repeatable execution patterns
- produce more predictable outcomes

Unlike core application logic or backend systems, Skills act as a lightweight orchestration and guidance layer for agents. 

## Skill structure
Each Skill lives in its own directory and contains a `SKILL.md` file.

```bash
skills/
├── skill-name/
│   ├── SKILL.md                # Required
│   ├── references/             # Optional: documentation
│   │   ├── api_schema.md
│   │   └── domain_notes.md
│   ├── scripts/                # Optional: executable code
│   │    └── helper_script.py
│   ├── assets/                 # Optional: templates, resources
└── ...                         # Any additional files/directories
```

## Core Components
### `SKILL.md`
The main and **required** instruction file for the SKILL.

Typically includes:
- metadata
- activation guidance
- execution workflow
- tool usage instructions
- response formatting rules
- examples

### `scripts/`
**Optional** lightweight helper scripts used by the Skill.

Examples:
- utility script
- preprocessing helpers
- formatting tools

Core business logit and large application system should remain outside the Skill directory.

### `references/`
**Optional** supporting materials used by the Skill.

Example:
- schemas
- documentation
- examples
- domain-specific notes

## `SKILL.md` Specification & Requirements
Every Skill must contain a `SKILL.md` file that serves as the primary entry point for agent discovery and execution guidance.

The `SKILL.md` file should follow a lightweight, portable structure guided by the Agent Skills Specification. 

At minimum, each `SKILL.md` should include YAML frontmatter followed by Markdown content.

```yaml
---
name: skill-name
description: A description of what this skill does and when to use it.
---
```

Example with optional fields:
```yaml
---
name: skill-name
description: A description of what this skill does and when to use it.
license: MIT
metadata:
  author: example-org
  version: "1.0"
---
```
The markdown body after the frontmatter should include the skill instructions. 

The recommended body sections include:
- Overview
- Step by step instructions
- Example inputs and outputs
- Error handling
- Edge cases