# 🎯 ARCHITECTURE FIX - Setup Instructions

## ✅ What I Just Fixed

**Problem:** Prices were hardcoded in GeoJSON, causing disconnect with Google Sheet updates.

**Solution:** 
- ✅ Removed all hardcoded prices from GeoJSON
- ✅ GeoJSON now contains ONLY: Geometry + Parcel ID + Area
- ✅ Google Sheet is now the SINGLE SOURCE OF TRUTH for all attributes
- ✅ Portal automatically reads from Google Sheet for prices, status, buyer info

---

## 📋 What You Need to Do

### Step 1: Rename Your Google Sheet (RECOMMENDED)

To make it distinct and avoid confusion, rename the sheet from `MASTER_TEMPLATE_DATA` to `SILVERSTONE_ESTATE_PARCELS`.

**How:**
1. Open: https://docs.google.com/spreadsheets/d/1S5DaLtj6ZrZXKfGAuZh2VKjKKDAlHouNYzxn6Sj7UFM/edit
2. At the bottom, you'll see the sheet tab labeled "MASTER_TEMPLATE_DATA"
3. Right-click on it
4. Select "Rename"
5. Type: `SILVERSTONE_ESTATE_PARCELS`
6. Click "OK" or press Enter

**Then email me the new sheet name so I can update the portal config.**

### Step 2: Verify Your Google Sheet Structure

Make sure your sheet has these columns (copy from GOOGLE_SHEET_STRUCTURE.md):

| Column | Header | Example | Format |
|--------|--------|---------|--------|
| A | ParcelID | P15 | Text |
| B | Status | available | Text (available/reserved/sold) |
| C | Buyer_Name | John Doe | Text |
| D | Contact_Phone | +2348147042804 | Text |
| E | Email_Address | john@email.com | Text |
| F | PurchaseID | PVP-001 | Text |
| G | Display_Preference | full | Text (full/first_name_only/none) |
| H | Area_SQM | 450 | Number |
| I | **Price_Naira** | 3500000 | **NUMBER** (critical!) |
| J | Sale_Date | 2025-12-04 | Date |
| K | Service_Fee_Due | 50000 | Number |
| L | Payment_Status | pending | Text (pending/paid/partial) |

**CRITICAL:** Column I must be numeric (3500000) not text ("₦3,500,000")

### Step 3: Add All 51 Parcels to Your Sheet

Your sheet should have:
- **Row 1:** Headers
- **Rows 2-52:** One row per parcel (P15, P16, P17... P118)

If you don't have all 51 parcels listed, let me create a template for you.

### Step 4: Once Done, Let Me Know

After you:
1. ✅ Rename the sheet
2. ✅ Verify column structure
3. ✅ Confirm all 51 parcels are listed

Email/message me and I'll:
1. Update the portal config with new sheet name
2. Test the connection
3. Deploy the changes

---

## 🔧 Current Architecture

```
BEFORE (Problem):
├─ GeoJSON: P15 → ₦3,500,000 (hardcoded)
├─ Google Sheet: P15 → ₦3,500,000 (separate)
└─ Portal: Uses whichever it finds first (inconsistent)

AFTER (Fixed):
├─ GeoJSON: P15 → Geometry only (no price)
├─ Google Sheet: P15 → ₦3,500,000 (single source)
└─ Portal: Always reads from Google Sheet (consistent) ✅
```

---

## 📝 Why This Matters

### Before
- Change price in Sheet → Some parcels update, some don't
- Hardcoded GeoJSON prices override Sheet data
- Difficult to maintain two sources

### After
- Change price in Sheet → ALL parcels update instantly ✅
- Only one source of data (Google Sheet)
- Easy to manage and consistent

---

## 🧪 How to Test When Done

1. Open portal: https://silverstone-estate-pvp.netlify.app
2. Click parcel P15 on the map
3. In the popup, verify:
   - ✅ Price matches your Google Sheet (₦3,500,000 or whatever you set)
   - ✅ Status matches your Google Sheet (available/reserved/sold)
   - ✅ Buyer name matches your Google Sheet (if filled in)

4. Change price in Google Sheet (Column I):
   - P15 price → 4000000
   - Save the sheet

5. Hard refresh portal: `Ctrl+Shift+R`

6. Click P15 again:
   - ✅ Should show ₦4,000,000 (from Sheet)

If prices update consistently, the fix is working! ✅

---

## 📧 What to Send Me

Once you've renamed your sheet, send me:
1. Confirmation that you renamed it to `SILVERSTONE_ESTATE_PARCELS`
2. Confirmation that all 51 parcels are in your sheet
3. Confirmation that prices are numeric in column I

Then I'll:
1. Update the portal config
2. Deploy changes to Netlify
3. Test and verify everything works

---

## 📚 Reference Files

See the following files for more details:
- `GOOGLE_SHEET_STRUCTURE.md` - Complete column reference
- `clean_geojson.py` - Script that removed hardcoded prices
- Commit: `5c80b00` - All changes documented in Git

---

**Status:** Portal architecture fixed ✅ - Now waiting for you to rename sheet and verify structure.
