# Read-Only IDE for Agentic Development

_Date: 2025-08-10_

## Core Insight

The terminal or chat-based agentic UI for authoring software is transformative and opens an "empty" space for a new tool that sits somewhere between a terminal and an IDE. The key realization is that the terminal or chat should be _the_ way to edit files, but there should be a complementary visual component that serves as context and oversight.

## The Read-Only IDE Concept

This visual component would function as a read-only IDE whose primary purpose is giving developers context on what the agent has done, is doing, and what it plans to do. Rather than being another editing interface, it serves as a comprehensive view into the agentic development process.

The interface could represent the contents of software projects more abstractly by stacking framework-specific concepts on top of the traditional file system view. For Dagster projects specifically, this could mean toggling between standard file-change views and more visual representations like "asset graph diffing" that Dagster has built internally.

## Integration Opportunities

This read-only IDE concept could be built as an additive feature in "dg dev", Dagster's local development experience. The tool would provide developers with rich context about their Dagster projects while maintaining the agentic terminal interface as the primary editing mechanism.

There's also alignment with planned features for editing subsets of code in a code location directly from branch deployments. In these scenarios, the read-only IDE would provide essential context about the broader project while developers make targeted changes through the agentic interface.

## Broader Applications

The lessons learned from building the knowledge app demonstrate the power of purpose-built tooling that understands specific domains. This read-only IDE approach could extend beyond Dagster to any framework where abstract representations of code structure provide more value than traditional file trees. The key is maintaining the separation between the agentic editing interface and the contextual viewing interface, allowing each to excel at its specific purpose.
