#!/usr/bin/env python3

import os
import re
from datetime import datetime

def sanitize_title(title):
    """Convert issue title to a filename-safe format."""
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

def main():
    issue_title = os.environ.get('ISSUE_TITLE', '')
    issue_body = os.environ.get('ISSUE_BODY', '')
    issue_number = os.environ.get('ISSUE_NUMBER', '')
    
    if not issue_title:
        print("No issue title found")
        return
    
    # Parse title and body from the email subject (issue title) and email body (issue body)
    # Email subject format: "Shower Thought - YYYY-MM-DD HH:MM [shower-thought]"
    # We need to get the actual content from the email body
    email_content = issue_body.strip() if issue_body else issue_title.replace('[shower-thought]', '').strip()
    
    if ':' in email_content:
        title_part, body_part = email_content.split(':', 1)
        title_part = title_part.strip()
        body_part = body_part.strip()
    else:
        title_part = email_content
        body_part = ''
    
    # Generate filename from the parsed title
    sanitized_title = sanitize_title(title_part)
    current_date = datetime.now().strftime('%Y-%m-%d')
    filename = f"{sanitized_title}-{current_date}.md"
    
    # Ensure shower-thoughts directory exists
    os.makedirs('base/shower-thoughts', exist_ok=True)
    
    # Create file path
    filepath = os.path.join('base/shower-thoughts', filename)
    
    # Check if file already exists, add counter if needed
    counter = 1
    original_filepath = filepath
    while os.path.exists(filepath):
        name, ext = os.path.splitext(original_filepath)
        filepath = f"{name}-{counter}{ext}"
        counter += 1
    
    # Write the content (use body if available, otherwise title)
    content = body_part if body_part else title_part
    
    with open(filepath, 'w') as f:
        f.write(content)
    
    print(f"Created shower thought: {filepath}")
    print(f'Title: "{title_part}"')
    print(f'Body: "{body_part}"')

if __name__ == '__main__':
    main()