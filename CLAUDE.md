# Knowledge Repository Guidelines

This repository serves as a comprehensive knowledge management system for both personal and professional work. It is organized into discrete projects under the `base/projects/` directory, with individual tasks tracked in the `base/tasks/` directory.

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

- `base/projects/components_ga/` - Dagster Components General Availability project
- `base/projects/ai_software_engineering_blog/` - Blog series about using AI in software engineering

## Task Management

The `base/tasks/` directory contains individual task files for ongoing investigations and work items (both personal and professional) that don't fit within specific projects. Each task file should:

1. **Clear objective**: Document the goal and scope of the task
2. **Background/context**: Include relevant background information when available
3. **Organic structure**: Let sections develop naturally - don't auto-generate "Areas for Investigation" or "Next Steps" sections unless explicitly requested

Tasks are meant to be lightweight investigations that may eventually graduate into full projects or get completed as standalone work.

## Notes

The `base/notes/` directory contains point-in-time, dated documents that capture research findings, insights, or analysis from a specific moment. Note files should:

1. **Date encoding**: Include the date in the filename (e.g., `topic-research-2025-08-11.md`)
2. **Prose format**: Written in flowing prose rather than bullet points or structured formats
3. **Timestamped**: Include the date prominently in the document header
4. **Contextual**: Capture not just facts but analysis and implications for specific scenarios

Notes differ from tasks in that they document completed research or thinking rather than ongoing work items.

## Daily Task Management

The `DAILY_TODO.md` file tracks daily tasks with date-based sections. Each day gets its own section with the date as a header (e.g., `## 2025-08-12`).

Guidelines for daily todos:

1. **Simple format**: Use unchecked bullet points (`- [ ]`) for new tasks
2. **Date-based**: Each day gets its own section with date header
3. **No history tracking**: Focus only on current/recent days, don't maintain extensive history
4. **Organic growth**: Add tasks as they come up throughout the day

### Processing Previous Day TODOs

When starting a new session, Claude should:

1. Check `DAILY_TODO.md` for any unchecked tasks from previous days
2. For each unchecked TODO from previous days, prompt the user with options:
   - **Complete** - Mark as done `[x]`
   - **Move to today** - Move the task to today's section
   - **Delete** - Remove the task entirely
   - **Keep** - Leave unchanged in previous day's section
3. Process each TODO individually, waiting for user response before proceeding to the next

## Knowledge CLI

A Python CLI tool located at `python/knowledge/` provides commands for managing the repository. Uses uv for Python package management.

**Setup**: Run `uv sync` from the repository root to install dependencies, then use `.venv/bin/knowledge` or `.venv/bin/know` to run commands.

### Add Commands

- `knowledge add shower-thought "<thought>"` - Add a shower thought directly to the repository
- `knowledge add task <name>` - Create new task files
- `knowledge add project <name>` - Create new project directories
- `knowledge add todo` - Manage daily todos

### List Commands

- `knowledge ls shower-thought` - List all shower thoughts (newest first)
- `knowledge ls task` - List all task files
- `knowledge ls project` - List all project directories
- `knowledge ls todo` - Show daily todos

### Check Commands

- `knowledge check md` - Check markdown file formatting using prettier
- `knowledge check md --fix` - Fix markdown file formatting issues

## Shower Thoughts Processing

When processing shower thoughts:

1. Always run `git pull` first to ensure you have the latest content
2. Use the shower-thoughts-processor agent to systematically review captured ideas
3. Organize thoughts into appropriate locations (tasks, projects, or existing work streams)
4. Both personal and professional thoughts should be processed and organized
5. When asking which shower thought to process next, always present all remaining options using proper formatting:
   - Use bullet points (not numbered lists)
   - Bold the main topic
   - Include descriptive text after dash
   - Ensure proper line breaks between items
