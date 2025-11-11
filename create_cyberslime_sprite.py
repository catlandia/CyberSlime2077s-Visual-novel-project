#!/usr/bin/env python3
"""Create a placeholder CyberSlime2077 character sprite"""

import os

# Create images/characters directory if it doesn't exist
os.makedirs('game/images/characters', exist_ok=True)

# Create a simple placeholder PNG (green rectangle representing CyberSlime2077)
# This is a minimal PNG file
with open('game/images/characters/cyberslime.png', 'wb') as f:
    # PNG signature
    f.write(b'\x89PNG\r\n\x1a\n')
    # IHDR chunk (400x600 image, RGBA)
    f.write(b'\x00\x00\x00\rIHDR\x00\x00\x01\x90\x00\x00\x02X\x08\x06\x00\x00\x00\x8e\x1d\x1f\x8d')
    # IDAT chunk (green rectangle)
    # Using a simple green color fill
    f.write(b'\x00\x00\x00\x0cIDATx\x9cc\xf8\x0f\xc4\x00\x00\x03\xfe\x01\xff\x9e\xdd\x88\x7f')
    # IEND chunk
    f.write(b'\x00\x00\x00\x00IEND\xaeB`\x82')

print("Created placeholder CyberSlime2077 sprite!")
print("Location: game/images/characters/cyberslime.png")
print("\nReplace this with your actual CyberSlime2077.png when ready!")
