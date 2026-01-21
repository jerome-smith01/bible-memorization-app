"""Converts Bible verses to first-letter initials"""
import re


class VerseInitializer:
    """Converts verse text to first initial of each word"""

    @staticmethod
    def to_initials(verse_text: str) -> str:
        """
        Convert verse text to first initial of each word.
        Preserves punctuation and case.
        
        Args:
            verse_text: Full verse text
            
        Returns:
            Formatted initials with punctuation
        """
        if not verse_text:
            return ""

        # Split by spaces while preserving punctuation attached to words
        words = verse_text.split()
        initials = []

        for word in words:
            if not word:
                continue

            # Separate leading punctuation from word
            leading_punct = ""
            trailing_punct = ""
            clean_word = word

            # Extract leading punctuation (e.g., opening quotes, parentheses)
            i = 0
            while i < len(word) and not word[i].isalnum():
                i += 1
            leading_punct = word[:i]
            clean_word = word[i:]

            # Extract trailing punctuation (e.g., periods, commas, quotes)
            j = len(clean_word) - 1
            while j >= 0 and not clean_word[j].isalnum():
                j -= 1
            if j >= 0:
                trailing_punct = clean_word[j + 1:]
                clean_word = clean_word[:j + 1]
            else:
                # All punctuation
                trailing_punct = clean_word
                clean_word = ""

            # Get first character if word exists
            if clean_word:
                initial = clean_word[0]
                initials.append(leading_punct + initial + trailing_punct)
            elif leading_punct or trailing_punct:
                # Preserve standalone punctuation
                initials.append(leading_punct + trailing_punct)

        return " ".join(initials)

    @staticmethod
    def format_with_line_breaks(verse_text: str, book_abbr: str, chapter: int, verse: int) -> str:
        """
        Format verse initials with line breaks at sentence boundaries.
        
        Args:
            verse_text: Full verse text
            book_abbr: Book abbreviation (e.g., 'Eph')
            chapter: Chapter number
            verse: Verse number
            
        Returns:
            Formatted initials with line breaks and footer
        """
        initials = VerseInitializer.to_initials(verse_text)

        # Split by sentence boundaries (periods, question marks, exclamation marks)
        sentences = re.split(r'(?<=[.!?])\s+', initials)

        # Join with line breaks
        formatted = "\n".join(sentences)

        # Add footer with obscured reference
        footer = f"\n{book_abbr} --:--"
        
        return formatted + footer

    @staticmethod
    def format_range_with_breaks(verses_dict: dict, book_abbr: str) -> str:
        """
        Format multiple verses (range) with line breaks.
        
        Args:
            verses_dict: Dict with format {'text': full_text, 'chapter': int, 'start': int, 'end': int}
            book_abbr: Book abbreviation
            
        Returns:
            Formatted initials
        """
        initials = VerseInitializer.to_initials(verses_dict['text'])
        sentences = re.split(r'(?<=[.!?])\s+', initials)
        formatted = "\n".join(sentences)
        
        chapter = verses_dict['chapter']
        start_v = verses_dict['start']
        end_v = verses_dict['end']
        
        footer = f"\n{book_abbr} --:--"
        return formatted + footer
