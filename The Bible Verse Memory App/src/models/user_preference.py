"""User preference model for persistent storage"""
from dataclasses import dataclass, asdict
from typing import Optional
from datetime import datetime
import json
import os


@dataclass
class UserPreference:
    """Stores user's persistent preferences across sessions"""
    start_date: Optional[str] = None  # ISO format date string
    start_time: str = "06:00"  # HH:MM format, default 6:00 AM
    bible_version: str = "Recovery Version"
    progression_interval_days: int = 7  # Default 7 days
    output_preference: Optional[str] = None  # 'google_tasks', 'ics_download', 'email', 'both'
    user_email: Optional[str] = None  # For email delivery
    last_updated: Optional[str] = None

    def to_dict(self):
        """Convert to dictionary"""
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict):
        """Create from dictionary"""
        return cls(**{k: v for k, v in data.items() if k in cls.__dataclass_fields__})

    def save(self, filepath: str = "data/user_preferences.json"):
        """Save preferences to JSON file"""
        os.makedirs(os.path.dirname(filepath) or '.', exist_ok=True)
        self.last_updated = datetime.now().isoformat()
        with open(filepath, 'w') as f:
            json.dump(self.to_dict(), f, indent=2)

    @classmethod
    def load(cls, filepath: str = "data/user_preferences.json"):
        """Load preferences from JSON file"""
        if not os.path.exists(filepath):
            return cls()
        with open(filepath, 'r') as f:
            data = json.load(f)
        return cls.from_dict(data)
