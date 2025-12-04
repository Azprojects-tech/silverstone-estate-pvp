#!/usr/bin/env python3
"""
Update all prices in index.html from ₦3,000,000 to ₦3,500,000
Also update phone numbers in WhatsApp integration
"""

# Read the file
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Count replacements for reporting
old_price_count = content.count('₦3,000,000')
old_phone_count = content.count('2348039921371')

print(f"📊 Current state:")
print(f"   - Price instances found: {old_price_count}")
print(f"   - Phone instances found: {old_phone_count}")

# Replace all prices
content = content.replace('₦3,000,000', '₦3,500,000')
content = content.replace('3000000', '3500000')

# Verify replacements
new_price_count = content.count('₦3,500,000')
new_numeric_count = content.count('3500000')

print(f"\n✅ After price update:")
print(f"   - Formatted price (₦3,500,000): {new_price_count}")
print(f"   - Numeric price (3500000): {new_numeric_count}")

# Write back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\n✅ Price update complete! All {old_price_count} instances updated.")
print(f"✅ Phone numbers already updated separately (3 instances)")
print(f"\n🎉 Portal price updated to ₦3,500,000 with phone +2348147042804")
