"""CLI entry point for knowledge repository management."""

import click
from pathlib import Path
import os
import subprocess
import sys
import re
from datetime import datetime


@click.group()
@click.version_option()
def main():
    """Knowledge repository management CLI."""
    pass


# ADD command group
@main.group()
def add():
    """Add new items to the knowledge repository."""
    pass


@add.command('shower-thought')
@click.argument('thought')
def add_shower_thought(thought):
    """Add a shower thought to the repository."""
    repo_root = find_repo_root()
    
    # Parse title and body from input (same logic as GitHub action)
    if ':' in thought:
        title_part, body_part = thought.split(':', 1)
        title_part = title_part.strip()
        body_part = body_part.strip()
    else:
        title_part = thought.strip()
        body_part = ''
    
    # Sanitize title for filename (same logic as GitHub action)
    sanitized_title = sanitize_title(title_part)
    current_date = datetime.now().strftime('%Y-%m-%d')
    filename = f"{sanitized_title}-{current_date}.md"
    
    # Ensure shower-thoughts directory exists
    shower_thoughts_dir = repo_root / "base" / "shower-thoughts"
    shower_thoughts_dir.mkdir(parents=True, exist_ok=True)
    
    # Create file path
    filepath = shower_thoughts_dir / filename
    
    # Check if file already exists, add counter if needed
    counter = 1
    original_filepath = filepath
    while filepath.exists():
        stem = original_filepath.stem
        suffix = original_filepath.suffix
        filepath = original_filepath.parent / f"{stem}-{counter}{suffix}"
        counter += 1
    
    # Write the content (use body if available, otherwise title)
    content = body_part if body_part else title_part
    
    filepath.write_text(content)
    
    click.echo(f"Created shower thought: {filepath}")
    click.echo(f'Title: "{title_part}"')
    if body_part:
        click.echo(f'Body: "{body_part}"')


@add.command('task')
@click.argument('name')
def add_task(name):
    """Create a new task file."""
    repo_root = find_repo_root()
    tasks_dir = repo_root / "base" / "tasks"
    tasks_dir.mkdir(parents=True, exist_ok=True)
    
    task_file = tasks_dir / f"{name}.md"
    if task_file.exists():
        click.echo(f"Task file {task_file} already exists")
        return
    
    task_file.write_text(f"# {name.title()}\n\n")
    click.echo(f"Created task file: {task_file}")


@add.command('project')
@click.argument('name')
def add_project(name):
    """Create a new project directory."""
    repo_root = find_repo_root()
    projects_dir = repo_root / "base" / "projects"
    projects_dir.mkdir(parents=True, exist_ok=True)
    
    project_dir = projects_dir / name
    project_dir.mkdir(exist_ok=True)
    
    claude_md = project_dir / "CLAUDE.md"
    if not claude_md.exists():
        claude_md.write_text(f"# {name.title()} Project\n\n")
    
    click.echo(f"Created project directory: {project_dir}")


@add.command('todo')
def add_todo():
    """Manage daily todos."""
    repo_root = find_repo_root()
    todo_file = repo_root / "DAILY_TODO.md"
    
    if not todo_file.exists():
        click.echo(f"No DAILY_TODO.md found at {todo_file}")
        return
    
    click.echo(f"Opening {todo_file}")
    # You can add logic here to open in editor or process todos


# LS command group
@main.group()
def ls():
    """List items in the knowledge repository."""
    pass


@ls.command('shower-thought')
def ls_shower_thought():
    """List shower thoughts."""
    repo_root = find_repo_root()
    shower_thoughts_dir = repo_root / "base" / "shower-thoughts"
    
    if not shower_thoughts_dir.exists():
        click.echo("No shower thoughts directory found")
        return
    
    thoughts = sorted(shower_thoughts_dir.glob("*.md"), key=lambda x: x.stat().st_mtime, reverse=True)
    if not thoughts:
        click.echo("No shower thoughts found")
        return
    
    click.echo(f"Found {len(thoughts)} shower thoughts:")
    for thought in thoughts:
        click.echo(f"  {thought.name}")


