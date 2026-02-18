# Parcel Vision Pro (PVP) Portal Setup Guide
**Version 1.0** | Last Updated: February 18, 2026

---

## 📋 QUICK REFERENCE

### Current Working Portals
| Portal | URL | Sheet ID | API Key | Email Owner |
|--------|-----|----------|---------|-------------|
| **Silverstone Estate** | https://jeff-realty-silverstone.netlify.app | `1S5DaLtj6ZrZXKfGAuZh2VKjKKDAlHouNYzxn6Sj7UFM` | `AIzaSyCkLewazfYqcQ_llw_Adj_mTNK71T2iRL0` | azprojectslimited@gmail.com |
| **Pineleaf Estate** | https://pineleaf-estates.netlify.app | `1S5DaLtj6ZrZXKfGAuZh2VKjKKDAlHouNYzxn6Sj7UFM` | `AIzaSyCkLewazfYqcQ_llw_Adj_mTNK71T2iRL0` | azprojectslimited@gmail.com |

---

## 🐛 ISSUES ENCOUNTERED & SOLUTIONS

### Issue 1: `ReferenceError: Cannot access 'GOOGLE_SHEETS_CONFIG' before initialization` ❌

**Problem:**
- Variable used before definition
- Code tried to access `GOOGLE_SHEETS_CONFIG` in class constructors before it was declared

**Location in Code:**
```javascript
// WRONG - Using before declaring
const territoryMgr = new TerritoryManager(GOOGLE_SHEETS_CONFIG.spreadsheetId, ...);
const GOOGLE_SHEETS_CONFIG = { ... }; // Declared AFTER use
```

**Solution:**
- Move `GOOGLE_SHEETS_CONFIG` declaration **BEFORE** all class instantiations
- Find line starting with `const GOOGLE_SHEETS_CONFIG`
- Move it to the TOP of the initialization section (right after class definitions)

**Code Fix:**
```javascript
// RIGHT - Declare FIRST
const GOOGLE_SHEETS_CONFIG = {
    spreadsheetId: '...',
    apiKey: '...',
    sheetName: '...',
    sheetUrl: '...'
};

// THEN use it
const territoryMgr = new TerritoryManager(GOOGLE_SHEETS_CONFIG.spreadsheetId, ...);
```

---

### Issue 2: HTTP 403 Forbidden When Syncing ❌

**Root Cause:**
API Key was restricted to ONLY allow ONE domain (Pineleaf), so Silverstone couldn't access

**Problem Details:**
- API Key has **Domain Restrictions** enabled
- Pineleaf portal was listed: `https://pineleaf-estates.netlify.app/*`
- Silverstone portal was NOT listed
- Result: Google blocks Silverstone's requests = 403 Forbidden

**Solution Steps:**

1. **Go to Google Cloud Console:**
   - https://console.cloud.google.com/apis/credentials

2. **Find your API Key:**
   - Look for: `Parcel-Vision-Pro-API-Key`
   - Click on it to edit

3. **Add new domain restriction:**
   - Find **"API restrictions"** section → **"Website"**
   - Click **Edit** (pencil icon)
   - Add new line: `https://YOUR-NEW-PORTAL.netlify.app/*`
   - Include the `/*` at the end (allows all paths)

4. **Save changes**
   - Wait 2-5 minutes for Google to apply
   - Refresh the portal in browser

**Example - Both Portals Allowed:**
```
Website restrictions:
- https://pineleaf-estates.netlify.app/*
- https://jeff-realty-silverstone.netlify.app/*
- https://your-new-portal.netlify.app/*
```

---

### Issue 3: Sheet Name vs File Name Confusion ❌

**The Confusion:**
- **File name** (top of Google Sheets): `MASTER_TEMPLATE_DATA`
- **Sheet tab name** (bottom, left of sheet): `SILVERSTONE_ESTATE_PARCELS`
- Code uses the **SHEET TAB NAME**, not the file name!

**Correct Configuration:**
```javascript
const GOOGLE_SHEETS_CONFIG = {
    spreadsheetId: '1S5DaLtj...',
    apiKey: 'AIzaSyCk...',
    sheetName: 'SILVERSTONE_ESTATE_PARCELS', // ✅ SHEET TAB name (NOT file name)
    ...
};
```

