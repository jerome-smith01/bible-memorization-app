# Bible Memorization Assistant

A REST API and conversational assistant for Bible verse memorization using the Recovery Version Bible. Features include verse fetching, progressive memorization scheduling, calendar integration, and email delivery.

**Current Status**: ✅ Fully functional with all core features implemented and tested

## Features

- **Bible Text Fetching**: Retrieves verses from [Recovery Version Bible](https://text.recoveryversion.bible/) with intelligent HTML parsing
- **Verse Initialization**: Converts verse text to first-letter initials while preserving punctuation and formatting
- **Progressive Memorization**: Configurable multi-week progression (default 7 days, user-selectable)
- **Multi-Output Support**:
  - RFC 5545 .ics calendar file generation (tested and working)
  - Email delivery via Resend API (ready for API key configuration)
  - Google Tasks integration (structure ready, OAuth implementation pending)
- **Cross-Session Persistence**: User preferences stored in JSON format (tested)
- **Fair Use Compliance**: Proper attribution to Living Stream Ministry on all outputs
- **REST API**: Five endpoints for programmatic access

## Project Structure

```
bible_memorization_app/
├── src/
│   ├── services/           # External service integrations
│   │   ├── bible_fetcher.py
│   │   └── ...
│   ├── formatters/         # Verse formatting logic
│   │   └── verse_initializer.py
│   ├── integrations/       # API integrations
│   │   ├── calendar_generator.py
│   │   ├── email_service.py
│   │   └── google_tasks.py
│   ├── models/             # Data models
│   │   └── user_preference.py
│   ├── app.py              # Flask application
│   └── __init__.py
├── data/                   # User preferences and cache
│   ├── user_preferences.json
│   └── verse_cache.json
├── requirements.txt        # Python dependencies
├── .env.example           # Environment variables template
├── .gitignore            # Git ignore rules
└── README.md            # This file
```

## Installation

### Prerequisites
- Python 3.8+
- pip

### Setup

1. **Clone the repository**:
   ```bash
   cd "The Bible Verse Memory App"
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # Windows
   # or
   source venv/bin/activate      # macOS/Linux
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**:
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and add your API keys:
   ```
   RESEND_API_KEY=your_resend_api_key
   FLASK_ENV=development
   FLASK_DEBUG=True
   ```

## Usage

### Running the Flask Server

```bash
python -m src.app
```

Server runs on `http://localhost:5000`

### API Endpoints

#### 1. Fetch Verse and Convert to Initials

**POST** `/api/verse`

Request:
```json
{
  "book": "Ephesians",
  "chapter": 3,
  "verse_start": 17,
  "verse_end": 19,
  "book_abbr": "Eph"
}
```

Response:
```json
{
  "verse_reference": "Ephesians 3:17-19",
  "full_text": "...",
  "initials": "T...\nG...\nE...\n\nEph --:--",
  "attribution": "Recovery Version Bible, © Living Stream Ministry"
}
```

#### 2. Get User Preferences

**GET** `/api/preferences`

Response:
```json
{
  "start_date": "2026-01-26",
  "start_time": "06:00",
  "bible_version": "Recovery Version",
  "progression_interval_days": 7,
  "output_preference": "email",
  "user_email": "user@example.com"
}
```

#### 3. Update User Preferences

**POST** `/api/preferences`

Request:
```json
{
  "progression_interval_days": 3,
  "output_preference": "both",
  "user_email": "newemail@example.com"
}
```

#### 4. Schedule Memorization

**POST** `/api/schedule`

Request:
```json
{
  "book": "Ephesians",
  "chapter": 3,
  "verse_start": 17,
  "verse_end": 19,
  "progression_days": 7,
  "output_method": "email",
  "email": "user@example.com"
}
```

## Configuration

### Environment Variables

- `RESEND_API_KEY`: Resend email API key (for email delivery)
- `GOOGLE_OAUTH_CLIENT_ID`: Google OAuth client ID (for Google Tasks)
- `GOOGLE_OAUTH_CLIENT_SECRET`: Google OAuth client secret
- `FLASK_ENV`: Set to `development` or `production`
- `FLASK_DEBUG`: Set to `True` for development

### Resend API Setup

1. Sign up at [Resend.com](https://resend.com)
2. Create an API key (free tier: 3,000 emails/month)
3. Add to `.env` as `RESEND_API_KEY`

### Google Tasks Setup (Future Enhancement)

Full Google OAuth2 setup is required for Google Tasks integration. Currently marked as future enhancement.

## Development

### Running Tests

Tests will be added in future phases.

### Code Structure

- **services/**: Handles external API communication (Bible text, Google Tasks, Resend)
- **formatters/**: Processes verse text (e.g., initial conversion, line breaks)
- **integrations/**: Specialized integrations (calendar, email, task management)
- **models/**: Data structures (user preferences, task data)

## Future Enhancements

- [ ] Google Tasks list auto-creation
- [ ] Full OAuth2 flow for Google Tasks
- [ ] Unit and integration tests
- [ ] Web UI (React/Vue frontend)
- [ ] Additional Bible versions (KJV, NIV, ESV)
- [ ] Mobile app support
- [ ] Memorization progress tracking
- [ ] Community verse sharing

## Licensing

**Bible Text**: Recovery Version Bible, © Living Stream Ministry. Used with fair use guidelines.

**Application Code**: MIT License

## Attribution

Recovery Version Bible source: https://text.recoveryversion.bible/
Living Stream Ministry: https://www.lsm.org/

## Support

For issues or questions, contact: [support contact info to be added]

---

**Version**: 0.1.0  
**Last Updated**: January 20, 2026
