"""Generates RFC 5545 compliant iCalendar (.ics) files"""
from datetime import datetime, timedelta
from ics import Calendar, Event
import uuid


class CalendarGenerator:
    """Generates .ics calendar files for Bible memorization tasks"""

    @staticmethod
    def generate_ics_event(
        title: str,
        description: str,
        start_date: datetime,
        duration_days: int = 7
    ) -> Event:
        """
        Create a single calendar event.
        
        Args:
            title: Event title (e.g., "Ephesians 3:17")
            description: Event description (verse initials)
            start_date: Start date/time
            duration_days: Event duration in days (default 7)
            
        Returns:
            ics.Event object
        """
        event = Event()
        event.name = title
        event.description = description
        event.begin = start_date
        event.end = start_date + timedelta(days=duration_days)
        event.uid = f"{uuid.uuid4()}@bible-memory.local"
        
        # Daily recurrence for 7 days
        event.repeat = "daily"
        event.repeat_interval = 1
        event.repeat_count = duration_days
        
        return event

    @staticmethod
    def generate_calendar(events_list: list) -> Calendar:
        """
        Create a complete calendar with multiple events.
        
        Args:
            events_list: List of Event objects
            
        Returns:
            ics.Calendar object
        """
        cal = Calendar()
        cal.creator = "Bible Memorization Assistant"
        
        for event in events_list:
            cal.events.add(event)
        
        return cal

    @staticmethod
    def save_ics_file(calendar: Calendar, filepath: str) -> str:
        """
        Save calendar to .ics file.
        
        Args:
            calendar: ics.Calendar object
            filepath: Output file path
            
        Returns:
            Path to saved file
        """
        with open(filepath, 'w') as f:
            f.writelines(calendar)
        return filepath

    @staticmethod
    def create_progression_calendar(
        verse_reference: str,
        verse_initials_list: list,
        start_date: datetime,
        progression_days: int = 7
    ) -> Calendar:
        """
        Create calendar with progressive memorization tasks.
        
        Args:
            verse_reference: e.g., "Ephesians 3:17-19"
            verse_initials_list: List of verse initials for each week
            start_date: Starting date (typically Sunday)
            progression_days: Days between progression steps (default 7)
            
        Returns:
            ics.Calendar object with all tasks
        """
        events = []
        current_date = start_date
        
        for i, initials in enumerate(verse_initials_list, 1):
            title = f"Memory: {verse_reference} - Week {i}"
            event = CalendarGenerator.generate_ics_event(
                title=title,
                description=initials,
                start_date=current_date,
                duration_days=progression_days
            )
            events.append(event)
            current_date += timedelta(days=progression_days)
        
        return CalendarGenerator.generate_calendar(events)
