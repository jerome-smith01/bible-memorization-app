# Quick Start Guide

## Running the App Locally

### Option 1: Simple (Flask Development Server)

The Flask server is **already running**! Just access it:

```
http://127.0.0.1:5000
```

The app serves the `index.html` file automatically.

### Option 2: Fresh Start

If the server stopped, restart it:

```bash
cd "c:\Users\Jerom\My Apps\The Bible Verse Memory App"
python run.py
```

Then open your browser to: `http://127.0.0.1:5000`

---

## Using the Web Interface

### 1. Find a Verse
- **Left card** - "Find a Verse"
- Enter book name (e.g., "John", "Ephesians")
- Enter chapter and verse number
- Click "Fetch Verse"
- See the full text and memory aid (initials)

### 2. Create Memorization Schedule
- **Right card** - "Create Memorization Schedule"
- Click "Yes, Use It" to use the verse you just fetched
- Or manually enter a verse reference
- Set progression interval (days between weeks)
- Choose output method:
  - "Download Calendar (.ics)" - for importing to calendar apps
  - "Email to Me" - send schedule via email
  - "Both" - do both
- Click "Create Schedule"
- Download the calendar file or get email notification

### 3. Manage Your Preferences
- **Bottom card** - "Your Preferences"
- Set your email for notifications
- Set preferred reminder time (6:00 AM by default)
- Set progression interval (7 days by default)
- Click "Save Preferences"

---

## Testing with Example Verses

### Famous Passages to Try:
- **John 1:1-3** - Gospel opening
- **Ephesians 3:17-19** - Paul's prayer
- **Psalm 23:1-6** - The Lord's Prayer
- **Proverbs 3:5-7** - Trust in the Lord
- **Romans 3:23-24** - Grace and redemption
- **1 John 1:1-3** - Fellowship with God
- **Matthew 5:3-12** - The Beatitudes

---

## Understanding the Memory Aid (Initials)

When you fetch a verse, the "Memory Aid (Initials)" takes the first letter of each word:

**Example:**
```
Full Text: "In the beginning was the Word, and the Word was with God..."
Initials:  I  t  b  w  t  W,  a  t  W  w  w  G...
```

This creates a pattern to help you memorize! You can practice reciting the verse while thinking of these initials.

---

## Downloaded Calendar Files

The `.ics` files you download are **calendar format** (RFC 5545). You can import them into:

- ✅ Google Calendar
- ✅ Apple Calendar (macOS/iOS)
- ✅ Microsoft Outlook
- ✅ Mozilla Thunderbird
- ✅ Any calendar app on Windows/Mac/Linux

**To import:**
1. Download the `.ics` file
2. Open your calendar app
3. Look for "Import" or "Add event from file"
4. Select the downloaded file
5. Events appear as recurring daily tasks for your progression weeks

---

## Troubleshooting

### "Cannot connect to API" Error
- Make sure Flask is running (see "Running the App Locally" above)
- Check that you're accessing `http://127.0.0.1:5000` (not `https`)

### Verse Not Found
- Check spelling of book name (case-insensitive)
- Make sure chapter and verse numbers exist
- Try with a known verse like "John 1:1"

### Schedule Won't Create
- Make sure all fields are filled in
- Try with a simple single verse first (e.g., John 1:1)
- Check browser console (F12) for error details

### Download Not Working
- Try a different browser
- Check your Downloads folder
- Allow pop-ups for this site

---

## Environment Variables (Optional)

For email functionality, create a `.env` file in the project root:

```
RESEND_API_KEY=your_api_key_here
FLASK_DEBUG=True
FLASK_ENV=development
```

Get your Resend API key from https://resend.com

---

## Next Steps

### To Deploy to Netlify:
1. Read `DEPLOYMENT_GUIDE.md` for full instructions
2. Create GitHub repository
3. Deploy backend to Render (free)
4. Deploy frontend to Netlify (free)
5. Share your URL!

### To Add More Features:
- See `IMPLEMENTATION_COMPLETE.md` for what's ready
- See `.github/copilot-instructions.md` for development notes
- Check `TEST_RESULTS.md` for API documentation

---

## Support

**Need help?**

1. Check the **Browser Console** (F12 → Console tab) for error messages
2. Check the **Flask Terminal** output for server errors
3. Review the API documentation in `TEST_RESULTS.md`
4. See development notes in `.github/copilot-instructions.md`

---

**Current Status**: ✅ **Everything is working locally!**

Ready to go live? Follow `DEPLOYMENT_GUIDE.md`

