---
title: "Claude Code Best Practices: Comprehensive Guide"
url: "https://rosmur.github.io/claudecode-best-practices/"
author: "Claude Code (synthesized from 12 sources)"
date: "2025-11-06"
word_count: 4987
topics: ["AI coding", "Claude Code", "software engineering", "context management", "workflow optimization"]
summary: |
  This comprehensive guide synthesizes 12 expert sources on using Claude Code
  effectively. The three core takeaways are: (1) context management is paramount
  through CLAUDE.md files and aggressive clearing, (2) planning before implementation
  is essential for production code, and (3) simplicity beats complexity in agent
  design. The guide covers general practices, core recommendations by category,
  contradictions and trade-offs, and practical quick-start workflows.
main_points:
  - Context management through CLAUDE.md files, documentation systems, and aggressive token clearing is the primary success factor
  - Planning Mode and structured architectural review before coding prevents technical debt and misalignment
  - Simple control loops and low-level tools (Bash, Read, Edit) outperform complex multi-agent systems
  - Test-Driven Development and continuous quality gates enforce code reliability
  - Skills with auto-activation hooks and context-aware slash commands improve workflow efficiency
content_type: "guide"
difficulty: "advanced"
---

# Claude Code Best Practices: Comprehensive Guide

## Core Summary

This guide distills best practices from 12 expert sources on using Claude Code for production-quality development. Success hinges on three pillars: obsessive context management, mandatory planning before implementation, and architectural simplicity. The guide provides actionable recommendations organized by priority level, complete with workflows, anti-patterns to avoid, and metrics for measuring success.

## The Three Critical Takeaways

### 1. Context Management is Paramount

The most successful Claude Code workflows obsessively manage context through:
- **CLAUDE.md files** (100-200 lines maximum) documenting project-specific rules and command references
- **Aggressive clearing** at 60k tokens or 30% context threshold
- **Documentation systems** using plan.md, context.md, and tasks.md structure
- **Token-efficient tool design** keeping baseline context under 20k tokens

"Context degradation is the primary failure mode" across production deployments.

### 2. Planning Before Implementation is Non-Negotiable

Eight sources emphasize upfront planning for production code:
- Use Planning Mode to research codebase and propose approaches
- Create written development docs before implementation
- Challenge assumptions and request alternative approaches
- Document decisions in version-controlled planning files
- "Vibe coding" works only for throwaway MVPs, not production systems

### 3. Simplicity Beats Complexity

"Simple control loops outperform multi-agent systems. Low-level tools plus selective abstractions beat heavy RAG or complex frameworks."

The Claude Code architecture itself uses:
- One main thread (flat message list)
- Maximum one branching point (subagent results)
- LLM search via ripgrep/jq rather than RAG
- Minimal, purposeful tool abstraction

## Essential Practices (Implement First)

### Create CLAUDE.md (100-200 lines max)

Structure the file as:
- **Root CLAUDE.md**: Critical universal rules, command reference, testing instructions, repository etiquette
- **Subdirectory CLAUDE.md**: Project-specific context (50-100 lines each)

Anti-patterns to avoid:
- Don't embed entire files with @-mentions; instead reference documentation paths
- Don't write negative prescriptions ("Never use X flag"); suggest positive alternatives
- Don't create comprehensive manuals; document what Claude gets wrong

**Token efficiency**: One team reports 20k baseline tokens (10% of 200k context) with strategic CLAUDE.md structure.

### Aggressive Context Clearing

Clear context at:
- 60k tokens, or
- 30% of available context

Use the `/clear` + `/catchup` pattern for simple restarts. For complex tasks, implement "Document & Clear":
1. Have Claude write progress to .md file
2. Execute `/clear`
3. Start fresh session reading the progress file
4. Continue work

"Don't use /compact; it's opaque, error-prone, and not well-optimized" for preserving important details.

### Test-Driven Development Pattern

The consensus workflow:
1. Write tests BEFORE implementation
2. Confirm tests fail (avoid mock implementations)
3. Commit tests separately
4. Implement until tests pass
5. Do NOT modify tests during implementation

"AI-generated code often works superficially but contains subtle bugs. Tests provide the only reliable validation mechanism."

### Planning Workflow (Explore → Plan → Code → Commit)

**Step 1: Explore** - Tell Claude NOT to code yet; read relevant files, existing patterns, images, URLs
**Step 2: Plan** - Use Planning Mode, research details, verify architecture, create written plan
**Step 3: Code** - Implement with explicit verification steps, commit in stages
**Step 4: Commit** - Update documentation, create PR with clear commit messages

"Steps 1-2 are crucial—without them, Claude tends to jump straight to coding."

### Be Specific in Instructions

Bad: "Add a user settings page"

Good: "Create user settings page at /settings with profile section (name, email, avatar), notification preferences (checkboxes), using UserProfile component pattern, MUI v7 grid layout, and form validation tests"

## High-Impact Practices to Implement Soon

### Dev Docs System

Use the three-file pattern for each feature:

```
~/dev/active/[task-name]/
├── [task-name]-plan.md       # Accepted plan
├── [task-name]-context.md    # Key files, decisions
└── [task-name]-tasks.md      # Work checklist
```

