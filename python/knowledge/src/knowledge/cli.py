"""CLI entry point for knowledge repository management."""

import click
from pathlib import Path
import os


@click.group()
@click.version_option()
def main():
    """Knowledge repository management CLI."""
    pass


@main.command()
def todo():
    """Manage daily todos."""
    repo_root = find_repo_root()
    todo_file = repo_root / "DAILY_TODO.md"
    
    if not todo_file.exists():
        click.echo(f"No DAILY_TODO.md found at {todo_file}")
        return
    
    click.echo(f"Opening {todo_file}")
    # You can add logic here to open in editor or process todos


@main.command()
@click.argument('name')
def task(name):
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


@main.command()
@click.argument('name')
def project(name):
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