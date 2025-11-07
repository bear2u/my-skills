# Claude Code Best Practices

## Executive Summary

This comprehensive guide synthesizes best practices from 12 sources on using Claude Code effectively. Three core principles emerge:

1. **Context Management is Critical**: Successful users manage context through CLAUDE.md files, strategic `/clear` usage, and documentation systems. Context degradation represents the primary failure mode.

2. **Planning Before Implementation is Essential**: All high-quality sources emphasize upfront planning using Planning Mode or written architectural reviews before coding begins.

3. **Simplicity Over Complexity**: Simple control loops outperform multi-agent systems. Low-level tools combined with selective high-level abstractions work better than heavy frameworks.

---

## General Software Engineering Best Practices

### Test-Driven Development (TDD)

Write tests before implementation to validate AI-generated code reliability. The consensus pattern:
- Create tests first
- Confirm tests fail
- Commit tests separately
- Implement until tests pass
- Never modify tests during implementation

### Code Review Requirements

All code requires human review. As noted: "I'm ultimately responsible for the code in a PR with my name on it, regardless of how it was produced." Multiple eyes catch spaghetti code, missing error handling, and security issues that LLMs miss.

### Quality Gates

Implement hooks for continuous validation:
- TypeScript/linter checks after edits
- Test execution on file changes
- Build validation before commits

*Caveat*: Automatic formatting hooks consume excessive tokens (160k reported in 3 rounds). Format manually between sessions instead.

### Incremental Commits

Commit early with meaningful messages using Conventional Commits format. Each commit should compile and pass tests.

---

## Core Recommendations

### Context Management (Most Critical)

#### CLAUDE.md File Structure

Universal consensus across all sources. Structure as:

**Root file** (100-200 lines):
- Critical universal rules
- Testing instructions
- Quick command reference

**Subdirectory files** (50-100 lines):
- Project-specific context
- Local commands

**Token efficiency**: Keep CLAUDE.md under 2,000 tokens. One team baseline: 20k tokens total (10% of 200k context).

**Anti-patterns to avoid**:
- Don't @-file entire documentation
- Don't write comprehensive manuals
- Do focus on what Claude gets wrong

#### Aggressive Context Clearing

Clear at 60k tokens or 30% context—don't wait for limits. Use `/clear` + `/catchup` pattern for simple restarts.

For complex work: have Claude document progress to markdown, `/clear`, restart fresh reading the progress file.

**Avoid `/compact`**: Automatic compaction is opaque and error-prone.

#### Documentation Systems

The Three-File Pattern for each task:
- `[task]-plan.md` - The accepted plan
- `[task]-context.md` - Key files and decisions
- `[task]-tasks.md` - Work checklist

Update plans during implementation. This enables fresh conversations to pick up exactly where you left off.

---

### Planning & Architecture

#### Planning Mode is Mandatory

Steps:
1. Enter Planning Mode with high-level description
2. Review proposal thoroughly
3. Ask clarifying questions and request alternatives
4. Document accepted plan
5. Implement in stages with periodic plan review

Planning reveals changed requirements and prevents "vibe coding" that creates technical debt.

#### Explore, Plan, Code, Commit Workflow

1. **Explore**: Read files and context without coding
2. **Plan**: Create documented architecture
3. **Code**: Implement with verification steps
4. **Commit**: Update READMEs and create PR

---

### Tool Usage & Automation

#### Skills System with Auto-Activation

Skills need hook-based activation since manual skills are ignored ~90% of the time.

**Hook pattern**: Analyze incoming prompts for keywords, then inject skill activation reminders before Claude sees the message.

**Skill structure**: Main file <500 lines + resource files for progressive disclosure.

#### Hooks for Quality Control

Primary strategy: **Block-at-submit hooks** that prevent commits until requirements met.

Example: Check for test passes before allowing git commits.

Secondary: **Hint hooks** provide non-blocking feedback on suboptimal patterns.

#### Subagents/Task Delegation

Two competing philosophies:

**Custom Specialized Agents**: Build purpose-built subagents (e.g., code-architecture-reviewer)

**Clone Pattern**: Use Task(...) to spawn clones of the main agent, letting it manage orchestration dynamically

The clone pattern preserves more context and avoids gatekeeping. Most users should start with clones.

#### Slash Commands

Use simple shortcuts, not complex workflows. Recommended:
- `/dev-docs` - Strategic planning
- `/catchup` - Read changed files
- `/code-review` - Architectural review
- `/test-route` - Test authenticated endpoints
- `/pr` - Clean up code and prepare

**Anti-pattern warning**: "If you have a long list of complex custom commands, you've created an anti-pattern." Focus on typing naturally.

#### MCP Strategy Evolution

Heavy MCP usage is counterproductive. Quote: "If you're using more than 20k tokens of MCPs, you're crippling Claude."

New philosophy—MCPs should act as secure gateways, not API mirrors:
- Bad: Dozens of tools mirroring REST operations
- Good: Few powerful gateways handling auth/security

Skills > MCPs for most use cases. Use MCPs only for stateful environments.

---

### Workflow Optimization

#### Specificity in Instructions

Vague instructions produce vague results. Provide:
- Specific file paths
- Component patterns to follow
- Tech stack details
- Testing requirements