**How to verify:**
1. Open your Google Sheet
2. Look at the bottom where it shows sheet tabs
3. Find the tab you want to use
4. Right-click → "Rename" to see the EXACT name
5. Use that exact name in `sheetName: '...'` (case-sensitive!)

---

## 📊 COLUMN STRUCTURE IN GOOGLE SHEETS

Your `MASTER_TEMPLATE_DATA` sheet should have these columns:

| Col | Name | Type | Example | Notes |
|-----|------|------|---------|-------|
| A | ParcelID | Text | P71, P70, P69 | Unique identifier |
| B | Status | Dropdown | Available, Reserved, Sold | Color-coded on map |
| C | Purchaser_Name | Text | Anya N, Offer I A | Buyer name |
| D | Phone_Number | Text | 2348164532286 | Contact phone |
| E | Email_Address | Text | email@domain.com | Contact email |
| F | Purchase_ID | Text | UD_2024 | Purchase reference |
| G | Display_Preference | Dropdown | none, name, purchase_id | Privacy setting |
| H | Area_SqM | Number | 450, 500 | Land area |
| I | Price_Naira | Number | 3500000 | Sale price |
| J | Sale_Date | Date | 2024-02-20 | Transaction date |
| K | Service_Fee_Due | Number | 81000 | Fee amount |
| L | Payment_Status | Dropdown | pending, paid | Payment status |

**Important:**
- Column A MUST have ParcelID
- Column B MUST have Status (controls map colors)
- Headers are flexible - code auto-detects columns
- Missing data = portal uses defaults (3.5M price, 450 sqm area)

---

## 🔧 HOW TO CREATE A NEW PORTAL (TEMPLATE)

### Step 1: Prepare Your Data
```
1. Create new Google Sheet or duplicate existing
2. Name the file: MASTER_TEMPLATE_DATA (or your choice)
3. Name the sheet tab: YOUR_ESTATE_PARCELS (case-sensitive!)
4. Add all your parcel data with columns A-L
5. Share: File → Share → "Anyone with link" → Viewer access
```

### Step 2: Set Up GitHub Repository
```bash
# Option A: Clone Silverstone as template
git clone https://github.com/Azprojects-tech/silverstone-estate-pvp.git YourEstateName
cd YourEstateName
git remote set-url origin https://github.com/Azprojects-tech/your-new-repo.git
git push -u origin main

# Option B: Create fresh repo with index.html
# (Ask for the current Silverstone index.html as template)
```

### Step 3: Update Configuration in index.html

**Find these lines (around line 4553):**
```javascript
const GOOGLE_SHEETS_CONFIG = {
    spreadsheetId: '1S5DaLtj6ZrZXKfGAuZh2VKjKKDAlHouNYzxn6Sj7UFM', // ← Change this
    apiKey: 'AIzaSyCkLewazfYqcQ_llw_Adj_mTNK71T2iRL0',             // Keep same (shared key)
    sheetName: 'SILVERSTONE_ESTATE_PARCELS',                       // ← Change this
    sheetUrl: 'https://docs.google.com/spreadsheets/d/1S5DaLtj...' // ← Change this
};
```

**Get your Spreadsheet ID:**
- Open your Google Sheet
- URL: `https://docs.google.com/spreadsheets/d/COPY-THIS-PART-HERE/edit`
- Copy the long ID between `/d/` and `/edit`

### Step 4: Add Portal to API Key Restrictions
```
1. Go: https://console.cloud.google.com/apis/credentials
2. Click: Parcel-Vision-Pro-API-Key
3. Scroll: API restrictions → Website → Edit
4. Add: https://your-new-portal.netlify.app/*
5. Save
6. Wait 2-5 minutes
```

### Step 5: Deploy to Netlify
```
1. Create new Netlify site
2. Connect your GitHub repo
3. Netlify auto-deploys on every git push
4. Set up custom domain
5. Done! 🚀
```

---

## 🎨 CUSTOMIZATION POINTS

### Header/Title
**Line ~501:**
```html
<title>YOUR_ESTATE_NAME - Real Estate Mapper</title>
```

### Main Heading
**Line ~1169:**
```html
<h1>YOUR_ESTATE_NAME</h1>
```

