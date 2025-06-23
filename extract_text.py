#!/usr/bin/env python3
"""
HTML Text Extractor
Extracts plain text content from HTML files by removing all HTML tags.
"""

import sys
import re
from pathlib import Path

def extract_text_from_html(html_content):
    """
    Extract plain text from HTML content by removing all HTML tags.
    
    Args:
        html_content (str): The HTML content as a string
        
    Returns:
        str: Plain text with HTML tags removed
    """
    # Remove HTML tags using regex
    clean_text = re.sub(r'<[^>]+>', '', html_content)
    
    # Decode HTML entities
    html_entities = {
        '&amp;': '&',
        '&lt;': '<',
        '&gt;': '>',
        '&quot;': '"',
        '&apos;': "'",
        '&nbsp;': ' ',
        '&#39;': "'",
        '&hellip;': '...',
        '&mdash;': '—',
        '&ndash;': '–',
        '&rsquo;': "'",
        '&lsquo;': "'",
        '&rdquo;': '"',
        '&ldquo;': '"'
    }
    
    for entity, char in html_entities.items():
        clean_text = clean_text.replace(entity, char)
    
    # Clean up whitespace
    clean_text = re.sub(r'\s+', ' ', clean_text.strip())
    
    return clean_text

def main():
    if len(sys.argv) != 2:
        print("Usage: python extract_text.py <input_html_file>")
        sys.exit(1)
    
    input_file = Path(sys.argv[1])
    
    if not input_file.exists():
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)
    
    try:
        # Read the HTML file
        with open(input_file, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Extract text content
        text_content = extract_text_from_html(html_content)
        
        # Create output filename
        output_file = input_file.with_suffix('.txt')
        
        # Write extracted text to output file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(text_content)
        
        print(f"Text extracted successfully!")
        print(f"Output saved to: {output_file}")
        
    except Exception as e:
        print(f"Error processing file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()