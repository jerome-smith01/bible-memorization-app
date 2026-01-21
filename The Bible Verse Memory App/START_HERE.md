# Getting Started - Bible Memorization Assistant

## ✅ Your App is Running!

**Access it here**: http://127.0.0.1:5000

---

## What You Get

A complete Bible memorization assistant with:

### Features
- 📖 **Bible Verse Fetcher** - Get any verse from Recovery Version Bible
- 🎯 **Memory Aids** - Auto-convert verses to first-letter initials
- 📅 **Memorization Schedules** - Progressive 7-day (or custom) intervals
- 📥 **Download Calendars** - Export to Google Calendar, Apple Calendar, Outlook, etc.
- 💾 **Save Preferences** - Your settings persist between sessions
- 📧 **Email Integration** - Send schedules via email (requires API key)

### Tech Stack
- **Frontend**: Modern responsive HTML/CSS/JavaScript
- **Backend**: Flask REST API (Python)
- **Database**: Local JSON files
- **Deployment**: Ready for Netlify + Render (both free!)

---

## Using the Web Interface

### 1️⃣ Find a Verse

**Left Card - "Find a Verse"**

```
Steps:
1. Enter book name (e.g., "John", "Ephesians", "Psalm")
2. Enter chapter number
3. Enter verse number(s)
4. Click "Fetch Verse"
```

**Example:**
- Book: `John`
- Chapter: `1`
- Verse Start: `1`
- Verse End: `(empty for single verse)`

Result:
```
Full Text: "In the beginning was the Word, and the Word was with God, and the Word was God."

Memory Aid (Initials): "I t b w t W, a t W w w G, a t W w G."
```

### 2️⃣ Create Memorization Schedule

**Right Card - "Create Memorization Schedule"**

```
Steps:
1. Enter verse reference or click "Yes, Use It" (from left card)
2. Set progression interval (default: 7 days)
3. Choose output method:
   - "Download Calendar (.ics)" - for importing to calendar apps
   - "Email to Me" - send schedule via email
   - "Both" - do both!
4. Click "Create Schedule"
5. Download the file
```

**What You Get:**
- Multi-week progression calendar
- Week 1: Verse 1
- Week 2: Verses 1-2  
- Week 3: Verses 1-3 (etc.)
- Each event repeats daily for your chosen interval

### 3️⃣ Manage Preferences

**Bottom Card - "Your Preferences"**

```
Settings:
- Email address (for notifications)
- Daily reminder time (e.g., 6:00 AM)
- Progression interval (days - default 7)
- Bible version (Recovery Version)
```

---

## Try It Now!

### Quick Test Verses

Try these famous passages:

| Verse | Reference |
|-------|-----------|
| Gospel Opening | John 1:1-3 |
| Paul's Prayer | Ephesians 3:17-19 |
| The Beatitudes | Matthew 5:3-12 |
| The Lord's Prayer | Psalm 23:1-6 |
| Trust in God | Proverbs 3:5-7 |
| Grace | Romans 3:23-24 |
| Fellowship | 1 John 1:1-3 |

**Try John 1:1:**
1. Enter "John" in book field
2. Enter "1" in chapter
3. Enter "1" in verse start
4. Click "Fetch Verse"
5. See the memory aid!

---

## Deploying to Netlify

When ready to go live to the world:

### Quick Path (5-10 minutes)
1. Read `DEPLOYMENT_GUIDE.md`
2. Push code to GitHub
3. Deploy backend to Render.com (free tier)
4. Deploy frontend to Netlify.com (free tier)
5. Update `index.html` with your backend URL
6. Share your Netlify URL!

### Cost
- **Free Tier Total**: $0/month
- Optional paid upgrades: $7/month (Render) or $10+/month (Netlify)

---

## Understanding Memory Aids

### How It Works

The "Memory Aid (Initials)" takes the first letter of each word:

```
Original:  "In the beginning was the Word, and the Word was with God..."
Initials:  I  t  b        w    t    W     a   t   W    w   w    G

Abbreviated: "I t b w t W, a t W w w G..."
```

### Why This Helps

- **Visual Pattern**: Easier to remember the sequence
- **Guided Recitation**: Recite the verse while thinking of initials
- **Daily Practice**: Use calendar to practice each week's verses
- **Progressive Challenge**: Each week, expand from previous verses

### Example Schedule
```
Week 1: "I t b w t W, a t W w w G, a t W w G."
Week 2: "I t b w t W, a t W w w G, a t W w G. H w i t b w G."
Week 3: "I t b w t W, a t W w w G, a t W w G. H w i t b w G. A t c i b t H..."
```

Each week, you keep the previous verses and add more!

---

## Importing Downloaded Calendars

