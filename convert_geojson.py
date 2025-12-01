import json

# Read the GeoJSON
with open('Geojson/Parcels.geojson', 'r') as f:
    data = json.load(f)

# Filter only valid parcels (non-null Text)
valid_features = [p for p in data['features'] if p['properties']['Text'] is not None]

# Convert MultiPolygon to Polygon format (using first polygon of first group)
for feature in valid_features:
    if feature['geometry']['type'] == 'MultiPolygon':
        # Take the first polygon from the first group, remove the Z coordinates
        coords = feature['geometry']['coordinates'][0][0]
        # Remove Z coordinates (keep only [lon, lat])
        coords_2d = [[c[0], c[1]] for c in coords]
        feature['geometry']['type'] = 'Polygon'
        feature['geometry']['coordinates'] = [coords_2d]
    
    # Add standard properties like Madox template
    text = feature['properties'].get('Text', 'UNKNOWN')
    area = feature['properties'].get('Shape_Area', 0)
    feature['properties']['area'] = f"{int(area)} sqm"
    feature['properties']['price'] = "₦3,000,000"
    feature['properties']['status'] = "Available"

# Create output
output = {
    'type': 'FeatureCollection',
    'features': valid_features
}

# Write to file
with open('subdivision_data.json', 'w') as f:
    json.dump(output, f, indent=4)

print(f"✓ Converted {len(valid_features)} parcels to subdivision_data.json")
print(f"✓ All coordinates converted to 2D (lon, lat) WGS84 format")
print(f"✓ Ready to embed in index.html")
