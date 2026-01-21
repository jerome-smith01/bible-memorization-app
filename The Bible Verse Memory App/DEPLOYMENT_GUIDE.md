# Deployment Guide: Bible Memorization Assistant on Netlify

## Overview

Your Bible Memorization Assistant consists of two parts:
1. **Frontend**: HTML/CSS/JavaScript (hosted on Netlify)
2. **Backend**: Flask API (needs separate hosting)

This guide walks you through the deployment process.

---

## Part 1: Deploy Backend to Render (Free)

The Flask backend needs to be hosted somewhere. We'll use **Render** (free tier available).

### Step 1: Create Render Account
1. Go to https://render.com
2. Sign up with GitHub or email
3. Create new account

### Step 2: Prepare Your Project for Deployment

Your project already has `requirements.txt`. Let's verify it's complete:

```
Flask==2.3.3
Flask-CORS==4.0.0
requests==2.31.0
BeautifulSoup4==4.12.2
ics==0.7
python-dateutil==2.8.2
python-dotenv==1.0.0
google-auth-oauthlib==1.1.0
google-auth-httplib2==0.2.0
google-api-python-client==2.100.0
resend==0.3.0
gunicorn==21.2.0
```

### Step 3: Create Procfile
Create a file named `Procfile` in your project root (same level as `requirements.txt`):

```
web: gunicorn run:app
```

### Step 4: Update run.py for Production

Modify `run.py` to work with Gunicorn:

```python
#!/usr/bin/env python
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from src.app import app

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
```

### Step 5: Push to GitHub
1. Initialize git (if not already):
   ```
   git init
   git add .
   git commit -m "Initial commit"
   ```
2. Push to GitHub repository
3. Copy your repository URL

### Step 6: Deploy on Render

1. Go to https://render.com/dashboard
2. Click "New +" → "Web Service"
3. Select "Deploy from a Git repository"
4. Paste your GitHub repository URL
5. Fill in details:
   - **Name**: `bible-memorization-api`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn run:app`
   - **Plan**: Free
6. Click "Create Web Service"
7. Wait for deployment (2-5 minutes)
8. Copy your Render URL (will look like `https://bible-memorization-api.onrender.com`)

**Keep this URL - you'll need it for the frontend!**

---

## Part 2: Deploy Frontend to Netlify

### Step 1: Create Netlify Account
1. Go to https://netlify.com
2. Sign up with GitHub
3. Connect your GitHub account

### Step 2: Prepare Frontend Files

Create these files in your project root:

**netlify.toml** (in project root):
```toml
[build]
  command = "echo 'No build required'"
  publish = "."

[dev]
  command = "python run.py"
  port = 5000

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200

[[headers]]
  for = "/index.html"
  [headers.values]
    Cache-Control = "max-age=0, no-cache, no-store, must-revalidate"
```

### Step 3: Update Frontend with Backend URL

Edit your `index.html` file (around line 360):

**Before** (local development):
```javascript
const API_BASE_URL = 'http://127.0.0.1:5000';
```

**After** (with your Render backend URL):
```javascript
const API_BASE_URL = 'https://bible-memorization-api.onrender.com';
// Replace with your actual Render URL
```

### Step 4: Deploy to Netlify

**Option A: Using GitHub (Recommended)**

1. Commit and push your `index.html` and `netlify.toml` to GitHub
2. Go to https://app.netlify.com
3. Click "Add new site" → "Import an existing project"
4. Select GitHub and authorize
5. Choose your repository
6. Configure build settings:
   - **Base directory**: (leave empty)
   - **Build command**: (leave empty)
   - **Publish directory**: `.`
7. Click "Deploy site"
8. Wait for deployment (1-2 minutes)
9. Your site URL will appear (e.g., `https://your-site-name.netlify.app`)

**Option B: Manual Deployment (Quick)**

1. Create a new folder called `netlify-deploy`
2. Copy only `index.html` and `netlify.toml` into it
3. Go to https://app.netlify.com
4. Drag & drop the folder onto the page
5. Wait for deployment

### Step 5: Verify Deployment

1. Visit your Netlify URL
2. Try fetching a verse (e.g., John 1:1)
3. Check browser console (F12) for any errors

---

## Troubleshooting

### "Cannot connect to API" error

1. Check if Render backend is running (check Render dashboard)
2. Make sure frontend has correct backend URL in `index.html`
3. Check browser console for CORS errors
4. Add backend URL to Netlify environment variables if needed

### CORS Error

If you see "CORS error" in console:

1. Your backend API should have CORS enabled (it does - line 18 of `src/app.py`)
2. Make sure `API_BASE_URL` in `index.html` is correct
3. No trailing slash in the URL

### File Download Not Working

1. Make sure `/download/<filename>` endpoint exists (it does)
2. Check that ICS file was created in `data/` directory
3. Verify file permissions

---

## Environment Variables

### For Render Backend

If you want to use email or Google Tasks features:

1. Go to your Render service dashboard
2. Click "Environment" on the left
3. Add these variables:
   ```
   RESEND_API_KEY = your_api_key_here
   GOOGLE_OAUTH_CLIENT_ID = your_client_id
   GOOGLE_OAUTH_CLIENT_SECRET = your_secret
   FLASK_ENV = production
   ```

---

## Custom Domain (Optional)

### For Netlify:
1. Go to "Domain management"
2. Click "Add a domain"
3. Follow DNS setup instructions

### For Render:
1. Go to "Settings"
2. Click "Custom Domains"
3. Follow instructions

---

## Performance Tips

1. **Render Free Tier**: Spins down after 15 minutes of inactivity
   - First request after inactivity may take 10-30 seconds
   - Pay tier keeps it always running ($7/month)

2. **Improve Speed**:
   - Verses are cached locally (first request takes longer)
   - Subsequent requests are instant
   - Consider upgrading to Render paid tier if speed is critical

---

## Cost Summary

| Component | Cost |
|-----------|------|
| Render Backend (Free) | $0/month |
| Netlify Frontend (Free) | $0/month |
| Custom Domain (Optional) | $10-15/year |
| **Total** | **$0-2/month** |

Render has paid tiers starting at $7/month for always-on service.

---

## Next Steps

1. **Test Locally** (Current):
   - Frontend: Open `http://127.0.0.1:5000` (Flask serves it)
   - Backend: Automatically running on port 5000

2. **Deploy to Netlify**:
   - Update `index.html` with backend URL
   - Follow "Part 2" above

3. **Deploy Backend**:
   - Push to GitHub
   - Deploy on Render
   - Update frontend URL

4. **Go Live**:
   - Share your Netlify URL
   - Users can access from anywhere!

---

## Support Resources

- Netlify Docs: https://docs.netlify.com
- Render Docs: https://render.com/docs
- Flask + Gunicorn: https://flask.palletsprojects.com/deployment/gunicorn/

---

**Questions?** Check the test results and implementation docs in the project.

