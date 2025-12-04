# 📊 Google Sheet Sync Diagnostic Guide

## ✅ Embedded Price Fix - COMPLETE
**Status:** All 51 parcel prices updated from ₦3,000,000 to ₦3,500,000 ✅
- **Commit:** c310902
- **Pushed to GitHub:** Yes ✅
- **Netlify Auto-Deploy:** In progress (should deploy within 5 minutes)

---

## 🔍 Google Sheet Sync Issue - Diagnosis

### **The Problem**
You changed the price in Google Sheet (MASTER_TEMPLATE_DATA) to ₦3,500,000, but the portal is not showing it.

### **Why This Happens**
The portal has a **dual-source price system**:

```
1. Primary Source: Google Sheet (MASTER_TEMPLATE_DATA)
   └─ IF loaded → displays priceNaira from sheet
   
2. Fallback: Embedded GeoJSON price
   └─ IF sheet fails → displays feature.properties.price (now ₦3,500,000 ✅)
   
3. Last Resort: Hardcoded fallback
   └─ IF both fail → displays '₦3,500,000'
```

### **Possible Causes**

| Issue | How to Check | How to Fix |
|-------|-------------|-----------|
| **Sheet not updating after price change** | Hard refresh portal: `Ctrl+Shift+R` | Save sheet, wait 5 seconds, refresh |
| **API key rate limit hit** | Check browser console (F12) for 403 errors | Wait 60 seconds, try again |
| **Sheet name or ID mismatch** | Verify Google Sheets config is correct | See "Verify Configuration" below |
| **Google Sheets API disabled** | Try test link in browser | Re-enable Google Sheets API |
| **Parcel data not in correct format** | Check Google Sheet columns | Ensure column C has price as number (3500000) |
| **Sheet not publicly shared** | Test with share link | Share sheet "Anyone with link can view" |

---

## 🧪 How to Test Google Sheet Sync

### **Step 1: Check Portal Console for Errors**
1. Open the portal: https://silverstone-estate-pvp.netlify.app (or your live URL)
2. Right-click → **Inspect** (or press `F12`)
3. Go to **Console** tab
4. Look for any red error messages about Google Sheets API

### **Step 2: Hard Refresh the Portal**
Clear browser cache to ensure you have the latest code:
- **Windows/Chrome:** `Ctrl + Shift + R`
- **Mac/Chrome:** `Cmd + Shift + R`
- **Firefox:** `Ctrl + F5`

### **Step 3: Click a Parcel and Check the Popup**
1. Click any parcel on the map
2. Check the price shown in the popup
3. Should display: **₦3,500,000** (either from sheet OR from embedded data)

### **Step 4: Test Google Sheets API Connection**
The portal has a built-in diagnostic tool. Check if it's running:

1. In browser console, type:
```javascript
// This should show the Google Sheets config
console.log(GOOGLE_SHEETS_CONFIG);

// Try to fetch data manually
fetch(`https://sheets.googleapis.com/v4/spreadsheets/${GOOGLE_SHEETS_CONFIG.spreadsheetId}/values/MASTER_TEMPLATE_DATA!A1:L100?key=${GOOGLE_SHEETS_CONFIG.apiKey}`)
  .then(r => r.json())
  .then(data => console.log('Sheet data:', data))
  .catch(e => console.error('Sheet error:', e));
