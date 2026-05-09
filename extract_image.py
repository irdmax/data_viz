#!/usr/bin/env python3
"""
Extract and display the base64-encoded image from biennale_poster_source.html
"""
import re
import base64
from pathlib import Path

def extract_and_save_image():
    """Extract the base64 image from HTML and save as PNG"""
    # Read the HTML file
    html_file = Path('biennale_poster_source.html')
    
    if not html_file.exists():
        print(f"Error: HTML file not found: {html_file}")
        return False
    
    try:
        html_content = html_file.read_text()
    except Exception as e:
        print(f"Error reading HTML file: {e}")
        return False
    
    # Find the base64 image data using regex
    # Looking for: href="data:image/png;base64,..."
    pattern = r'href="data:image/png;base64,([^"]+)"'
    match = re.search(pattern, html_content)
    
    if not match:
        print("Error: Could not find base64 image data in HTML file")
        return False
    
    # Get the base64 data
    base64_data = match.group(1)
    
    # Decode base64 to binary
    try:
        image_data = base64.b64decode(base64_data)
    except base64.binascii.Error as e:
        print(f"Error decoding base64 data: {e}")
        return False
    
    # Save as PNG file
    output_file = Path('world_map.png')
    output_file.write_bytes(image_data)
    
    print(f"✓ Successfully extracted and saved image to: {output_file}")
    print(f"  Image size: {len(image_data):,} bytes")
    
    return True

if __name__ == '__main__':
    success = extract_and_save_image()
    if success:
        print("\nYou can now view the image:")
        print("  - Open world_map.png in an image viewer")
        print("  - Or open biennale_poster_source.html in a web browser")
