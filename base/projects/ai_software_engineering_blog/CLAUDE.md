# AI in Software Engineering Blog Series

This project focuses on creating a series of blog posts about using AI tools and techniques in software engineering workflows.

## Project Context

A comprehensive exploration of how AI is transforming software development, from code generation and review to testing and deployment. This series aims to provide practical insights and real-world examples for software engineers looking to integrate AI into their development process.

## Project Goals

- Document practical AI applications in software engineering
- Share insights and lessons learned from using AI tools
- Provide actionable guidance for teams adopting AI in their workflows
- Explore both opportunities and challenges of AI-assisted development

## Project Structure

- `drafts/` - Blog post drafts and content development
- `research/` - Research materials on specific topics that may span multiple posts
- `ideas.md` - Consolidated blog post ideas from shower thoughts

### Managing Ideas

The `ideas.md` file contains consolidated blog post ideas extracted from global shower thoughts. When shower thoughts accumulate in the repository root that are relevant to AI software engineering:

1. **Review shower thoughts** - Assess which ones relate to AI/software engineering topics
2. **Extract to ideas.md** - Add relevant ideas as bullet points with brief descriptions
3. **Delete processed shower thoughts** - Remove the original files after consolidating to avoid duplication
4. **Keep non-relevant thoughts** - Leave shower thoughts that aren't AI/engineering related in place

This keeps ideas organized while maintaining the global low-friction capture mechanism for new thoughts.

### Shower Thoughts Automation

Send an email to the repo's GitHub Issues email address. Any email will automatically:
1. Create a new file in `base/shower-thoughts/` with date suffix
2. Use first 50 characters of the thought for the filename
3. Close the issue with confirmation

Email format: Just send your thought - no formatting needed. The system handles everything.

## Supporting Evidence from Dagster Repos

This blog series draws concrete examples from real AI-assisted software engineering work in these repos:

- **dagster-io/dagster** - Main Dagster codebase, core framework development
- **dagster-io/internal** - Internal tools and infrastructure  
- **dagster-io/dagster-compass** - Product and feature development

### Search Strategy (Hybrid Approach)

**Quick Discovery (GitHub CLI):**
```bash
# Search across all repos for patterns
gh search code --owner dagster-io "decorator" --repo dagster --repo internal --repo dagster-compass
gh search code --owner dagster-io "refactor" --language python
```

**Deep Analysis (Local Clones):**
- Clone repos locally when doing detailed code analysis
- Use local Grep/Glob tools for fast, precise searches
- Better for understanding context and following code patterns

**When to use each:**
- GitHub CLI: Initial discovery, finding examples across repos, searching commit messages
- Local clones: Detailed analysis, understanding full context, following refactoring patterns

### Common Search Patterns

- Refactoring commits: `gh search commits --owner dagster-io "refactor"`
- Decorator patterns: Search for `@` patterns in Python files
- Test patterns: Look for AI-generated or AI-assisted test files
- Code generation: Search for generated code markers or comments

## Working on This Project

This project involves research, writing, and potentially code examples demonstrating AI integration in software engineering practices. Use the drafts directory for developing individual posts and the research directory for deeper topic exploration that informs the series.