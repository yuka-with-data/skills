# Skills
>
> A curated collection of AI Agent Skills, reusable Skill patterns, templates, examples, and reference implementations.

This repository serves as both a public resource and a showcase of practical Skill development across modern AI agent ecosystems.

Skills are actively used as operational capability layers alongside tools, MCP servers, APIs, and application backends across my AI and agent-based projects.

The goal is to help developers:

- understand how Skills are structured and organized
- explore reusable Skill patterns and workflows
- discover practical Skill examples and templates
- build portable and maintainable Skills across projects

## What You'll Find

This repository includes:

- reusable Skill templates
- reference implementations
- demonstration Skills
- documented Skill patterns
- selected production-ready Skill examples
- personal Skill showcases and experiments

While some production Skills may live directly inside applications, MCP servers, or other repositories, this collection focuses on reusable knowledge, examples, and patterns that can be adapted across projects.

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

## Prompt vs System Prompt vs Skill

Understanding the difference between these layer is important when building AI agents and resuable Skills.

| Layer | Scope | Purpose | Persistence | Controlled By |
| --- | --- | --- | --- | --- |
| **System Prompt** | Global | Defines the agent’s overall behavior, rules, and personality | Always active during runtime | Developer |
| **Skill** | Domain capability | Provides reusable task knowledge, workflows, scripts, and references | Loaded dynamically when relevant | Developer |
| **Prompt** | Task request | Tells the agent what to do for a specific interaction | Temporary / one-time | User |

### Mental Model

- **System Prompt** → *How the agent should behave*
- **Skill** → *What specialized capability the agent can use*
- **Prompt** → *What the user wants done right now*

### Example: Difference

A coding agent might have

- A **System Prompt** that says:
  - “Be concise”
  - “Explain reasoning clearly”
  - “Follow safe coding practices”

- A **Python Debugging Skill** containing:
  - debugging workflows
  - validation scripts
  - common error patterns
  - troubleshooting references

- A **User Prompt** like:
  - “Help me fix this async bug in FastAPI”

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

### YAML Frontmatter

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

### The Body

The markdown body after the frontmatter should include the skill instructions.

The recommended body sections include:

- Overview
- Step by step instructions
- Example inputs and outputs
- Error handling
- Edge cases

### What `SKILL.md` is for

The Skill layer should focus on:

- agent behavior
- workflow guidance
- tool orchestration
- execution patterns

#### For concrete implementation patterns and directory structure examples, refer to the `templates/` directory in this repository

## Recommended Architecture

```txt
Skill Layer
 ↓ 
Agent Runtime (Codex / Claude / etc.)
 ↓ 
Tools / MCP / APIs
 ↓ 
Application Logic & Data Sources
```

## Compatibility

This repository follows convensions inspired by:

- Agent Skills
- Hugging Face Context Engineering
- Codex Skills
- Claude-style agent workflows

The goal is to keep Skills portable and adaptable across multiple agent ecosystem.

## `SKILL.md` File Size Guideline

- Metadata (frontmatter): lightweight (~ 100 tokens and ~10–25 lines, always loaded as part of skill listing)
- SKILL.md body (core instructions): ≤ 500 lines and ≤ 5,000 tokens (loaded on activation)
- Skill listing visibility (Codex contraint):
  - Initial skill descriptions are compressed into ~2% of context or ~8,000 characters total
  - Large skill sets may be shortened or partially omitted from the initial list
  - Description is prioritized for compression → keep it high-signal and compact
- Design implication: SKILL.md must assume it will often be seen in a compressed form before activation
- Architecture principle (progressive disclosure):
  - SKILL.md = decision layer (what to do, when, and which tools to use)
  - external files = detailed knowledge (how to do it)
  - details must be explicitly loaded when required

## Resources

Agent Skills Spec:
<https://agentskills.io/skill-creation/best-practices>

Open AI Codex Skills:
<https://developers.openai.com/codex/skills>

Hugging Face Skill Format:
<https://huggingface.co/learn/context-course/unit1/skill-format>

How Skills compares to prompts, Projects, MCP, and subagents:
<https://claude.com/blog/skills-explained>
