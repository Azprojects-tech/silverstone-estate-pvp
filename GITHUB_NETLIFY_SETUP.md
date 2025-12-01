# GitHub + Netlify Deployment Guide
## Silverstone Estate Ogbeke PVP

---

## 🚀 STEP-BY-STEP DEPLOYMENT

### **Step 1: Initialize Git Repository**

```bash
cd "c:\Users\Admin\Silverstone Estate Ogbeke"
git init
git add .
git commit -m "v1.0.0 - Initial Silverstone Estate PVP Portal"
git branch -M main
```

### **Step 2: Create GitHub Repository**

1. Go to **https://github.com/new**
2. Create new repository:
   - **Repository name:** `silverstone-estate-pvp`
   - **Description:** "Interactive Property Visualization Portal - Silverstone Estate Ogbeke"
   - **Visibility:** Public (required for free Netlify)
   - **Initialize:** Leave unchecked (we already have files)
   - Click **"Create repository"**

3. After creation, you'll see commands. Run these in your terminal:

```bash
git remote add origin https://github.com/YOUR-USERNAME/silverstone-estate-pvp.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your actual GitHub username.

---

### **Step 3: Connect GitHub to Netlify**

1. Go to **https://app.netlify.com**
2. Click **"New site from Git"**
3. Click **"GitHub"**
4. Select **"silverstone-estate-pvp"** repository
5. Configure build settings:
   - **Build command:** (leave blank)
   - **Publish directory:** `.` (root directory)
   - Click **"Deploy site"**

**Netlify will:**
- ✅ Automatically deploy your site
- ✅ Assign a live URL (like: `https://silverstone-estate.netlify.app`)
- ✅ Auto-update whenever you push to GitHub

---

### **Step 4: Update Silverstone Data**

**Workflow for updates:**

```bash
# Make changes to your files locally (e.g., index.html)
git add .
git commit -m "Updated parcel prices and buyer data"
git push origin main

# Netlify automatically detects the push and redeploys!
# Check deployment status: https://app.netlify.com
```

---

### **Step 5: Set Custom Domain (Optional)**

In Netlify dashboard:
1. Go to **Settings > Domain management**
2. Click **"Add domain"**
3. Enter your domain (e.g., `silverstone-estate.com`)
4. Follow DNS setup instructions
5. Netlify provides **FREE SSL certificate**

---

## 📋 WHAT TO COMMIT TO GITHUB

### **Essential Files (COMMIT THESE):**
- ✅ `index.html` - Main portal
- ✅ `README.md` - Documentation
- ✅ `START_HERE.md` - Quick start guide
- ✅ `DEPLOYMENT_GUIDE.md` - Deployment instructions
- ✅ `QUICK_START_GUIDE.md` - User guide
- ✅ `.gitignore` - Git ignore rules

### **Helper Scripts (OPTIONAL):**
- ✅ `convert_geojson.py` - For future data updates
- ✅ `inject_data.py` - For injecting new parcel data

### **DO NOT COMMIT:**
- ❌ API keys / credentials (already in index.html but marked)
- ❌ Large media files
- ❌ node_modules, __pycache__, .vscode

---

## 🔄 UPDATING THE PORTAL

### **Scenario 1: Update Parcel Data**
```bash
# 1. Update GeoJSON or run conversion scripts
python convert_geojson.py
python inject_data.py

# 2. Push to GitHub
git add index.html
git commit -m "Updated parcel data - 5 new parcels added"
git push origin main

# 3. Live! Check https://app.netlify.com for deployment status
# Client sees updates in ~30-60 seconds
```

### **Scenario 2: Update Prices or Information**
```bash
# 1. Edit index.html directly
# (or use convert_geojson.py to regenerate data)

# 2. Push to GitHub
git add index.html
git commit -m "Updated pricing to ₦3,500,000"
git push origin main

# 3. Live immediately!
```

### **Scenario 3: Fix Bugs or Styling**
```bash
# 1. Edit files as needed
# 2. Test locally

# 3. Push to GitHub
git add .
git commit -m "Fixed satellite map display issue"
git push origin main

# 4. Live!
```

---

## 📊 NETLIFY DEPLOYMENT STATUS

After pushing to GitHub:
1. Go to **https://app.netlify.com**
2. Select **silverstone-estate-pvp** site
3. Watch deployment progress in real-time
4. Once "Published", changes are live

**Expected time:** 30-90 seconds from push to live

---

## 🔐 SECURITY NOTES

### **API Keys in Code:**
The Google Sheets API key is embedded in `index.html`. This is okay because:
- ✅ Key is restricted to read-only Google Sheets API
- ✅ Key has IP/referrer restrictions in Google Console
- ✅ Only accesses the specific public spreadsheet

### **For Production:**
If you want to hide the key, create a backend server that:
1. Stores the API key securely
2. Proxies Google Sheets requests
3. Portal makes requests to your backend instead

---

## 📞 HANDOVER CHECKLIST

Before giving client the URL:

- [ ] Verify all 51 parcels display on map
- [ ] Check prices are correct (₦3,000,000)
- [ ] Verify admin panel syncs with Google Sheet
- [ ] Test WhatsApp inquiry button
- [ ] Test on mobile devices
- [ ] Test satellite map toggle
- [ ] Verify contact information is correct

---

## 🎯 DEPLOYMENT COMMANDS REFERENCE

```bash
# Initial setup
git init
git add .
git commit -m "v1.0.0 - Initial commit"
git remote add origin https://github.com/USERNAME/silverstone-estate-pvp.git
git push -u origin main

# Subsequent updates
git add .
git commit -m "Description of changes"
git push origin main

# View commit history
git log --oneline

# Check status before pushing
git status
```

---

## 🌐 CLIENT ACCESS

**Give your client this URL:**
```
https://silverstone-estate.netlify.app
```

**They can:**
- ✅ View all 51 properties
- ✅ Toggle between Map and Satellite
- ✅ Click parcels for details
- ✅ Send WhatsApp inquiries
- ✅ See real-time buyer database (admin panel)

**Updates are automatic:**
- Every time you push to GitHub
- Changes live within 1 minute
- No manual deployment needed

---

## 📈 NEXT STEPS

1. ✅ Setup GitHub repo (follow Step 1-2 above)
2. ✅ Connect to Netlify (follow Step 3 above)
3. ✅ Get live URL from Netlify
4. ✅ Share with client
5. ✅ Make updates as needed via GitHub push

---

**Questions?** Check Netlify docs: https://docs.netlify.com

**Ready to go live!** 🚀
