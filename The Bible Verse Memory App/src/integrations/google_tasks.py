"""Google Tasks integration"""
from typing import Optional, List
import os


class GoogleTasksService:
    """Manages Google Tasks integration"""

    def __init__(self, credentials_path: Optional[str] = None):
        """
        Initialize Google Tasks service.
        
        Args:
            credentials_path: Path to Google OAuth credentials file
        """
        self.credentials_path = credentials_path
        self.service = None
        self.daily_bread_list_id = None

    def authenticate(self) -> bool:
        """
        Authenticate with Google Tasks API.
        
        Returns:
            True if successful
        """
        try:
            from google.auth.transport.requests import Request
            from google.oauth2.service_account import Credentials
            from google_auth_oauthlib.flow import InstalledAppFlow
            
            SCOPES = ['https://www.googleapis.com/auth/tasks']
            
            # This is a placeholder; full OAuth flow implementation needed
            print("Google Tasks authentication not yet fully implemented")
            return False
        
        except Exception as e:
            print(f"Error authenticating with Google Tasks: {e}")
            return False

    def verify_daily_bread_list(self) -> Optional[str]:
        """
        Verify that "Daily Bread" task list exists.
        
        Returns:
            Task list ID if found, None otherwise
        """
        try:
            if not self.service:
                return None
            
            tasklists = self.service.tasklists().list().execute()
            
            for tasklist in tasklists.get('items', []):
                if tasklist['title'] == 'Daily Bread':
                    self.daily_bread_list_id = tasklist['id']
                    return tasklist['id']
            
            return None
        
        except Exception as e:
            print(f"Error verifying Daily Bread list: {e}")
            return None

    def create_task(
        self,
        task_list_id: str,
        title: str,
        notes: str,
        due_date: str
    ) -> Optional[str]:
        """
        Create a task in Google Tasks.
        
        Args:
            task_list_id: Target task list ID
            title: Task title
            notes: Task notes (verse initials)
            due_date: Due date (ISO format)
            
        Returns:
            Task ID if successful, None otherwise
        """
        try:
            if not self.service:
                return None
            
            task = {
                'title': title,
                'notes': notes,
                'due': due_date
            }
            
            result = self.service.tasks().insert(
                tasklist=task_list_id,
                body=task
            ).execute()
            
            return result.get('id')
        
        except Exception as e:
            print(f"Error creating task: {e}")
            return None

    def create_recurring_task(
        self,
        task_list_id: str,
        title: str,
        notes: str,
        start_date: str,
        num_days: int
    ) -> List[str]:
        """
        Create a recurring daily task.
        
        Args:
            task_list_id: Target task list ID
            title: Task title
            notes: Task notes
            start_date: Start date (ISO format)
            num_days: Number of days to repeat
            
        Returns:
            List of created task IDs
        """
        task_ids = []
        
        try:
            from datetime import datetime, timedelta
            
            current_date = datetime.fromisoformat(start_date).date()
            
            for _ in range(num_days):
                task_id = self.create_task(
                    task_list_id=task_list_id,
                    title=title,
                    notes=notes,
                    due_date=current_date.isoformat()
                )
                
                if task_id:
                    task_ids.append(task_id)
                
                current_date += timedelta(days=1)
        
        except Exception as e:
            print(f"Error creating recurring tasks: {e}")
        
        return task_ids

    def delete_task(self, task_list_id: str, task_id: str) -> bool:
        """
        Delete a task from Google Tasks.
        
        Args:
            task_list_id: Task list ID
            task_id: Task ID to delete
            
        Returns:
            True if successful
        """
        try:
            if not self.service:
                return False
            
            self.service.tasks().delete(
                tasklist=task_list_id,
                task=task_id
            ).execute()
            
            return True
        
        except Exception as e:
            print(f"Error deleting task: {e}")
            return False
