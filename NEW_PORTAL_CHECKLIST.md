# NEW PORTAL QUICK SETUP TEMPLATE

**Use this checklist when you open a NEW FOLDER to build another PVP portal**

---

## 🚀 STEP-BY-STEP FOR NEW PROJECT

### 1️⃣ GATHER PROJECT INFO
- [ ] Estate Name (e.g., "Madox Homes", "Oranweza Heights")
- [ ] Portal URL for Netlify (will be something like: `https://estate-name.netlify.app`)
- [ ] WhatsApp Contact Number (for inquiries)
- [ ] Admin Password (for client/agent login)
- [ ] Parcel count (how many properties)
- [ ] Default price per parcel (or sheet has individual prices)

### 2️⃣ GOOGLE SHEET SETUP

**What To Do:**
```
📊 Google Sheet
├─ File name: MASTER_TEMPLATE_DATA (or any name)
├─ Sheet tab name: ESTATE_NAME_PARCELS (MUST be exact! case-sensitive)
├─ Columns: A=ParcelID, B=Status, C-L=other data (see docs)
├─ Sharing: File → Share → "Anyone with link" → Viewer
└─ URL Example: docs.google.com/spreadsheets/d/[SHEET_ID]/edit
```

**Get Your Sheet ID:**
- Open your Google Sheet
- Copy from URL: `...spreadsheets/d/[ THIS PART HERE ]/edit...`
- Save it (you'll need it in code)

### 3️⃣ CODE CONFIGURATION

**File to Edit:** `index.html` (around line 4553)

**Find this block:**
```javascript
const GOOGLE_SHEETS_CONFIG = {
    spreadsheetId: '................',
    apiKey: 'AIzaSyCkLewazfYqcQ_llw_Adj_mTNK71T2iRL0',
    sheetName: '...................',
    sheetUrl: 'https://docs.google.com/.../edit...'
};
```

**Replace with YOUR values:**
```javascript
const GOOGLE_SHEETS_CONFIG = {
    spreadsheetId: 'PASTE_YOUR_SHEET_ID_HERE',
    apiKey: 'AIzaSyCkLewazfYqcQ_llw_Adj_mTNK71T2iRL0', // ← KEEP SAME
    sheetName: 'YOUR_ESTATE_PARCELS', // ← MUST match your sheet tab name exactly!
    sheetUrl: 'https://docs.google.com/spreadsheets/d/YOUR_SHEET_ID/edit'
};
```

### 4️⃣ CUSTOMIZE TEXT

**Search & Replace in index.html:**

| Find | Replace With | Example |
|------|--------------|---------|
| `SILVERSTONE ESTATE OGBEKE` | Your Estate Name | `MADOX HOMES LIMITED` |
| `+234 814 704 2804` | Your WhatsApp | `+234 807 123 4567` |
| `3,500,000` | Default price | `2,500,000` |
| `azprojects2025` | New password | `yourclient2025` |
| `A&Z Projects Ltd` | Your Company | `Your Real Estate Co` |

### 5️⃣ GITHUB SETUP

```bash
# Clone template (if repo exists)
git clone https://github.com/Azprojects-tech/template-pvp.git YourEstateName
cd YourEstateName

# Or init fresh
git init
git remote add origin https://github.com/Azprojects-tech/your-repo.git
git add .
git commit -m "Initial commit: New PVP portal setup"
git push -u origin main
```

### 6️⃣ GOOGLE CLOUD - ADD DOMAIN RESTRICTION

**Go to:** https://console.cloud.google.com/apis/credentials

**Edit:** `Parcel-Vision-Pro-API-Key`

**Add your portal domain:**

In the **"Website"** field under **API restrictions**, add:
```
https://YOUR-ESTATE-NAME.netlify.app/*
```

**Wait 2-5 minutes** for changes to take effect

### 7️⃣ DEPLOY TO NETLIFY

```bash
git push origin main
# → Netlify auto-deploys
# → Get your live URL
# → Test the portal
```

### 8️⃣ TEST IT

1. **Open portal** in browser
2. **Wait for map** to load (30 seconds)
3. **Check console** (F12) for errors
4. **Click Admin** button
5. **Enter password**
6. **Click "Admin Sync"** button
7. **Check console** should say: ✅ Public parcel statuses updated
8. **Map colors** should match Google Sheets data

---

## ⚡ QUICK REFERENCE - WHAT CHANGES FOR EACH PORTAL

| Item | Changes? | Value Needed | Where in Code |
|------|----------|--------------|---------------|
| Sheet ID | ✅ YES | Your Google Sheet ID | Line ~4553 |
| Sheet Name | ✅ YES | Your sheet tab name | Line ~4556 |
| API Key | ❌ NO | Same key for all | Line ~4554 |
| Estate Name | ✅ YES | Your estate name | Lines 501, 1169, 4061 |
| Phone Number | ✅ YES | WhatsApp number | Lines 4061, 4079 |
| Admin Password | ✅ YES | Your password | Line 4303 |
| Company Name | ✅ YES | Your company | Footer line |

---

## ❗ COMMON MISTAKES (AVOID THESE!)

### ❌ Mistake 1: Wrong Sheet Name
```javascript
sheetName: 'MASTER_TEMPLATE_DATA' // WRONG! This is file name
sheetName: 'YOUR_ESTATE_PARCELS'   // RIGHT! This is tab name
```

### ❌ Mistake 2: Forgetting API Key Domain
```
Portal launches → Console shows 403 Forbidden
→ Need to add domain to API key in Google Cloud
```

### ❌ Mistake 3: Copy-Pasting URLs
```javascript
// Make sure spreadsheet ID in sheetUrl matches spreadsheetId!
spreadsheetId: '1S5DaLtj6ZrZ...',
sheetUrl: '...d/1S5DaLtj6ZrZ.../edit'
// ↑ Should both have same ID ↑
```

### ❌ Mistake 4: Case-Sensitive Sheet Names
```
Sheet tab is: "ESTATE_Parcels"
Code has: "estate_parcels"
Result: 404 error - sheet not found
```

---

## ✅ VERIFICATION CHECKLIST

Before telling client it's live:

- [ ] Parcels appear on map with colors (green/yellow/red)
- [ ] Click a parcel → popup closes without errors
- [ ] "Admin" button works → password blocks wrong entries
- [ ] "Admin Sync" button → console shows success message
- [ ] Refresh browser → data still loads
- [ ] No red errors in console (F12)
- [ ] Mobile works (Landscape mode toggles map/controls)
- [ ] All contact numbers are correct
- [ ] Estate name shows correctly on title and heading
- [ ] Footer shows client company info

---

## 📞 SUPPORT REFERENCE

**If something breaks:**

1. **Check console errors** (F12 in browser)
2. **Verify Google Sheet is public** (Share → Anyone with link → Viewer)
3. **Verify sheet name matches code** (exact case)
4. **Verify API key domain** includes your portal URL
5. **Wait 5 minutes** after changing API key restrictions
6. **Check GitHub commit** was pushed successfully
7. **Refresh portal** after changes

---

**Last Updated:** Feb 18, 2026  
**Template Version:** 1.0
