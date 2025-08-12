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


@main.command()
@click.argument('thought')
def shower_thought(thought):
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


@main.command()
@click.option('--check', is_flag=True, help='Check if files need formatting (exit with non-zero if changes needed)')
@click.option('--write', is_flag=True, default=True, help='Write changes to files (default: True)')
def lint(check, write):
    """Format markdown files using prettier."""
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
    
    click.echo(f"Found {len(md_files)} markdown files to format")
    
    # Prepare pnpm dlx prettier command
    cmd = ['pnpm', 'dlx', 'prettier']
    
    if check and not write:
        cmd.append('--check')
    elif not check and write:
        cmd.append('--write')
    else:
        # Default behavior: write changes
        cmd.append('--write')
    
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
            if check:
                click.echo("Some files need formatting. Run 'knowledge lint' to fix them.")
            else:
                click.echo("Prettier encountered an error")
            sys.exit(result.returncode)
        else:
            if check:
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