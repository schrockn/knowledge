# Knowledge Repository Guidelines

This repository serves as a comprehensive knowledge management system for both personal and professional work. It is organized into discrete projects under the `projects/` directory, with individual tasks tracked in the `tasks/` directory.

## Project Guidelines

1. **Self-contained**: Each project should contain everything needed to understand and work on that specific initiative
2. **Clear scope**: Projects should have well-defined boundaries and objectives  
3. **Flexible structure**: Projects can organize their materials however makes sense for their specific needs
4. **Documentation**: Each project must have a CLAUDE.md file with project-specific context and instructions

## Working with Projects

When working on a specific project:
1. Always check the project's CLAUDE.md for specific instructions and context
2. Keep project materials isolated within the project directory
3. Organize materials in whatever way makes sense for that particular project
4. Update project documentation as the work evolves

## Current Projects

- `components_ga/` - Dagster Components General Availability project
- `ai_software_engineering_blog/` - Blog series about using AI in software engineering

## Task Management

The `tasks/` directory contains individual task files for ongoing investigations and work items (both personal and professional) that don't fit within specific projects. Each task file should:

1. **Clear objective**: Document the goal and scope of the task
2. **Progress tracking**: Include a progress log with dates and findings
3. **Next steps**: Maintain a clear list of what needs to be done next
4. **Research notes**: Capture findings, dead ends, and useful links

Tasks are meant to be lightweight investigations that may eventually graduate into full projects or get completed as standalone work.

## Shower Thoughts Processing

When processing shower thoughts:
1. Always run `git pull` first to ensure you have the latest content
2. Use the shower-thoughts-processor agent to systematically review captured ideas
3. Organize thoughts into appropriate locations (tasks, projects, or existing work streams)
4. Both personal and professional thoughts should be processed and organized