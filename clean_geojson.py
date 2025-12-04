#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Clean the GeoJSON - remove hardcoded prices/status
Keep ONLY: Parcel ID, area, and geometry
Prices and status will come from Google Sheet
"""

import json

# Read the current GeoJSON
with open('subdivision_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"📊 Processing {len(data['features'])} parcels...")

# Clean each feature - keep only essential properties
cleaned_count = 0
for feature in data['features']:
    props = feature['properties']
    
    # Keep only: Text (parcel ID) and area
    # Remove: price, status (these come from Google Sheet)
    original_price = props.get('price', 'N/A')
    original_status = props.get('status', 'N/A')
    
    # Create new properties with only essential data
    feature['properties'] = {
        'Text': props.get('Text', ''),
        'Shape_Area': props.get('Shape_Area', 0),
        'area': props.get('area', '450 sqm')
    }
    
    cleaned_count += 1
    if cleaned_count <= 3:
        print(f"  • {props['Text']}: Removed price ({original_price}), status ({original_status})")

# Write cleaned version
with open('subdivision_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print(f"\n✅ Cleaned {cleaned_count} parcels")
print("✨ Removed all hardcoded prices and status from GeoJSON")
print("📊 Prices and status will now come from Google Sheet only")
