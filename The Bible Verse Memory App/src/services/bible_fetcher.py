"""Fetches Bible verses from Recovery Version website"""
import requests
from bs4 import BeautifulSoup
import json
import os
from typing import Optional


class BibleFetcher:
    """Fetches verse text from https://text.recoveryversion.bible/"""
    
    BASE_URL = "https://text.recoveryversion.bible"
    CACHE_FILE = "data/verse_cache.json"
    
    # Book number mapping (01-66 for OT/NT)
    BOOK_MAP = {
        "Genesis": "01", "Exodus": "02", "Leviticus": "03", "Numbers": "04",
        "Deuteronomy": "05", "Joshua": "06", "Judges": "07", "Ruth": "08",
        "1 Samuel": "09", "2 Samuel": "10", "1 Kings": "11", "2 Kings": "12",
        "1 Chronicles": "13", "2 Chronicles": "14", "Ezra": "15", "Nehemiah": "16",
        "Esther": "17", "Job": "18", "Psalms": "19", "Proverbs": "20",
        "Ecclesiastes": "21", "Isaiah": "22", "Jeremiah": "23", "Lamentations": "24",
        "Ezekiel": "25", "Daniel": "26", "Hosea": "27", "Joel": "28",
        "Amos": "29", "Obadiah": "30", "Jonah": "31", "Micah": "32",
        "Nahum": "33", "Habakkuk": "34", "Zephaniah": "35", "Haggai": "36",
        "Zechariah": "37", "Malachi": "38", "Matthew": "40", "Mark": "41",
        "Luke": "42", "John": "43", "Acts": "44", "Romans": "45",
        "1 Corinthians": "46", "2 Corinthians": "47", "Galatians": "48",
        "Ephesians": "49", "Philippians": "50", "Colossians": "51",
        "1 Thessalonians": "52", "2 Thessalonians": "53", "1 Timothy": "54",
        "2 Timothy": "55", "Titus": "56", "Philemon": "57", "Hebrews": "58",
        "James": "59", "1 Peter": "60", "2 Peter": "61", "1 John": "62",
        "2 John": "63", "3 John": "64", "Jude": "65", "Revelation": "66",
    }

    def __init__(self):
        """Initialize fetcher with cache"""
        self.cache = self._load_cache()

    def _load_cache(self) -> dict:
        """Load verse cache from file"""
        if os.path.exists(self.CACHE_FILE):
            with open(self.CACHE_FILE, 'r') as f:
                return json.load(f)
        return {}

    def _save_cache(self):
        """Save verse cache to file"""
        os.makedirs(os.path.dirname(self.CACHE_FILE) or '.', exist_ok=True)
        with open(self.CACHE_FILE, 'w') as f:
            json.dump(self.cache, f, indent=2)

    def fetch_verse(self, book: str, chapter: int, verse: int) -> Optional[str]:
        """
        Fetch a single verse.
        Args:
            book: Book name (e.g., 'John', 'Ephesians')
            chapter: Chapter number
            verse: Verse number
        Returns:
            Verse text or None if not found
        """
        import re
        cache_key = f"{book}_{chapter}_{verse}"
        
        # Check cache first
        if cache_key in self.cache:
            return self.cache[cache_key]

        try:
            # Build URL: e.g., https://text.recoveryversion.bible/43_John_1.htm
            book_num = self.BOOK_MAP.get(book)
            if not book_num:
                return None

            # Fetch chapter page
            url = f"{self.BASE_URL}/{book_num}_{book}_{chapter}.htm"
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            # Parse HTML
            soup = BeautifulSoup(response.content, 'html.parser')
            text_content = soup.get_text()
            
            # Create book abbreviation (e.g., John -> Jn, Ephesians -> Eph)
            if len(book) <= 4:
                book_abbr = book
            else:
                # For longer names, use first 3 letters + period
                book_abbr = book[:3]
            
            # Try multiple verse reference patterns since the website uses variations
            # Pattern 1: "Book Chapter:Verse " (with space after)
            pattern1 = f"{book} {chapter}:{verse} "
            # Pattern 2: "Abbreviated Book Chapter:Verse " (e.g., "Eph. 3:17 ")
            pattern2 = f"{book_abbr}. {chapter}:{verse} "
            # Pattern 3: Just the chapter:verse format
            pattern3 = f"{chapter}:{verse} "
            
            patterns = [pattern1, pattern2, pattern3]
            verse_text = None
            
            for pattern in patterns:
                start_idx = text_content.find(pattern)
                if start_idx != -1:
                    # Start after the verse reference
                    text_start = start_idx + len(pattern)
                    
                    # Find the next verse reference
                    remaining_text = text_content[text_start:]
                    
                    # Look for next verse pattern (could be Chapter:NextVerse or NextChapter:FirstVerse)
                    next_verse_match = re.search(r'\n[A-Z][a-z.]*\s*\d+:\d+\s', remaining_text)
                    if not next_verse_match:
                        # Try alternate pattern for abbreviated forms
                        next_verse_match = re.search(r'\n[A-Z][a-z]+\.\s*\d+:\d+\s', remaining_text)
                    
                    if next_verse_match:
                        verse_text = remaining_text[:next_verse_match.start()].strip()
                    else:
                        # Last verse in chapter
                        verse_text = remaining_text[:500].strip()
                        footer_idx = verse_text.find('Table of Contents')
                        if footer_idx > 0:
                            verse_text = verse_text[:footer_idx].strip()
                    
                    # Clean up and cache
                    verse_text = ' '.join(verse_text.split())
                    
                    if verse_text:
                        self.cache[cache_key] = verse_text
                        self._save_cache()
                        return verse_text
                    else:
                        # Pattern found but text extraction failed, try next pattern
                        continue
            
            return None
            
        except Exception as e:
            print(f"Error fetching {book} {chapter}:{verse} - {e}")
            return None

    def fetch_verse_range(self, book: str, chapter: int, start_verse: int, end_verse: int) -> Optional[str]:
        """
        Fetch a range of verses.
        Args:
            book: Book name
            chapter: Chapter number
            start_verse: Starting verse number
            end_verse: Ending verse number
        Returns:
            Combined verse text or None
        """
        verses = []
        for v in range(start_verse, end_verse + 1):
            verse_text = self.fetch_verse(book, chapter, v)
            if verse_text:
                verses.append(verse_text)
        
        return " ".join(verses) if verses else None
