# Internal Subagent Model Implementation

**Original thought:** "Implement subagents in compass [sms]"

## Objective

Implement an internal subagent model, which effectively means having specific base prompts for different tasks as a starting point.

## Concept

Rather than using a single general-purpose AI assistant, create specialized subagents that are optimized for specific types of tasks. Each subagent would have:

- Task-specific base prompts and context
- Specialized knowledge and capabilities
- Tailored response patterns and workflows
- Domain-specific expertise

## Implementation Approach

The subagent model should:

- Define clear task categories that benefit from specialization
- Create optimized base prompts for each task type
- Implement routing logic to select the appropriate subagent
- Maintain consistency while enabling specialization

## Benefits

- More targeted and relevant responses for specific tasks
- Better context awareness for domain-specific work
- Improved efficiency through specialized workflows
- Clearer separation of concerns between different types of assistance