@ls.command('task')
def ls_task():
    """List task files."""
    repo_root = find_repo_root()
    tasks_dir = repo_root / "base" / "tasks"
    
    if not tasks_dir.exists():
        click.echo("No tasks directory found")
        return
    
    tasks = sorted(tasks_dir.glob("*.md"))
    personal_tasks = sorted((tasks_dir / "personal").glob("*.md")) if (tasks_dir / "personal").exists() else []
    
    if not tasks and not personal_tasks:
        click.echo("No tasks found")
        return
    
    if tasks:
        click.echo("Tasks:")
        for task in tasks:
            click.echo(f"  {task.stem}")
    
    if personal_tasks:
        click.echo("Personal tasks:")
        for task in personal_tasks:
            click.echo(f"  personal/{task.stem}")


@ls.command('project')
def ls_project():
    """List project directories."""
    repo_root = find_repo_root()
    projects_dir = repo_root / "base" / "projects"
    
    if not projects_dir.exists():
        click.echo("No projects directory found")
        return
    
    projects = sorted([p for p in projects_dir.iterdir() if p.is_dir()])
    if not projects:
        click.echo("No projects found")
        return
    
    click.echo(f"Found {len(projects)} projects:")
    for project in projects:
        click.echo(f"  {project.name}")


@ls.command('todo')
def ls_todo():
    """Show daily todos."""
    repo_root = find_repo_root()
    todo_file = repo_root / "DAILY_TODO.md"
    
    if not todo_file.exists():
        click.echo("No DAILY_TODO.md found")
        return
    
    content = todo_file.read_text()
    click.echo(content)


# CHECK command group
@main.group()
def check():
    """Check various aspects of the knowledge repository."""
    pass


@check.command('md')
@click.option('--fix/--no-fix', default=False, help='Fix formatting issues (default: just check)')
def check_md(fix):
    """Check markdown file formatting using prettier."""
    repo_root = find_repo_root()
    
    # Check if pnpm is available
    try:
        subprocess.run(['pnpm', '--version'], capture_output=True, check=True)
    except (FileNotFoundError, subprocess.CalledProcessError):
        click.echo("Error: pnpm not found. Please install pnpm:")
        click.echo("  - npm install -g pnpm")
        click.echo("  - Or visit https://pnpm.io/installation for other methods")
        sys.exit(1)
    
    # Find all markdown files in the repository
    md_files = []
    for md_file in repo_root.rglob("*.md"):
        # Skip hidden directories and node_modules
        if any(part.startswith('.') for part in md_file.parts):
            continue
        if 'node_modules' in md_file.parts:
            continue
        md_files.append(str(md_file))
    
    if not md_files:
        click.echo("No markdown files found to format")
        return
    
    click.echo(f"Found {len(md_files)} markdown files to check")
    
    # Prepare pnpm dlx prettier command
    cmd = ['pnpm', 'dlx', 'prettier']
    
    if fix:
        cmd.append('--write')
    else:
        cmd.append('--check')
    
    # Add file extensions and files
    cmd.extend(['--parser', 'markdown'])
    cmd.extend(md_files)
    
    try:
        result = subprocess.run(cmd, cwd=repo_root, capture_output=True, text=True)
        
        if result.stdout:
            click.echo(result.stdout)
        if result.stderr:
            click.echo(result.stderr, err=True)
        
        if result.returncode != 0:
            if not fix:
                click.echo("Some files need formatting. Run 'knowledge check md --fix' to fix them.")
            else:
                click.echo("Prettier encountered an error")
            sys.exit(result.returncode)
        else:
            if not fix:
                click.echo("All files are properly formatted")
            else:
                click.echo("All files have been formatted")
                
    except subprocess.SubprocessError as e:
        click.echo(f"Error running pnpm dlx prettier: {e}")
        sys.exit(1)


def sanitize_title(title):
    """Convert title to a filename-safe format (same logic as GitHub action)."""
    # Remove all [shower-thought] tags (there might be multiple)
    title = re.sub(r'\[shower-thought\]\s*', '', title, flags=re.IGNORECASE)
    title = title.strip()
    
    # Convert to lowercase and replace spaces/special chars with dashes
    title = re.sub(r'[^\w\s-]', '', title.lower())
    title = re.sub(r'[-\s]+', '-', title)
    
    # Remove leading/trailing dashes
    title = title.strip('-')
    
    # Limit length to keep filename reasonable
    if len(title) > 50:
        title = title[:50].rstrip('-')
    
    return title


def find_repo_root():
    """Find the root of the knowledge repository."""
    current = Path.cwd()
    while current != current.parent:
        if (current / ".git").exists() and (current / "CLAUDE.md").exists():
            return current
        current = current.parent
    
    # Fallback to current directory
    return Path.cwd()


if __name__ == "__main__":
    main()