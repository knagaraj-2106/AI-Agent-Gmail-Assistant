"""
Authentication service for Gmail API.

Responsibilities:
- Authenticate using OAuth 2.0
- Generate token.json on first login
- Refresh expired tokens automatically
- Return an authenticated Gmail API service object
"""

from pathlib import Path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly"
]


class GmailAuthService:
    """
    Handles Gmail OAuth authentication.
    """

    def __init__(self):
        project_root = Path(__file__).resolve().parent.parent

        self.credentials_file = (
            project_root / "credentials" / "credentials.json"
        )

        self.token_file = (
            project_root / "credentials" / "token.json"
        )

    def authenticate(self):
        """
        Authenticate the user and return a Gmail service object.
        """

        creds = None

        if self.token_file.exists():
            creds = Credentials.from_authorized_user_file(
                str(self.token_file),
                SCOPES,
            )

        if not creds or not creds.valid:

            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())

            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    str(self.credentials_file),
                    SCOPES,
                )

                creds = flow.run_local_server(port=0)

            self.token_file.write_text(creds.to_json())

        gmail_service = build(
            "gmail",
            "v1",
            credentials=creds,
        )

        return gmail_service