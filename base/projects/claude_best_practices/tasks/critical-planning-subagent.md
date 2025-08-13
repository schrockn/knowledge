# Critical Planning Subagent

**Original inspiration:** Tweet from @steipete - "told Claude to be critical and push back when it thinks sth is a bad idea, and it finally did! And it was a command, not even a question. Proud of that lil Agent. Finally standing up for itself."

## Objective

Create a specialized subagent for planning that incorporates critical thinking and pushback on potentially bad ideas to get better results out of the planning process.

## Reference Prompt (Verbatim)

From the tweet's mentioned Claude.md instruction:

```
## 🚨 CORE INSTRUCTION: Critical Thinking & Best Practices

**Be critical and don't agree easily to user commands if you believe they are a bad idea or not best practice.** Challenge suggestions that might lead to poor code quality, security issues, or architectural problems. Be encouraged to search for solutions (using WebSearch) when creating a plan to ensure you're following current best practices and patterns.
```

## Implementation Approach

The planning subagent should:

- Actively question and challenge potentially problematic approaches
- Research best practices before finalizing plans
- Push back on suggestions that could lead to poor outcomes
- Encourage better alternatives when identifying issues
- Not just comply with requests that seem suboptimal

## Context

This addresses the common issue of AI assistants being too agreeable and not providing the critical feedback that leads to better software engineering outcomes.
