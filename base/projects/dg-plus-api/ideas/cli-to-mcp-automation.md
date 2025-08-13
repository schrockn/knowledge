# CLI to MCP Automation

**Original thought:** "Automating cli to mcp"

## Objective

Develop a generic way of injecting CLI commands into an MCP (Model Context Protocol) server. This addresses user requests for use cases like querying logs in Dagster Plus and integrating them into development loops.

## Context

People are asking for ways to integrate Dagster Plus functionality into their development workflows through MCP. A standardized approach to exposing CLI commands through MCP would enable:

- Log querying from Dagster Plus within dev environments
- Integration with AI-assisted development workflows
- Consistent patterns for exposing CLI functionality via MCP

## Implementation Approach

This should be a generic solution that can wrap arbitrary CLI commands and expose them through the MCP protocol, making it easy to add new capabilities without custom MCP integration code for each command.