### WhatsApp Contact Number
**Line ~4061 & ~4079:**
```javascript
const whatsappMessage = `... 📞 Contact us: +234 YOUR_NUMBER ...`;
```

### Admin Password
**Line ~4303:**
```javascript
const CLIENT_PASSWORD = 'change_this_password';
```

### Footer Contact Info
**Bottom of file:**
```html
<span>Your Company | Phone: +234... | Email: info@...</span>
```

---

## ✅ DEPLOYMENT CHECKLIST

Before pushing to production:

- [ ] **Google Sheet**
  - [ ] Sheet is publicly shared ("Anyone with link" → Viewer)
  - [ ] Sheet name matches code (case-sensitive)
  - [ ] Data is complete (all parcels, statuses, prices)
  - [ ] Headers match expected columns

- [ ] **Code Configuration**
  - [ ] GOOGLE_SHEETS_CONFIG spreadsheetId is correct
  - [ ] sheetName matches your sheet tab name exactly
  - [ ] API key can access the sheet (test in console first)
  - [ ] Title and headings updated to estate name
  - [ ] Contact numbers updated
  - [ ] Admin password changed

- [ ] **API Key Setup**
  - [ ] Google Sheets API is ENABLED in Cloud Console
  - [ ] Portal URL added to API key restrictions
  - [ ] Restrictions properly formatted: `https://domain.netlify.app/*`
  - [ ] 5+ minutes waited after making changes

- [ ] **GitHub & Netlify**
  - [ ] Code pushed to GitHub main branch
  - [ ] Netlify auto-deploy completed (check build logs)
  - [ ] Portal loads without console errors
  - [ ] Parcels display with colors
  - [ ] Sync button works and fetches data

- [ ] **Testing**
  - [ ] Open portal, parcels should appear colored
  - [ ] Click "Admin" → enter password
  - [ ] Click "Admin Sync" button
  - [ ] Console should show "✅ Public parcel statuses updated"
  - [ ] Map colors should reflect Google Sheets data

---

## 🚨 COMMON ERRORS & FIXES

| Error | Cause | Fix |
|-------|-------|-----|
| **403 Forbidden** | Domain not in API restrictions | Add `https://your-portal.netlify.app/*` to Google Cloud Console |
| **ReferenceError: Cannot access X before initialization** | Variable used before declared | Move declaration to top of script section |
| **Parcels not loading** | Wrong sheet name or ID | Verify against Google Sheet URL and tab names |
| **Sync button does nothing** | Google Sheets API not enabled | Enable in Google Cloud Console → APIs & Services |
| **Console shows 404** | Sheet/range doesn't exist | Check sheet name spelling (case-sensitive) |
| **Blank page** | HTML syntax error | Check browser console for JavaScript errors |

---

## 📞 SUPPORT CONTACTS

- **Silverstone Estate:** +234 814 704 2804
- **A&Z Projects:** azprojectslimited@gmail.com
- **Google Cloud Support:** https://console.cloud.google.com/support
- **Netlify Support:** https://app.netlify.com/account/support

---

## 🔑 SHARED API KEY DETAILS

**Key Name:** `Parcel-Vision-Pro-API-Key`  
**Created:** Sep 3, 2025  
**Restrictions:** Domain + Google Sheets API only  
**Status:** Active & Working  
**Used By:** Silverstone, Pineleaf, (+ future portals)

**Allowed Domains (as of Feb 18, 2026):**
- ✅ https://pineleaf-estates.netlify.app/*
- ✅ https://jeff-realty-silverstone.netlify.app/*

**To Add New Domain:**
1. Go to credentials page (link above)
2. Edit the key
3. Add URL to "Website" section
4. Save and wait 2-5 minutes

---

## 📝 CHANGE LOG

### Feb 18, 2026
- ✅ Fixed ReferenceError by moving GOOGLE_SHEETS_CONFIG declaration before use
- ✅ Fixed 403 error by adding Silverstone to API key domain restrictions
- ✅ Verified sheet tab name (SILVERSTONE_ESTATE_PARCELS) vs file name confusion
- ✅ Silverstone portal now syncing successfully

### Future Versions
- [ ] Add automatic sheet validation
- [ ] Create admin dashboard for multi-portal management
- [ ] Add mobile app support
- [ ] Implement real-time bidding system

---

**Questions?** Check the troubleshooting section or contact support.