Update the plan document during implementation to reveal changed requirements and enable fresh conversations to resume exactly where you left off.

### Skills with Auto-Activation Hooks

Manual skills are ignored ~90% of the time. The solution: hook-based auto-activation via:

**UserPromptSubmit Hook** (before Claude sees message):
- Analyze prompt for keywords/intent
- Inject skill activation reminders
- Claude sees recommendation before processing

**Stop Event Hook** (after response):
- Analyze edited files for risky patterns
- Display gentle self-check reminders
- Non-blocking awareness cues

Skill structure best practices:
- Main SKILL.md: Under 500 lines
- Use progressive disclosure with resource files
- Token efficiency improved 40-60% after restructuring

### Quality Gate Hooks

Implement non-blocking hooks for:
- Build checker (TypeScript/linter errors)
- Test runner (ensure passing tests)
- Error handling reminder
- Skills auto-activation

Strategy: "Don't block at write time—let the agent finish its plan, then check the final result."

### Continuous Quality Gates

Enforce quality automatically with:
- TypeScript/linter checks after every edit
- Build validation before commits
- Test execution on file changes
- Manual formatting between sessions (avoid auto-formatting hooks; they consume 160k tokens in 3 rounds)

### Code Review (Self + Human)

Multi-layer review process:
1. **Claude self-review**: Ask Claude to review its own code using subagents or fresh context
2. **Human review**: Manually verify behavior and test coverage
3. **Multiple Claude instances**: One writes, another reviews with fresh context

Look for: spaghetti code, substantial API changes, unnecessary imports, missing error handling, security issues.

## Advanced Patterns

### Git Worktrees for Parallel Work

Run multiple Claude instances on independent tasks:

```bash
git worktree add ../project-feature-a feature-a
cd ../project-feature-a && claude

# In new terminal:
git worktree add ../project-feature-b feature-b
cd ../project-feature-b && claude
```

Best practices: consistent naming, one terminal per worktree, notifications for attention needed, separate IDE windows, clean up afterward.

### Multi-Claude Verification Pipeline

Separate contexts for writing and reviewing:
1. Claude A writes code
2. `/clear` or start Claude B in new terminal
3. Claude B reviews Claude A's work
4. `/clear` or start Claude C
5. Claude C reads code and review, edits based on feedback

Advanced: o3 + Sonnet pipeline for critical code:
- o3: Generate plan
- Sonnet 4: Verify plan, create task list
- Sonnet 3.7/4: Execute plan
- Sonnet 4: Verify against plan
- o3: Verify against original ask
- Feed issues back into plan template

### Subagent Delegation Strategy

Two competing approaches:

**Custom Specialized Subagents**:
- code-architecture-reviewer
- build-error-resolver
- strategic-plan-architect

**Master-Clone Architecture** (preferred):
- Put all context in CLAUDE.md
- Let main agent use Task(...) to spawn clones
- Agent manages orchestration dynamically
- Preserves context better, more flexible

Resolution: Start with clone pattern for most tasks. Use specialized subagents only for highly specific, narrow tasks.

## Common Tools & Optimization

### Recommended Slash Commands

**Planning/Docs**:
- `/dev-docs` - Create strategic plan
- `/catchup` - Read changed files in branch
- `/create-dev-docs` - Convert plan to dev doc files

**Quality**:
- `/code-review` - Architectural review
- `/build-and-fix` - Run builds and fix errors

**Testing**:
- `/test-route` - Test authenticated routes
- `/route-research-for-testing` - Find affected routes

**Git Integration**:
- `/pr` - Clean up code, prepare PR with commit message

Philosophy: "If you have a long list of complex custom commands, you've created an anti-pattern. The entire point is to type almost whatever you want and get useful results."

### MCP Strategy: "Scripting Model"

Heavy MCP usage is an anti-pattern. If using >20k tokens of MCPs, "you're crippling Claude, giving you only 20k tokens left of actual work before context is cooked."

Better approach:
- Few powerful gateway tools (download_raw_data, take_sensitive_action, execute_code)
- MCP handles auth/security, agent scripts against data
- Most stateless tools → Simple CLIs documented in Skills
- MCPs only for stateful environments (e.g., Playwright)

### Error Handling Standards

```typescript
try {
  await prismaOperation()
} catch (error) {
  Sentry.captureException(error)  // Must capture
  throw new CustomError('Descriptive message', { context })  // Include context
}
```

Philosophy: "Fail fast with descriptive messages. Never silently swallow exceptions."

## Key Contradictions & Trade-Offs

### Skills Volume vs Context Efficiency

**More skills approach**: Multiple specialized skills (frontend, backend, workflow, notification guidelines)

**Minimal skills approach**: Keep skills under 100 lines total

**Resolution**: Progressive disclosure (main <500 lines + resource files). Token budget determines skill count. Measure baseline context usage and adjust accordingly.

### Auto-Formatting Hooks

**Original recommendation**: Auto-format after edits for consistency

**Updated consensus**: Don't auto-format in hooks—they consume excessive tokens (160k reported in 3 rounds)

