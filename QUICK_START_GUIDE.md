# Silverstone Estate Ogbeke PVP - Quick Start Guide

## 🗺️ Using the Portal

### Viewing Properties
1. **Open the Map** - The portal loads with satellite view by default
2. **Click any parcel** - Shows property details:
   - Parcel ID (e.g., "P103")
   - Asking Price (₦3,000,000)
   - Property Area (in sqm)
   - Current Status (Available, Sold, Reserved)
3. **Zoom In/Out** - Use mouse wheel or zoom controls in top-left
4. **Pan** - Click and drag the map

### Switching Views
- **Map Button** (top-right): Shows street map with labels
- **Satellite Button** (top-right): Shows satellite imagery (default)
- Toggle between views instantly

### Finding a Property
1. **Search Dropdown** - Top-right corner has parcel list
2. **Select a parcel** - Map zooms to that property
3. **Or click directly** - Click any parcel on the map

### Contacting for Inquiries

#### Option 1: Via WhatsApp (Recommended)
1. Click a parcel
2. Click "📞 Inquire Now" button
3. Fill in your details:
   - Your Name
   - Phone Number
   - Email Address
   - Message (optional)
4. Click "Send via WhatsApp"
5. WhatsApp opens automatically with pre-filled message

#### Option 2: Direct Contact
1. Click a parcel
2. Click "Call Agent" button
3. WhatsApp opens with pre-formatted inquiry

#### Option 3: Share with Friends
1. Click a parcel
2. Click "Share" button
3. Share via WhatsApp to contacts or groups

---

## 🔐 Admin Panel (For Staff Only)

### Accessing Admin
1. Look for **"🔐 Admin Login"** button (top-left)
2. Password-protected dashboard
3. Shows all buyer information and payment tracking

### Admin Features
- View all parcel buyer details
- Update payment status
- Track service fees
- Export reports
- Manage parcel status

**Default Admin Password:** Check with management team

---

## 📍 Location Features

### Map Elements Displayed
- **Blue Parcel Boundaries** - Property outline with ID label
- **White Location Markers** - Nearby landmarks and estates:
  - Civil Defense Estate
  - Pilgrimage Centre
  - Timber Market Ugwuogo
  - National Housing Estate
  - Seaman Global Estate
  - Breeze Garden Estate
  - Behold Gardens Estate

- **Road Lines** - Main access route (Ugwuogo Nike - Opi Road)
- **Estate Boundaries** - Dashed white lines for neighboring estates

### Zoom Levels
- **Zoom 10-14** - Shows entire subdivision with landmarks
- **Zoom 15-18** - Shows individual parcels with road names
- **Zoom 19-25** - Shows detailed boundaries and measurements

---

## 📱 Mobile Usage

### On Smartphone/Tablet
1. Portal is fully responsive
2. Tap parcel to view details
3. Pinch to zoom in/out
4. Two-finger tap for context menu
5. Rotate device for landscape view

### Best Experience On
- **Desktop** - Full features, best for admin
- **Tablet** - Good for property viewing
- **Mobile** - Good for quick inquiries

---

## 🌐 Deployment Options

### Local Testing (Development)
```bash
python -m http.server 8000
# Open: http://localhost:8000/index.html
```

### Netlify (Recommended - Free)
1. Drag and drop `index.html` to Netlify
2. Get instant live URL
3. Custom domain setup available

### Traditional Web Host
1. Upload `index.html` to web server
2. Configure domain DNS
3. Enable HTTPS/SSL

---

## ⚙️ Parcel Status Legend

| Status | Color | Meaning |
|--------|-------|---------|
| Available | 🟢 Green | Ready to purchase |
| Sold | 🔴 Red | Already sold to buyer |
| Reserved | 🟡 Yellow | On hold, being processed |
| Pending | 🟠 Orange | Under review |

---

## 🎯 Property Details Shown

When you click a parcel, the popup displays:

```
📍 PARCEL P103
━━━━━━━━━━━━━━━━━━
💰 Price: ₦3,000,000
📐 Area: 450 sqm
📊 Status: Available
━━━━━━━━━━━━━━━━━━
[📞 Inquire Now] [Share] [View Details]
```

---

## 💬 WhatsApp Integration

### Automatic Inquiry Format
When you submit an inquiry, it sends:

```
🏡 NEW INQUIRY - Silverstone Estate Ogbeke

📍 Interested in: Parcel P103
💰 Listed Price: ₦3,000,000

👤 Customer Details:
• Name: [Your Name]
• Phone: [Your Phone]
• Email: [Your Email]

💬 Message: [Your message]

⏰ Inquiry sent: [Timestamp]
```

**Sent to:** +234 803 992 1371 (A&Z Projects)

---

## 🔍 Troubleshooting

### Map Not Loading
- Check internet connection
- Clear browser cache (Ctrl+Shift+Del)
- Try different browser
- Disable ad-blocker

### Satellite View Not Showing
- Zoom to level 10 or higher
- Wait for tiles to load
- Toggle Map/Satellite twice
- Refresh page (F5)

### WhatsApp Not Opening
- Ensure WhatsApp is installed
- Check phone number setting
- Try copying message manually
- Contact: +234 803 992 1371

### Can't Find a Parcel
- Use dropdown search menu
- Scroll through parcel list
- Zoom out to see entire area
- Click on area to locate

---

## 📞 Support Contacts

| Service | Contact | Hours |
|---------|---------|-------|
| Inquiries | +234 803 992 1371 (WhatsApp) | 9am - 6pm |
| Emergency | +234 806 808 6806 | 24/7 |
| Portal Issues | Submit via admin panel | 9am - 5pm |

---

## 💡 Pro Tips

1. **Best Time to View** - Midday for clearest satellite imagery
2. **Mobile Shortcut** - Add to home screen for quick access
3. **Bulk Inquiries** - Use "Share" to send multiple properties at once
4. **Admin Mode** - Keep separate admin device for tracking
5. **Geolocation** - Enable location services to see distance to parcels

---

## ✅ Checklist Before Launch

- [ ] Portal loads without errors
- [ ] All 51 parcels visible on map
- [ ] Satellite imagery displays
- [ ] Map toggle works
- [ ] Parcel search dropdown populated
- [ ] WhatsApp integration functional
- [ ] Admin panel accessible
- [ ] All pricing shows ₦3,000,000
- [ ] Contact numbers verified
- [ ] Mobile responsive tested

---

**Portal Version:** 1.0.0  
**Last Updated:** November 30, 2025  
**Status:** ✅ Ready for Production
