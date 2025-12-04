#!/usr/bin/env python3
"""
Fix EMBEDDED PARCEL PRICES in index.html
This updates all 51 parcel price entries from ₦3,000,000 to ₦3,500,000
"""

# Read the file
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Count current prices
old_price_count = content.count('"price": "₦3,000,000"')
print(f"📊 Found {old_price_count} embedded parcel prices at ₦3,000,000")

# Replace ALL embedded parcel prices
content = content.replace('"price": "₦3,000,000"', '"price": "₦3,500,000"')

# Verify
new_price_count = content.count('"price": "₦3,500,000"')
print(f"✅ Updated to {new_price_count} parcel prices at ₦3,500,000")

# Write back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\n✅ SUCCESS! All {old_price_count} parcel prices updated!")
print(f"   When you click parcels on the map, they will now show ₦3,500,000")
