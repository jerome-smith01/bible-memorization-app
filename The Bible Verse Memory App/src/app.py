"""Main Flask application for Bible Memorization Assistant"""
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os

# Import services
from .services.bible_fetcher import BibleFetcher
from .formatters.verse_initializer import VerseInitializer
from .models.user_preference import UserPreference

# Get the parent directory (project root)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__, static_folder=BASE_DIR, static_url_path='')
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Initialize services
bible_fetcher = BibleFetcher()
user_prefs = UserPreference.load()


@app.route('/', methods=['GET'])
def serve_index():
    """Serve the main HTML interface"""
    try:
        index_path = os.path.join(BASE_DIR, 'index.html')
        with open(index_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return jsonify({"error": "UI not found. Place index.html in project root."}), 404


@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    """Download generated ICS file"""
    try:
        filepath = os.path.join('data', filename)
        if os.path.exists(filepath):
            return send_file(filepath, as_attachment=True, mimetype='text/calendar')
        else:
            return jsonify({"error": "File not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({"status": "ok", "version": "0.1.0"})


@app.route('/api/verse', methods=['POST'])
def fetch_and_format_verse():
    """
    Fetch Bible verse and convert to initials.
    
    Request body:
    {
        "book": "Ephesians",
        "chapter": 3,
        "verse_start": 17,
        "verse_end": 17
    }
    """
    try:
        data = request.get_json()
        book = data.get('book')
        chapter = data.get('chapter')
        verse_start = data.get('verse_start')
        verse_end = data.get('verse_end', verse_start)

        if not all([book, chapter, verse_start]):
            return jsonify({"error": "Missing required fields"}), 400

        # Fetch verse(s)
        if verse_start == verse_end:
            verse_text = bible_fetcher.fetch_verse(book, chapter, verse_start)
        else:
            verse_text = bible_fetcher.fetch_verse_range(book, chapter, verse_start, verse_end)

        if not verse_text:
            return jsonify({"error": "Verse not found"}), 404

        # Convert to initials
        book_abbr = data.get('book_abbr', book[:3])
        if verse_start == verse_end:
            initials = VerseInitializer.format_with_line_breaks(
                verse_text, book_abbr, chapter, verse_start
            )
        else:
            verses_dict = {
                'text': verse_text,
                'chapter': chapter,
                'start': verse_start,
                'end': verse_end
            }
            initials = VerseInitializer.format_range_with_breaks(verses_dict, book_abbr)

        return jsonify({
            "verse_reference": f"{book} {chapter}:{verse_start}" + (f"-{verse_end}" if verse_end != verse_start else ""),
            "full_text": verse_text,
            "initials": initials,
            "attribution": "Recovery Version Bible, © Living Stream Ministry"
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/preferences', methods=['GET'])
def get_preferences():
    """Get current user preferences"""
    return jsonify(user_prefs.to_dict())


@app.route('/api/preferences', methods=['POST'])
def update_preferences():
    """Update user preferences"""
    try:
        data = request.get_json()
        
        for key, value in data.items():
            if hasattr(user_prefs, key):
                setattr(user_prefs, key, value)
        
        user_prefs.save()
        
        return jsonify({"message": "Preferences updated", "preferences": user_prefs.to_dict()})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/schedule', methods=['POST'])
def schedule_memorization():
    """
    Schedule Bible verse memorization with progressive weekly expansion.
    
    Request body:
    {
        "book": "Ephesians",
        "chapter": 3,
        "verse_start": 17,
        "verse_end": 19,
        "progression_days": 7,
        "output_method": "ics_download|email|google_tasks|both",
        "email": "user@example.com"
    }
    """
    try:
        from .integrations.calendar_generator import CalendarGenerator
        from .integrations.email_service import EmailService
        from datetime import datetime, timedelta
        
        data = request.get_json()
        
        # Validate input
        required_fields = ['book', 'chapter', 'verse_start', 'output_method']
        if not all(field in data for field in required_fields):
            return jsonify({"error": "Missing required fields"}), 400
        
        book = data.get('book')
        chapter = data.get('chapter')
        verse_start = data.get('verse_start')
        verse_end = data.get('verse_end', verse_start)
        progression_days = data.get('progression_days', 7)
        output_method = data.get('output_method', 'ics_download')
        user_email = data.get('email', user_prefs.user_email)
        
        # Fetch the verse(s)
        if verse_start == verse_end:
            full_text = bible_fetcher.fetch_verse(book, chapter, verse_start)
        else:
            full_text = bible_fetcher.fetch_verse_range(book, chapter, verse_start, verse_end)
        
        if not full_text:
            return jsonify({"error": "Verse not found"}), 404
        
        # Convert to initials
        book_abbr = data.get('book_abbr', book[:3])
        if verse_start == verse_end:
            initials = VerseInitializer.format_with_line_breaks(
                full_text, book_abbr, chapter, verse_start
            )
        else:
            verses_dict = {
                'text': full_text,
                'chapter': chapter,
                'start': verse_start,
                'end': verse_end
            }
            initials = VerseInitializer.format_range_with_breaks(verses_dict, book_abbr)
        
        # Generate progression calendar
        start_date = user_prefs.start_date or datetime.now()
        if isinstance(start_date, str):
            start_date = datetime.fromisoformat(start_date)
        
        # Build verse reference
        verse_ref = f"{book} {chapter}:{verse_start}"
        if verse_end != verse_start:
            verse_ref += f"-{verse_end}"
        
        # Create calendar events for progressive memorization
        calendar_gen = CalendarGenerator()
        all_events = []
        
        # Calculate number of weeks needed
        num_verses = (verse_end - verse_start) + 1
        
        for week in range(1, num_verses + 1):
            week_start = start_date + timedelta(days=(week - 1) * progression_days)
            title = f"Memorization - {verse_ref} (Week {week})"
            description = f"Continue memorizing {verse_ref}\n\nProgressively expand your memorization:\n\n{initials}"
            
            event = calendar_gen.generate_ics_event(
                title=title,
                description=description,
                start_date=week_start,
                duration_days=progression_days
            )
            all_events.append(event)
        
        # Create calendar
        calendar = calendar_gen.generate_calendar(all_events)
        
        # Handle output method
        ics_filename = f"memorization_{verse_ref.replace(' ', '_').replace(':', '-')}.ics"
        ics_filepath = os.path.join('data', ics_filename)
        os.makedirs('data', exist_ok=True)
        
        if output_method in ['ics_download', 'both']:
            calendar_gen.save_ics_file(calendar, ics_filepath)
        
        if output_method in ['email', 'both']:
            if user_email:
                email_service = EmailService(os.getenv('RESEND_API_KEY'))
                email_service.send_ics_attachment(
                    recipient_email=user_email,
                    subject=f"Your Bible Memorization Schedule: {verse_ref}",
                    body=f"Your progressive memorization schedule for {verse_ref} is attached.",
                    ics_filepath=ics_filepath
                )
        
        return jsonify({
            "message": "Memorization schedule created successfully",
            "verse_reference": verse_ref,
            "progression_weeks": num_verses,
            "progression_interval_days": progression_days,
            "output_method": output_method,
            "ics_filename": ics_filename if output_method in ['ics_download', 'both'] else None
        }), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found"}), 404


@app.errorhandler(500)
def server_error(error):
    return jsonify({"error": "Internal server error"}), 500


if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG', False), port=5000)
