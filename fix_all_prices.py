#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix all embedded parcel prices from ₦3,000,000 to ₦3,500,000
Handles Unicode escape sequences properly
"""

import re

html_file = r"c:\Users\Admin\Silverstone Estate Ogbeke\index.html"

# Read the file with UTF-8 encoding
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Count before
before_count = content.count('\\u20a63,000,000')
print(f"📊 Found {before_count} prices at \\u20a63,000,000")

# Replace the escaped Unicode pattern (two possibilities)
# Pattern 1: "\u20a63,000,000"
content = content.replace('"\\u20a63,000,000"', '"\\u20a63,500,000"')

# Also replace the literal character if it exists
content = content.replace('"₦3,000,000"', '"₦3,500,000"')

# Count after
after_count = content.count('\\u20a63,500,000') + content.count('"₦3,500,000"')
print(f"✅ Updated to {before_count} parcel prices at \\u20a63,500,000")

# Write back
with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("✨ All embedded parcel prices updated successfully!")
