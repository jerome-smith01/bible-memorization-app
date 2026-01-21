"""Email service integration for Resend API"""
import os
from typing import Optional


class EmailService:
    """Handles email delivery via Resend API"""

    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize email service.
        
        Args:
            api_key: Resend API key (defaults to env var RESEND_API_KEY)
        """
        self.api_key = api_key or os.getenv('RESEND_API_KEY')
        if not self.api_key:
            raise ValueError("RESEND_API_KEY not provided or found in environment")

    def send_ics_attachment(
        self,
        recipient_email: str,
        subject: str,
        body: str,
        ics_filepath: str
    ) -> bool:
        """
        Send email with .ics file attachment via Resend.
        
        Args:
            recipient_email: Recipient email address
            subject: Email subject
            body: Email body text
            ics_filepath: Path to .ics calendar file
            
        Returns:
            True if successful, False otherwise
        """
        try:
            # Import here to avoid hard dependency if not using email
            from resend import Resend
            
            client = Resend(api_key=self.api_key)
            
            # Read ICS file as attachment
            with open(ics_filepath, 'rb') as f:
                ics_content = f.read()
            
            # Send email with attachment
            response = client.emails.send({
                "from": "bible-memory@resend.dev",  # Update with your domain
                "to": recipient_email,
                "subject": subject,
                "html": f"<p>{body}</p>",
                "attachments": [
                    {
                        "filename": "memorization_schedule.ics",
                        "content": ics_content,
                    }
                ]
            })
            
            return bool(response.get('id'))
        
        except Exception as e:
            print(f"Error sending email: {e}")
            return False

    def send_confirmation_email(
        self,
        recipient_email: str,
        verse_reference: str,
        progression_interval: int,
        total_weeks: int
    ) -> bool:
        """
        Send confirmation email for scheduled memorization.
        
        Args:
            recipient_email: Recipient address
            verse_reference: Bible verse reference
            progression_interval: Days between progressions
            total_weeks: Number of progression weeks
            
        Returns:
            True if successful
        """
        try:
            from resend import Resend
            
            client = Resend(api_key=self.api_key)
            
            html_body = f"""
            <h2>Bible Memorization Scheduled</h2>
            <p>Your memorization schedule has been created:</p>
            <ul>
                <li><strong>Verse:</strong> {verse_reference}</li>
                <li><strong>Progression Interval:</strong> {progression_interval} days</li>
                <li><strong>Total Duration:</strong> {total_weeks} weeks</li>
            </ul>
            <p>Check your calendar for daily reminders, or import the attached .ics file into your calendar app.</p>
            """
            
            response = client.emails.send({
                "from": "bible-memory@resend.dev",
                "to": recipient_email,
                "subject": f"Bible Memorization Scheduled: {verse_reference}",
                "html": html_body
            })
            
            return bool(response.get('id'))
        
        except Exception as e:
            print(f"Error sending confirmation email: {e}")
            return False
