# GraphQL Changes Automation

**Original thought:** "Automation around porting graphql changes"

## Objective

Create automation to keep dg plus API commands up-to-date with changes in the GraphQL schema once the wrapper is set up.

## Context

As part of the dg-plus-api project, we're building a REST-like wrapper around our GraphQL API. However, the GraphQL schema will continue to evolve, and we need automated processes to ensure our API wrapper stays synchronized with these changes.

## Key Requirements

- Detect when GraphQL schema changes occur
- Automatically update the corresponding REST-like API endpoints
- Maintain compatibility and handle breaking changes gracefully
- Ensure the CLI commands reflect the latest schema capabilities

## Implementation Considerations

This automation is critical for maintaining the dg-plus-api wrapper without constant manual updates. It should handle schema evolution seamlessly while preserving the user-friendly API patterns we establish.
