#!/usr/bin/env python
"""
Post-generation hook to set up the searchable directory structure.
Creates directory junctions (Windows) or symlinks (Unix) for unified searching.
"""
import os
import sys
import subprocess
from pathlib import Path

def is_windows():
    return os.name == 'nt'

def create_directory_link(source, target):
    """Create a directory link (junction on Windows, symlink on Unix)"""
    source_path = Path(source).resolve()
    target_path = Path(target)
    
    # Create parent directory if it doesn't exist
    target_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Remove target if it already exists
    if target_path.exists() or target_path.is_symlink():
        if target_path.is_dir():
            if is_windows():
                subprocess.run(['rmdir', str(target_path)], shell=True, capture_output=True)
            else:
                target_path.rmdir()
        else:
            target_path.unlink()
    
    try:
        if is_windows():
            # Use mklink /J for directory junctions on Windows
            result = subprocess.run([
                'mklink', '/J', str(target_path), str(source_path)
            ], shell=True, capture_output=True, text=True)
            
            if result.returncode != 0:
                print(f"Warning: Could not create junction from {target_path} to {source_path}")
                print(f"Error: {result.stderr}")
                return False
        else:
            # Use symlinks on Unix systems
            target_path.symlink_to(source_path)
        
        print(f"Created link: {target_path} -> {source_path}")
        return True
        
    except Exception as e:
        print(f"Warning: Could not create link from {target_path} to {source_path}: {e}")
        return False

def setup_searchable_directory():
    """Set up the searchable directory with links to all content directories"""
    project_dir = Path.cwd()
    
    # Only create searchable links if the option is enabled
    include_searchable = '{{ cookiecutter.include_searchable_links }}'.lower() == 'true'
    if not include_searchable:
        print("Skipping searchable directory setup (disabled in config)")
        return
    
    thoughts_dir = project_dir / 'thoughts'
    searchable_dir = thoughts_dir / 'searchable'
    
    # Create searchable directory
    searchable_dir.mkdir(parents=True, exist_ok=True)
    
    # Define the directories to link
    directories_to_link = [
        ('shared', thoughts_dir / 'shared'),
        ('{{ cookiecutter.username }}', thoughts_dir / '{{ cookiecutter.username }}'),
        ('global', thoughts_dir / 'global')
    ]
    
    # Only include global if enabled
    if '{{ cookiecutter.include_global_directory }}'.lower() != 'true':
        directories_to_link = [d for d in directories_to_link if d[0] != 'global']
    
    # Create links
    successful_links = 0
    for link_name, source_dir in directories_to_link:
        if source_dir.exists():
            target_link = searchable_dir / link_name
            if create_directory_link(source_dir, target_link):
                successful_links += 1
    
    print(f"Searchable directory setup complete: {successful_links} links created")
    
    if successful_links == 0 and is_windows():
        print("\nNote: If you're on Windows and seeing permission errors,")
        print("you may need to run as Administrator to create directory junctions.")
        print("Alternatively, you can create the links manually later.")

def setup_git_repository():
    """Initialize git repository if sync method is git"""
    if '{{ cookiecutter.sync_method }}'.lower() != 'git':
        return
    
    project_dir = Path.cwd()
    
    # Check if already a git repository
    if (project_dir / '.git').exists():
        print("Git repository already exists")
        return
    
    try:
        # Initialize git repository
        subprocess.run(['git', 'init'], cwd=project_dir, check=True, capture_output=True)
        subprocess.run(['git', 'add', '.'], cwd=project_dir, check=True, capture_output=True)
        subprocess.run([
            'git', 'commit', '-m', 'Initial commit: {{cookiecutter.project_name}}'
        ], cwd=project_dir, check=True, capture_output=True)
        
        print("Git repository initialized")
        
        # Set up remote if URL is provided
        repo_url = '{{ cookiecutter.shared_repo_url }}'
        if repo_url and repo_url != 'https://github.com/your-org/thoughts':
            subprocess.run([
                'git', 'remote', 'add', 'origin', repo_url
            ], cwd=project_dir, check=True, capture_output=True)
            print(f"Remote origin set to: {repo_url}")
        
    except subprocess.CalledProcessError as e:
        print(f"Warning: Could not set up git repository: {e}")
    except FileNotFoundError:
        print("Warning: Git not found in PATH. Skipping git setup.")

def main():
    """Main post-generation setup"""
    print("Setting up {{cookiecutter.project_name}}...")
    
    # Set up searchable directory
    setup_searchable_directory()
    
    # Set up git repository
    setup_git_repository()
    
    print("\n[SUCCESS] {{cookiecutter.project_name}} setup complete!")
    print("\nNext steps:")
    print("1. Review the generated structure")
    print("2. Customize the README.md if needed")
    print("3. Add your first thoughts documents")
    
    if '{{ cookiecutter.include_sync_scripts }}'.lower() == 'true':
        print("4. Use the sync scripts to keep thoughts synchronized")
    
    project_root = '{{ cookiecutter.project_root }}'.replace('\\', '/')
    default_root = 'C:/Users/vaski/projects'
    if project_root and project_root != default_root:
        print(f"\nNote: Update your project root setting if {project_root} is incorrect")

if __name__ == '__main__':
    main()