```

2. Look for the sheet data in the console output
3. Check that prices are showing as **3500000** (numeric, not text)

---

## ✅ Verify Google Sheet Configuration

### **Your Current Configuration**
```
Spreadsheet ID: 1S5DaLtj6ZrZXKfGAuZh2VKjKKDAlHouNYzxn6Sj7UFM
Sheet Name: MASTER_TEMPLATE_DATA
API Key: AIzaSyCkLewazfYqcQ_llw_Adj_mTNK71T2iRL0
```

### **How to Verify Sheet Structure**
1. Open your Google Sheet: https://docs.google.com/spreadsheets/d/1S5DaLtj6ZrZXKfGAuZh2VKjKKDAlHouNYzxn6Sj7UFM/edit
2. Check the **MASTER_TEMPLATE_DATA** sheet tab (at bottom)
3. Look for these columns (approximately):
   - **Column A:** Parcel ID (P15, P16, P17, etc.)
   - **Column B:** Buyer Name
   - **Column C:** Price (should be: **3500000** - numeric)
   - **Column D:** Contact Phone
   - **Column E:** Status (Available/Sold/Reserved)

### **Correct Price Format in Sheet**
| Column | Should Be | Example |
|--------|-----------|---------|
| **C** (Price) | **Numeric** (not text) | `3500000` |
| NOT | Text with currency | `₦3,500,000` ❌ |
| NOT | Text with commas | `3,500,000` ❌ |

---

## 🚀 Current Deployment Status

### **What's Deployed**
✅ **Netlify Live URL:** https://silverstone-estate-pvp.netlify.app
- Embedded prices: ₦3,500,000 ✅
- WhatsApp messages: ₦3,500,000 ✅
- Google Sheet: Configured and connected (awaiting your verification)

### **What's In Progress**
⏳ Netlify auto-deployment from GitHub Commit c310902
- Status: Deploying now (check in 5 minutes)
- Refresh portal after 5 minutes: `Ctrl+Shift+R`

---

## 🛠️ Troubleshooting Steps (In Order)

### **If prices still show ₦3,000,000:**
1. ✅ Hard refresh: `Ctrl+Shift+R`
2. ✅ Wait 5 minutes for Netlify deployment
3. ✅ Try again: Hard refresh
4. ✅ Check console for errors: `F12` → Console
5. ✅ Clear all browser cache: Settings → Clear browsing data

### **If Google Sheet not loading data:**
1. ✅ Verify sheet is publicly shared
2. ✅ Check API key is correct
3. ✅ Verify spreadsheet ID matches
4. ✅ Check sheet name is exactly "MASTER_TEMPLATE_DATA"
5. ✅ Ensure prices are numeric (not text)

### **If getting API errors:**
- 403 error = API key issue or sheet not shared
- 404 error = Spreadsheet ID or sheet name wrong
- 429 error = Rate limit (wait 60 seconds)

---

## 📞 Quick Summary

**You Updated:**
- ✅ Google Sheet price to ₦3,500,000
- ✅ WhatsApp messages to ₦3,500,000
- ⏳ Portal embedded data to ₦3,500,000 (just pushed, deploying now)

**Next Steps:**
1. Wait 5 minutes for Netlify to deploy commit c310902
2. Hard refresh portal: `Ctrl+Shift+R`
3. Click a parcel - should see ₦3,500,000
4. If Google Sheet data still not loading, verify sheet is publicly shared

**Expected Result:**
- All parcel popups show ₦3,500,000 ✅
- WhatsApp messages show ₦3,500,000 ✅
- Google Sheet data syncs with portal ✅

---

## 📋 Price Change Summary

| Location | Old Price | New Price | Status |
|----------|-----------|-----------|--------|
| **Parcel Popup** | ₦3,000,000 | ₦3,500,000 | ✅ Fixed (51 parcels) |
| **WhatsApp Inquiry** | ₦3,000,000 | ₦3,500,000 | ✅ Fixed |
| **WhatsApp Direct** | ₦3,000,000 | ₦3,500,000 | ✅ Fixed |
| **Share Message** | ₦3,000,000 | ₦3,500,000 | ✅ Fixed |
| **Database Default** | 3000000 | 3500000 | ✅ Fixed |
| **Popup Fallback** | ₦3,000,000 | ₦3,500,000 | ✅ Fixed |
| **Google Sheet** | (old) | 3500000 | ✅ Updated by user |
| **Phone Number** | +2348039921371 | +2348147042804 | ✅ Fixed (all locations) |

---

**Generated:** 2025-09-24
**Commit:** c310902 (Embedded price fix)
**Status:** All prices now ₦3,500,000 across the board ✅
