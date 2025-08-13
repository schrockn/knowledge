# Docs Auditor Agent

**Original thought:** "Docs auditor"

## Objective

Create an agent that takes an adversarial approach to documentation. Given a blank context, examine docs and content to see if a person can figure out a concept or API in Dagster.

## Approach

The agent should:

- Start with zero prior knowledge/context
- Review documentation from a newcomer's perspective
- Identify gaps, unclear explanations, or missing context
- Test whether concepts can be understood without existing domain knowledge
- Flag areas where documentation assumes too much prior understanding

## Use Cases

- Audit Dagster API documentation for clarity and completeness
- Evaluate tutorial effectiveness for new users
- Identify documentation that requires additional context or examples
- Test whether concepts are self-contained and learnable from docs alone

## Implementation Vision

This agent would be particularly valuable for ensuring Dagster documentation is accessible to developers who are new to the framework, helping identify places where expert knowledge is assumed but not explained.