After creating a schedule, you get a `.ics` file (calendar format).

### How to Import

**Google Calendar:**
1. Go to https://calendar.google.com
2. Click "+" → "Import & export"
3. Select your .ics file
4. Click "Import"
5. Events appear in your calendar!

**Apple Calendar (Mac/iPhone):**
1. Double-click the .ics file
2. Click "Import"
3. Select which calendar to add to
4. Done!

**Microsoft Outlook:**
1. Click "File" → "Open & Export"
2. Click "Import"
3. Select the .ics file
4. Click "Import"

**Any other calendar app:**
1. Look for "Import" option
2. Select the .ics file
3. You're in!

---

## Troubleshooting

### Can't access the app
- Make sure Flask is running (terminal shows "Running on http://127.0.0.1:5000")
- If not, run: `python run.py` from the project folder
- Try in a different browser

### "Cannot fetch verse" error
- Check verse reference is valid (e.g., John 1:1 exists)
- Try a well-known verse like John 1:1
- Check browser console (F12) for more info

### "Cannot connect to API" when deploying
- After deploying to Netlify, update `index.html` line ~360
- Change: `const API_BASE_URL = 'http://127.0.0.1:5000'`
- To: `const API_BASE_URL = 'https://your-backend-url.com'`
- Save and redeploy frontend

### Calendar won't import
- Make sure file is .ics format
- Try importing to different calendar app
- Delete and recreate the schedule

---

## File Structure

```
Your Project/
├── index.html                    ← Web interface (frontend)
├── run.py                        ← Start Flask here
├── requirements.txt              ← Python dependencies
├── netlify.toml                  ← Netlify config
├── Procfile                      ← Production config
│
├── src/
│   ├── app.py                   ← Flask API
│   ├── models/user_preference.py ← Saves your settings
│   ├── services/bible_fetcher.py ← Gets verses from web
│   ├── formatters/verse_initializer.py ← Makes initials
│   └── integrations/             ← Calendar, email, tasks
│
├── data/
│   ├── user_preferences.json     ← Your settings (auto-saved)
│   ├── verse_cache.json          ← Cached verses (speeds up)
│   └── memorization_*.ics        ← Downloaded calendars
│
└── Documentation:
    ├── README.md                 ← Full overview
    ├── QUICK_START.md           ← This file's full version
    ├── DEPLOYMENT_GUIDE.md      ← How to deploy
    ├── TEST_RESULTS.md          ← API documentation
    └── IMPLEMENTATION_COMPLETE.md ← Technical details
```

---

## Next Steps

### 🚀 Go Live (Free Deployment)
1. Open `DEPLOYMENT_GUIDE.md`
2. Follow the steps (takes ~30 minutes)
3. Share your link!

### 🔧 Add More Features
- Email notifications (need Resend API key)
- Google Tasks integration (need Google OAuth)
- Custom frontend design
- Mobile app wrapper

### 📚 Learn More
- `IMPLEMENTATION_COMPLETE.md` - All technical details
- `TEST_RESULTS.md` - API documentation
- `.github/copilot-instructions.md` - Code notes

---

## API Endpoints (For Developers)

All endpoints available at `http://127.0.0.1:5000/api/`:

| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/health` | Check if server is running |
| POST | `/verse` | Fetch and format Bible verse |
| GET | `/preferences` | Get your saved settings |
| POST | `/preferences` | Save your settings |
| POST | `/schedule` | Create memorization schedule |
| GET | `/download/<file>` | Download calendar file |

Full API docs in `TEST_RESULTS.md`.

---

## Support

**Having issues?**

1. **Check the terminal** - Flask might show error messages
2. **Browser console** - Press F12, click "Console" for JavaScript errors
3. **Documentation** - See docs folder for detailed guides
4. **Try different verse** - Test with John 1:1

---

## Summary

You now have:

✅ A working Bible memorization app  
✅ Full-featured web interface  
✅ REST API backend  
✅ Calendar integration  
✅ Preference persistence  
✅ Ready-to-deploy code  

### One Thing to Remember

When you update `index.html` to point to your Netlify backend, change line ~360:

```javascript
// Local development:
const API_BASE_URL = 'http://127.0.0.1:5000';

// After deploying (replace with your backend URL):
const API_BASE_URL = 'https://your-render-backend-url.com';
```

---

## Questions?

Everything you need is in the documentation:

- **"How do I use it?"** → QUICK_START.md (or this file)
- **"How do I deploy?"** → DEPLOYMENT_GUIDE.md
- **"How does the API work?"** → TEST_RESULTS.md
- **"What's the code structure?"** → IMPLEMENTATION_COMPLETE.md

---

**Enjoy memorizing Scripture!** 📖

