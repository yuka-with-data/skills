---
name: template
description: description of what this skill does and when it should be used.
license: Apache-2.0
compatibility: Requires git, docker, jq, and access to the internet
metadata:
  author: example-org
  version: "1.0"
  created: "2026-01-15"
  updated: "2026-05-13"
  maintainer: "user"
allowed-tools: Bash(git:*) Bash(jq:*) Read
---
# [Template] Document Contributing Skill
## Overview
Brief description of what the skill does in a concise and practical way

Explains:
- primary purpose
- expected workflow
- major constraints

## Prerequisites Checklist
Before using this skill, ensure the following requirements are met:
- [ ] Python 3.8 or higher
- [ ] Required Python dependencies
- [ ] Valid authentication credentials
- [ ] Required environment variables
- [ ] Network access is available for external API or data source calls (if applicable)
- [ ] Target tools or services used by this skill are accessible and operational

## When to Use This Skill
### trigger conditions:
Use this skill when:
- condition 1
- condition 2
- condition 3
### Do NOT Use This Skill When:
- exclusion case 1
- exclusion case 2

## Execution Flow
Follow this step-by-step process:
1. A
2. B
3. C
4. D

## Tool Guidance
### Tool_name1
Purpose:
- A
- B

Key Rules:
- Rule 1
- Rule 2

## Response Guidelines
- Keep outputs structured and predictable
- Avoid unnecessary verbosity
- etc.

## Error Handling
if execution fails:
- Identify the cause
- Provide fallback stragety if possible
- etc.

## Validation
> File reference example

Run the validation script:
```bash
python scripts/validate_dataset.py data/my_dataset.csv
```

## Examples
### Example 1
User: "Example request"

Flow:
- Check prerequisites
- Select tool
- Execute
- Format output

### Example 2