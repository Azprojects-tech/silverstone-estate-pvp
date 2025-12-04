# 🔧 PRICE & PHONE NUMBER UPDATE GUIDE

## 💰 PRICE CHANGE: ₦3,000,000 → What new price?

### **Option A: Google Sheet (RECOMMENDED for future flexibility)**

**✅ PROS:**
- Change price ONCE, it updates everywhere
- Client can update prices themselves anytime
- Perfect if prices change frequently
- Better for admin dashboard

**❌ CONS:**
- Takes 2 steps to implement
- Slightly slower (API calls to Google Sheets)

**How:**
1. Edit your Google Sheet (MASTER_TEMPLATE_DATA)
2. Add a `price` column with the new price
3. Refresh the portal - it automatically loads from sheet

---

### **Option B: Replace in Code (FASTER for one-time change)**

**✅ PROS:**
- Instant change (no API calls)
- Only 3 places to update in index.html
- Faster execution

**❌ CONS:**
- Have to edit code every time price changes
- More places to remember to update
- Less flexible for client

**How:**
Replace `₦3,000,000` and `3000000` in these locations:
- Line 4158: WhatsApp message template (₦3,000,000)
- Line 4176: WhatsApp message template (₦3,000,000)
- Line 4187: Share message template (₦3,000,000)
- Line 4350: Popup display (₦3,000,000)
- Line 5888: Database calculation (3000000)
- Line 5896: Database calculation (3000000)
- Line 5905: Default price (3000000)

---

## 📞 PHONE NUMBER: +2348039921371 → +2348147042804

### **Only ONE way (Code replacement)**

There are **3 places** to update:

1. **Line 4161** - WhatsApp inquiry button
   ```
   wa.me/2348039921371 → wa.me/2348147042804
   ```

2. **Line 4179** - WhatsApp share button
   ```
   wa.me/2348039921371 → wa.me/2348147042804
   ```

3. **Line 4187** - Share message text
   ```
   +234 803 992 1371 → +234 814 704 2804
   ```

---

## 🎯 MY RECOMMENDATION

### **Best Approach:**

**For PRICE:**
→ Use **Google Sheet** (Option A)
- Change once, apply everywhere
- More professional for client management
- Future-proof if prices change

**For PHONE:**
→ Use **Code Replacement** (Option B)
- Only 3 places to change
- Quick and simple
- Done in 5 minutes

---

## 📊 WHAT'S YOUR NEW PRICE?

Tell me the new price and I'll:

1. ✅ Update it in the code (3 places)
2. ✅ Update WhatsApp phone (3 places)
3. ✅ Push to GitHub
4. ✅ Netlify auto-deploys

**Takes 5 minutes total!** ⚡

---

## 🔄 IMPLEMENTATION STEPS

**Step 1:** Tell me the new price
- Example: ₦2,500,000 or ₦3,500,000?

**Step 2:** I'll replace:
- All price references in code
- All WhatsApp phone numbers
- Commit to GitHub
- Auto-deploy to Netlify

**Step 3:** Done! Portal updates automatically

---

## 💡 AFTER THIS UPDATE

Whenever you change prices/phone in future:

**If you chose Google Sheet approach:**
```
Edit Google Sheet → Refresh portal → Done!
(No code changes needed)
```

**If you chose Code approach:**
```
Edit code → git add . → git commit → git push
(Netlify auto-deploys in 30-90 seconds)
```

---

## ✅ READY WHEN YOU ARE!

Just tell me:
1. **New price per parcel:** ?
2. **Confirm new phone:** +2348147042804

And I'll make both changes instantly! 🚀
