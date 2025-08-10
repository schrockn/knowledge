#!/usr/bin/env python3

import os
import re
from datetime import datetime

def sanitize_title(title):
    """Convert issue title to a filename-safe format."""
    # Remove [shower-thought] prefix
    title = re.sub(r'\[shower-thought\]\s*', '', title, flags=re.IGNORECASE)
    
    # Convert to lowercase and replace spaces/special chars with dashes
    title = re.sub(r'[^\w\s-]', '', title.lower())
    title = re.sub(r'[-\s]+', '-', title)
    
    # Remove leading/trailing dashes
    title = title.strip('-')
    
    # Limit length to keep filename reasonable
    if len(title) > 50:
        title = title[:50].rstrip('-')
    
    return title

def main():
    issue_title = os.environ.get('ISSUE_TITLE', '')
    issue_body = os.environ.get('ISSUE_BODY', '')
    issue_number = os.environ.get('ISSUE_NUMBER', '')
    
    if not issue_title:
        print("No issue title found")
        return
    
    # Generate filename
    sanitized_title = sanitize_title(issue_title)
    current_date = datetime.now().strftime('%Y-%m-%d')
    filename = f"{sanitized_title}-{current_date}.md"
    
    # Ensure shower-thoughts directory exists
    os.makedirs('shower-thoughts', exist_ok=True)
    
    # Create file path
    filepath = os.path.join('shower-thoughts', filename)
    
    # Check if file already exists, add counter if needed
    counter = 1
    original_filepath = filepath
    while os.path.exists(filepath):
        name, ext = os.path.splitext(original_filepath)
        filepath = f"{name}-{counter}{ext}"
        counter += 1
    
    # Write the content
    content = issue_body.strip() if issue_body else issue_title.replace('[shower-thought]', '').strip()
    
    with open(filepath, 'w') as f:
        f.write(content)
    
    print(f"Created shower thought: {filepath}")

if __name__ == '__main__':
    main()