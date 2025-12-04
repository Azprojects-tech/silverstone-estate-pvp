#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Update all parcel prices in subdivision_data.json from ₦3,000,000 to ₦3,500,000
"""

import json

# Read the JSON file
with open('subdivision_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Count before
before_count = 0
for feature in data['features']:
    if feature['properties']['price'] == '\u20a63,000,000' or feature['properties']['price'] == '₦3,000,000':
        before_count += 1

print(f"📊 Found {before_count} parcels with old price ₦3,000,000")

# Update all parcel prices
updated_count = 0
for feature in data['features']:
    if feature['properties']['price'] == '\u20a63,000,000' or feature['properties']['price'] == '₦3,000,000':
        feature['properties']['price'] = '\u20a63,500,000'
        updated_count += 1

# Write back
with open('subdivision_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print(f"✅ Updated {updated_count} parcel prices to ₦3,500,000")
print("✨ subdivision_data.json updated successfully!")
