import json

# Read converted subdivision data
with open('subdivision_data.json', 'r') as f:
    subdivision_data = json.load(f)

# Read the current index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Find the start of subdivisionData
start_marker = '// Embedded WGS84 GeoJSON data - SILVERSTONE ESTATE OGBEKE PARCELS'
end_marker = '};'

# Find start of subdivisionData object
start_idx = html_content.find(start_marker)
if start_idx == -1:
    # Try old marker as fallback
    start_marker = '// Embedded WGS84 GeoJSON data - Madox Mini Estate Parcels'
    start_idx = html_content.find(start_marker)

# Find the end of subdivisionData (the closing }; that matches it)
# We need to find the one that comes before "// Estates Data" or similar
estates_marker = '// Estates Data'
end_search_start = start_idx + len(start_marker)
end_search_end = html_content.find(estates_marker, end_search_start)

# Search for }; before the estates marker
last_brace = html_content.rfind('};', end_search_start, end_search_end)
if last_brace == -1:
    print("ERROR: Could not find subdivisionData end marker")
    exit(1)

# Get the end position (include the };)
end_idx = last_brace + 2

# Create the replacement text
replacement = f'''// Embedded WGS84 GeoJSON data - SILVERSTONE ESTATE OGBEKE PARCELS ({len(subdivision_data["features"])} parcels)
        const subdivisionData = {json.dumps(subdivision_data, indent=12)};'''

# Replace in HTML
html_content = html_content[:start_idx] + replacement + html_content[end_idx:]

# Write back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"✓ Successfully injected {len(subdivision_data['features'])} Silverstone parcels into index.html")
print(f"✓ Replaced Madox parcel data with exact Silverstone coordinates and boundaries")
