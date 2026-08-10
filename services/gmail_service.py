"""
gmail_service.py

Production Gmail Service

Responsibilities:
- Connect to Gmail
- Read Inbox
- Count unread emails
- Fetch recent emails
- Read complete email body
"""

import base64
from email.header import decode_header

from services.auth_service import GmailAuthService


class GmailService:

    def __init__(self):
        self.service = GmailAuthService().authenticate()

    # ---------------------------------------------------
    # Gmail Profile
    # ---------------------------------------------------

    def get_profile(self):
        """
        Returns Gmail account profile.
        """

        return (
            self.service.users()
            .getProfile(userId="me")
            .execute()
        )

    # ---------------------------------------------------
    # Unread Count
    # ---------------------------------------------------

    def get_unread_count(self):

        results = (
            self.service.users()
            .messages()
            .list(
                userId="me",
                labelIds=["UNREAD"],
            )
            .execute()
        )

        messages = results.get("messages", [])

        return len(messages)

    # ---------------------------------------------------
    # Recent Emails
    # ---------------------------------------------------

    def list_recent_emails(self, max_results=10):

        results = (
            self.service.users()
            .messages()
            .list(
                userId="me",
                maxResults=max_results,
            )
            .execute()
        )

        return results.get("messages", [])


    def search_emails(self, query: str, max_results: int = 10):
        """
        Search Gmail using Gmail search operators.

        Examples:
            from:google
            from:hdfcbank
            subject:invoice
            has:attachment
            is:unread
            newer_than:1d

        Returns:
            A list of emails containing:
            - id
            - from
            - subject
            - date
            - snippet
            - body
        """

        results = (
            self.service.users()
            .messages()
            .list(
                userId="me",
                q=query,
                maxResults=max_results,
            )
            .execute()
        )

        messages = results.get("messages", [])

        emails = []

        for message in messages:

            email = (
                self.service.users()
                .messages()
                .get(
                    userId="me",
                    id=message["id"],
                    format="full",
                )
                .execute()
            )

            payload = email.get("payload", {})

            headers = payload.get("headers", [])

            sender = self.get_header(headers, "From")
            subject = self.get_header(headers, "Subject")
            date = self.get_header(headers, "Date")

            body = self.get_email_body(payload)

            emails.append(
                {
                    "id": message["id"],
                    "from": sender,
                    "subject": subject,
                    "date": date,
                    "snippet": email.get("snippet", ""),
                    "body": body,
                }
            )

        return emails

        # ---------------------------------------------------
    # Search Emails - Full Details
    # ---------------------------------------------------

    def search_email_details(
        self,
        query: str,
        max_results: int = 10
    ):
        """
        Search Gmail and return complete email details.
        """

        results = (
            self.service.users()
            .messages()
            .list(
                userId="me",
                q=query,
                maxResults=max_results,
            )
            .execute()
        )

        messages = results.get(
            "messages",
            []
        )

        emails = []

        for message in messages:

            email = self.get_email(
                message["id"]
            )

            payload = email.get(
                "payload",
                {}
            )

            headers = payload.get(
                "headers",
                []
            )

            emails.append(
                {
                    "id": message["id"],
                    "from": self.get_header(
                        headers,
                        "From"
                    ),
                    "subject": self.get_header(
                        headers,
                        "Subject"
                    ),
                    "date": self.get_header(
                        headers,
                        "Date"
                    ),
                    "snippet": email.get(
                        "snippet",
                        ""
                    ),
                    "body": self.get_email_body(
                        payload
                    ),
                }
            )

        return emails


    def get_unread_email_details(self, max_results=10):
        """
        Returns detailed information for unread emails.
        """

        emails = []

        unread_messages = (
            self.service.users()
            .messages()
            .list(
                userId="me",
                labelIds=["UNREAD"],
                maxResults=max_results,
            )
            .execute()
            .get("messages", [])
        )

        for msg in unread_messages:

            email = self.get_email(msg["id"])

            payload = email["payload"]

            headers = payload.get("headers", [])

            emails.append(
                {
                    "id": msg["id"],
                    "from": self.get_header(headers, "From"),
                    "subject": self.get_header(headers, "Subject"),
                    "date": self.get_header(headers, "Date"),
                    "snippet": email.get("snippet", ""),
                    "body": self.get_email_body(payload),
                }
            )

        return emails
    # ---------------------------------------------------
    # Read Full Email
    # ---------------------------------------------------

    def get_email(self, message_id):

        return (
            self.service.users()
            .messages()
            .get(
                userId="me",
                id=message_id,
                format="full",
            )
            .execute()
        )

    # ---------------------------------------------------
    # Header Extraction
    # ---------------------------------------------------

    @staticmethod
    def get_header(headers, name):

        for header in headers:

            if header["name"].lower() == name.lower():

                value, encoding = decode_header(header["value"])[0]

                if isinstance(value, bytes):

                    value = value.decode(
                        encoding if encoding else "utf-8",
                        errors="ignore",
                    )

                return value

        return ""

    # ---------------------------------------------------
    # Email Body Extraction
    # ---------------------------------------------------

    def get_email_body(self, payload):

        body = ""

        if "parts" in payload:

            for part in payload["parts"]:

                if part.get("mimeType") == "text/plain":

                    data = part["body"].get("data")

                    if data:

                        body = base64.urlsafe_b64decode(
                            data
                        ).decode("utf-8", errors="ignore")

                        return body

        else:

            data = payload["body"].get("data")

            if data:

                body = base64.urlsafe_b64decode(
                    data
                ).decode("utf-8", errors="ignore")

        return body

    # ---------------------------------------------------
    # Email Summary Data
    # ---------------------------------------------------

    def get_recent_email_details(self, max_results=10):

        emails = []

        messages = self.list_recent_emails(max_results)

        for msg in messages:

            email = self.get_email(msg["id"])

            payload = email["payload"]

            headers = payload.get("headers", [])

            emails.append(
                {
                    "id": msg["id"],
                    "from": self.get_header(headers, "From"),
                    "subject": self.get_header(headers, "Subject"),
                    "date": self.get_header(headers, "Date"),
                    "snippet": email.get("snippet", ""),
                    "body": self.get_email_body(payload),
                }
            )

        return emails