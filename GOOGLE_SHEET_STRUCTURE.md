# 📊 Google Sheet Structure for Silverstone Estate PVP

## Current Setup

**Sheet Name:** `MASTER_TEMPLATE_DATA`
**Spreadsheet ID:** `1S5DaLtj6ZrZXKfGAuZh2VKjKKDAlHouNYzxn6Sj7UFM`
**URL:** https://docs.google.com/spreadsheets/d/1S5DaLtj6ZrZXKfGAuZh2VKjKKDAlHouNYzxn6Sj7UFM/edit

---

## How It Works Now (FIXED)

### GeoJSON (Geometry Only)
- **File:** `subdivision_data.json` & embedded in `index.html`
- **Contains:** Parcel coordinates (polygon geometry) + Parcel ID + Area only
- **Does NOT contain:** Prices, status, buyer info

### Google Sheet (Data Source)
- **File:** MASTER_TEMPLATE_DATA sheet
- **Purpose:** Single source of truth for all parcel attributes
- **Portal reads:** Columns A-L when parcel is clicked

### Portal Logic (Merged)
1. Load GeoJSON for map geometry
2. Fetch Google Sheet for all attributes
3. Merge: Geometry + Data from Sheet
4. Display merged data in popup

---

## Google Sheet Column Structure

**Row 1:** HEADERS (do not change)
**Rows 2+:** One row per parcel

| Column | Letter | Field | Example | Notes |
|--------|--------|-------|---------|-------|
| **1** | A | ParcelID | P15 | Must match GeoJSON parcel IDs |
| **2** | B | Status | available | Options: available, reserved, sold |
| **3** | C | Buyer_Name | John Doe | Only if sold/reserved |
| **4** | D | Contact_Phone | +2348147042804 | Buyer contact number |
| **5** | E | Email_Address | john@email.com | Buyer email |
| **6** | F | PurchaseID | PVP-001 | Transaction ID |
| **7** | G | Display_Preference | full | Options: full, first_name_only, none |
| **8** | H | Area_SQM | 450 | Size in square meters |
| **9** | I | Price_Naira | 3500000 | **NUMERIC** (not text, no currency symbol) |
| **10** | J | Sale_Date | 2025-12-04 | Format: YYYY-MM-DD |
| **11** | K | Service_Fee_Due | 50000 | **NUMERIC** |
| **12** | L | Payment_Status | pending | Options: pending, paid, partial |

---

## How Portal Uses This Data

### When User Clicks a Parcel:

```javascript
// Portal fetches Google Sheet
GET https://sheets.googleapis.com/v4/spreadsheets/{ID}/values/MASTER_TEMPLATE_DATA!A2:L

// For parcel P15 (from row 2):
// A2 = "P15"           → Parcel ID to match
// B2 = "available"     → Color code on map (green, yellow, red)
// C2 = "John Doe"      → Show buyer name in popup
// D2 = "+234..."       → Show contact in popup
// I2 = "3500000"       → Show price in popup (formatted as ₦3,500,000)
// J2 = "2025-12-04"    → Show purchase date in popup
// G2 = "full"          → Determine what buyer info to display
```

### Portal Display:
```
Parcel P15
━━━━━━━━━━━━━━━━━━━
Status: Available ✅
Area: 450 sqm
Price: ₦3,500,000
Buyer: John Doe
Contact: +234 814 704 2804
Purchase Date: 2025-12-04
```

---

## Current Issue: Disconnect

### Problem
Some parcels update from Google Sheet, some don't.

### Root Causes
1. **ParcelID mismatch** - Sheet has "P15" but portal looks for "p15" (case sensitivity)
2. **Wrong column** - Price in wrong column (should be column I)
3. **Text format** - Price as text "3,500,000" instead of number 3500000
4. **Sheet not refreshing** - Portal cached old data

### Solution
1. ✅ Removed hardcoded prices from GeoJSON
2. ✅ Portal now ONLY reads from Google Sheet for prices/status
3. 📋 You need to verify Google Sheet column structure

---

## RECOMMENDED: Rename Your Sheet

To make it distinct and avoid confusion, rename:
- **FROM:** `MASTER_TEMPLATE_DATA`
- **TO:** `SILVERSTONE_ESTATE_PARCELS`

**How to rename in Google Sheets:**
1. Right-click on sheet tab at bottom
2. Select "Rename"
3. Type: `SILVERSTONE_ESTATE_PARCELS`
4. Click "OK"

Then update this one line in `index.html` (line ~4409):
```javascript
const GOOGLE_SHEETS_CONFIG = {
    spreadsheetId: '1S5DaLtj6ZrZXKfGAuZh2VKjKKDAlHouNYzxn6Sj7UFM',
    apiKey: 'AIzaSyCkLewazfYqcQ_llw_Adj_mTNK71T2iRL0',
    sheetName: 'SILVERSTONE_ESTATE_PARCELS',  // ← Change this line
    sheetUrl: '...'
};
```

---

## Verification Checklist

- [ ] Sheet name updated to: `SILVERSTONE_ESTATE_PARCELS`
- [ ] Column A: ParcelID (P15, P16, P17, ... P45, etc.)
- [ ] Column B: Status (available/reserved/sold)
- [ ] Column I: Price_Naira (numeric: 3500000, not text)
- [ ] All 51 parcels listed (rows 2-52)
- [ ] No spaces before/after ParcelID
- [ ] API Key still valid and sheet is publicly shared

---

## How to Test

1. **Make a test change in Google Sheet:**
   - Change P15 status from "available" to "reserved"
   - Change P15 price to "4000000"
   - Save the sheet

2. **Hard refresh portal:**
   - Press: `Ctrl+Shift+R` (Windows) or `Cmd+Shift+R` (Mac)

3. **Click P15 parcel:**
   - Should show status: Reserved (yellow color)
   - Should show price: ₦4,000,000

4. **Check browser console:**
   - Right-click → Inspect → Console tab
   - Should see: `📋 Public parcel data loaded: 51 parcels`
   - No error messages

---

## Next Steps

1. Rename the Google Sheet (optional but recommended)
2. Verify all parcel IDs match between Sheet and GeoJSON
3. Verify Price column (I) has numeric values only
4. Hard refresh portal and test one parcel update
5. Let me know if updates work consistently

---

**Status:** Portal now uses ONLY Google Sheet for prices/status ✅
**Architecture:** GeoJSON = Geometry | Google Sheet = Attributes ✅