**Better practice**: Run Prettier manually between sessions

### Planning Mode vs Manual Plans

**Built-in Planning Mode**: Better codebase research, structured output

**Custom planning with slash commands**: More control, can see agent output while planning

**Resolution**: Use Planning Mode for research phase, then exit and create manual dev docs from results. Use custom slash commands for plan refinement. This combines benefits of both approaches.

## Architecture & Design Principles

### Simple Control Loops > Multi-Agent Systems

"Debuggability >> complicated hand-tuned multi-agent lang-chain-graph-node mishmash"

Claude Code architecture:
- One main thread (flat message list)
- Maximum one branch (subagent results)
- No complex multi-agent orchestration
- Simple iterative tool calling

Reasoning: Every abstraction layer makes debugging exponentially harder. LLMs are fragile; added complexity breaks unpredictably.

### LLM Search > RAG for Code

Claude Code uses complex ripgrep, jq, find commands rather than RAG.

RAG introduces hidden failure modes:
- What similarity function?
- What reranker?
- How to chunk code?
- How to handle large JSON/logs?

LLM search:
- Examines 10 lines to understand structure
- Requests 10 more if needed (like humans)
- Reinforcement-learnable
- Model does heavy lifting, fewer moving parts

### Tool Abstraction Strategy

Strategic mix:
- **Low-level** (Bash, Read, Write): Flexibility
- **Medium-level** (Edit, Grep, Glob): Frequently used patterns
- **High-level** (Task, WebFetch): Deterministic workflows

Decision framework: High-frequency tasks → Dedicated tools. Low-frequency → Use Bash. Highly deterministic → High-level tools.

## Production Code Quality Standards

### Testing Checklist

1. Parameterize inputs (no magic numbers/strings)
2. Add test only if it can fail for real defect
3. Ensure description matches assertion
4. Compare to independent expectations, not function output
5. Follow same lint/type-safety as production code
6. Express invariants/axioms (use fast-check for property tests)
7. Group unit tests under describe(functionName)
8. Use expect.any(...) for variable parameters
9. Use strong assertions (toEqual vs toBeGreaterThanOrEqual)
10. Test edge cases, realistic input, boundaries
11. Don't test conditions caught by type checker

Test types:
- **Unit tests**: Colocated *.spec.ts
- **Integration tests**: Separate from unit tests (don't mock DB)
- **Property-based tests**: Use fast-check for invariants

### Type Safety Practices

```typescript
// Prefer branded types for IDs
type UserId = Brand<string, 'UserId'>  // ✅
type UserId = string                   // ❌

// Use import type for type-only imports
import type { User } from './types'    // ✅

// Override incorrect generated types in db-types.override.ts
export interface CustomOverride {
  bigIntField: string;  // Override BigInt → string
}
```

### Visual References for UI Work

Methods:
- Paste screenshots (macOS: cmd+ctrl+shift+4 → ctrl+v)
- Drag and drop images
- Provide image file paths
- Use design mocks as reference

Iteration pattern:
1. Give Claude visual mock
2. Implement in code
3. Take screenshot of result
4. Compare and iterate
5. Usually 2-3 iterations for good match

## Quick-Start Workflow (4-Week Ramp-Up)

### Week 1: Foundations
- Create CLAUDE.md with commands and testing instructions
- Practice Planning Mode → review → implement → commit
- Start clearing context at 60k tokens
- Manually review all AI-generated code

### Week 2: Quality Systems
- Set up TDD workflow
- Create 2-3 custom slash commands
- Implement basic build checker hook
- Add visual references to UI work

### Week 3: Advanced Context
- Implement dev docs system
- Create 1-2 Skills for common patterns
- Add skill auto-activation hook
- Practice subagent code review

### Week 4: Optimization
- Audit context usage with `/context`
- Optimize CLAUDE.md
- Add quality gate hooks
- Experiment with git worktrees

## Success Metrics

### Context Efficiency
- Baseline context cost: <20k tokens (10% of 200k)
- CLAUDE.md size: <2000 tokens
- MCP tools total: <20k tokens
- Context clearing: Every 60k tokens or less

### Code Quality
- Test coverage: >80% for new code
- TypeScript errors: Zero before commits
- Code review findings: Track patterns, update CLAUDE.md
- Production bugs from AI code: Decreases over time

### Productivity
- Time from plan to PR: Track and optimize
- Plan iterations: Should stabilize at 1-3
- Context compactions: Decrease with better practices
- Parallel tasks: Can scale to 3-4 with worktrees

## Practices to Avoid

❌ Auto-formatting hooks (excessive token consumption)
❌ Heavy MCP usage (>20k tokens)
❌ Complex multi-agent orchestration
❌ RAG for code search
❌ Vague instructions
❌ Skipping planning phase
❌ Letting context fill to limits

## Core Insight

"The difference between frustration and productivity isn't the tool—it's how you use it. Invest time in your infrastructure (CLAUDE.md, skills, hooks, docs), and you'll build production-quality code with confidence."

Success requires obsessive context management, rigorous upfront planning, and architectural simplicity. These foundational practices compound across every future task.
