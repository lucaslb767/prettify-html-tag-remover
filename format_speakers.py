#!/usr/bin/env python3
"""
Speaker Formatter for Transcripts
Formats transcript text to have one speaker per line.
"""

import sys
import re
from pathlib import Path

def format_speakers(text):
    """
    Format transcript text to have one speaker per line.
    
    Args:
        text (str): The transcript text
        
    Returns:
        str: Formatted text with one speaker per line
    """
    # Split into lines first
    lines = text.strip().split('\n')
    formatted_lines = []
    
    for line in lines:
        # Skip empty lines
        if not line.strip():
            continue
            
        # Find all speaker patterns in the line (timestamp + name + colon)
        # Pattern: MM:SS Name: or HH:MM:SS Name:
        speaker_pattern = r'(\d{1,2}:\d{2}(?::\d{2})?\s+[^:]+:)'
        
        # Split the line by speaker patterns while keeping the separators
        parts = re.split(f'({speaker_pattern})', line)
        
        current_speaker_line = ""
        
        for part in parts:
            if not part.strip():
                continue
                
            # Check if this part is a speaker pattern
            if re.match(speaker_pattern, part.strip()):
                # If we have accumulated text for previous speaker, save it
                if current_speaker_line.strip():
                    formatted_lines.append(current_speaker_line.strip())
                
                # Start new speaker line
                current_speaker_line = part.strip()
            else:
                # Add content to current speaker line
                current_speaker_line += " " + part.strip()
        
        # Add the last speaker line if it exists
        if current_speaker_line.strip():
            formatted_lines.append(current_speaker_line.strip())
    
    return '\n'.join(formatted_lines)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 format_speakers.py <input_file>")
        sys.exit(1)
    
    input_file = Path(sys.argv[1])
    
    if not input_file.exists():
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)
    
    try:
        # Read the input file
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Format the speakers
        formatted_content = format_speakers(content)
        
        # Create output filename
        output_file = input_file.with_name(f"{input_file.stem}_formatted{input_file.suffix}")
        
        # Write formatted content to output file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(formatted_content)
        
        print(f"Speakers formatted successfully!")
        print(f"Output saved to: {output_file}")
        
    except Exception as e:
        print(f"Error processing file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()