#### Visual References

Paste screenshots for UI work. Iteration pattern:
1. Provide visual mock
2. Claude implements
3. Take screenshot and compare
4. Iterate (typically 2-3 rounds)

#### Course Correction Techniques

Four tools:
1. Ask for plan first before coding
2. Press Escape to interrupt
3. Double-tap Escape to jump back in history
4. Ask Claude to undo

#### Git Worktrees for Parallel Work

Run multiple Claude instances on independent tasks:
```bash
git worktree add ../project-feature-a feature-a
cd ../project-feature-a && claude
```

---

### Production Code Quality

#### Error Handling Standards

Pattern: Explicit error handling with monitoring.

Gentle reminder hooks check for:
- try-catch blocks
- Async operations
- Database calls
- Sentry error capture

#### Testing Standards

TDD checklist:
- Parameterize inputs
- Ensure tests can fail for real defects
- Compare to independent expectations, not function output
- Test edge cases and boundaries
- Use property-based testing with fast-check

#### Type Safety

Use branded types for IDs. Prefer import type for type-only imports. Override incorrect generated types as needed.

---

### Advanced Patterns

#### Headless Mode for Automation

Use for CI/CD, pre-commit hooks, issue triage:
```bash
claude -p "migrate foo.py from React to Vue" \
  --allowedTools Edit Bash(git commit:*)
```

#### Multi-Claude Verification

Separate contexts for writing and reviewing:
1. Claude A writes code
2. Claude B reviews from fresh context
3. Claude C edits based on feedback

Advanced: Use o3 for planning, Sonnet 4 for verification, Sonnet 3.7 for implementation.

#### Simple Control Loops

Architectural insight: "Debuggability >> complicated multi-agent systems." Claude Code uses one flat message list. Most applications don't need multi-agent complexity.

#### LLM Search Over RAG

Claude Code uses complex ripgrep/jq/find commands rather than RAG. Why: RAG introduces hidden failure modes (similarity function, chunking strategy, reranking). LLM search is simpler and the model handles heavy lifting.

---

## Contradictions & Trade-offs

### Skills vs Context Bloat

**Position A**: Create many specialized skills with progressive disclosure
**Position B**: Keep skills minimal (<100 lines)

**Resolution**: Progressive disclosure matters. Auto-activation hooks are essential either way.

### Custom Subagents vs Clone Pattern

**Position A**: Build specialized subagents for specific roles
**Position B**: Avoid custom subagents; use Task(...) clones

**Resolution**: Both work. Clones preserve context and flexibility. Custom subagents suit highly specialized tasks.

### Auto-Formatting Hooks

Initially recommended, but updated guidance: Don't use auto-format hooks. Token cost (160k in 3 rounds) exceeds marginal benefit. Format manually between sessions.

### Planning Mode vs Manual Plans

**Planning Mode**: Better codebase research
**Manual planning**: More control, better with agent output

**Resolution**: Use Planning Mode for research, exit and create manual dev docs, refine with custom commands.

---

## Essential Practices (Do These First)

1. Create CLAUDE.md (100-200 lines max)
2. Use Planning Mode before coding
3. Clear context aggressively (at 60k tokens)
4. Write tests first (TDD)
5. Be specific in instructions
6. Review all code manually

---

## High-Impact Practices (Implement Soon)

1. Dev docs system (plan/context/tasks files)
2. Skills with auto-activation hooks
3. Quality gate hooks
4. Slash commands
5. Visual references for UI
6. Subagent delegation
7. Course correction patterns (ESC, double-ESC)

---

## Advanced Practices (For Experienced Users)

1. Git worktrees for parallel development
2. Multi-Claude verification
3. Headless mode for automation
4. Minimal MCP servers
5. PM2 for microservices
6. Utility scripts in Skills
7. Living documentation

---

## Practices to Avoid

❌ Auto-formatting hooks (excessive tokens)
❌ Heavy MCP usage (>20k tokens)
❌ Complex multi-agent systems (debugging nightmare)
❌ RAG for code search
❌ Vague instructions
❌ Skipping planning
❌ Filling context to limits

---

## Quick Start Workflow

**Week 1**: Create CLAUDE.md, practice Planning Mode, clear context regularly, review code
**Week 2**: Set up TDD, create slash commands, implement build hooks, add visual references
**Week 3**: Implement dev docs, create Skills, add auto-activation, practice code review
**Week 4**: Audit context usage, optimize CLAUDE.md, add quality gates, experiment with worktrees

---

## Success Metrics

**Context efficiency**:
- Baseline <20k tokens (10% of 200k)
- CLAUDE.md <2,000 tokens
- MCP tools <20k tokens

**Code quality**:
- Test coverage >80%
- Zero TypeScript errors before commits
- Production bugs decreasing over time

**Productivity**:
- Track plan-to-PR time
- Monitor parallel tasks with worktrees
- Reduce context compactions needed

---

## Conclusion

The most successful Claude Code users obsess over three things: context management, upfront planning, and simplicity. Invest time in infrastructure (CLAUDE.md, skills, hooks, docs), and productivity increases significantly. The difference isn't the tool—it's how you use it.