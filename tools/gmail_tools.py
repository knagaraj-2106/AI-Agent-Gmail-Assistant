"""
gmail_tools.py

LangChain tools for Gmail operations.
"""

from langchain.tools import tool
from services.email_analysis_service import (
    EmailAnalysisService
)
from services.gmail_service import GmailService
from services.summary_service import SummaryService


gmail_service = GmailService()
summary_service = SummaryService()
email_analysis_service = EmailAnalysisService()


# ---------------------------------------------------------
# Unread Email Count
# ---------------------------------------------------------

@tool
def get_unread_email_count() -> str:
    """
    Returns the number of unread emails.
    """

    count = gmail_service.get_unread_count()

    return f"You have {count} unread emails."


# ---------------------------------------------------------
# Recent Emails
# ---------------------------------------------------------

@tool
def get_recent_emails() -> str:
    """
    Returns recent emails.
    """

    emails = gmail_service.get_recent_email_details(5)

    if not emails:
        return "No emails found."

    output = []

    for i, email in enumerate(emails, start=1):

        output.append(
            f"""
Email {i}

From: {email['from']}
Subject: {email['subject']}
Date: {email['date']}
"""
        )

    return "\n".join(output)


# ---------------------------------------------------------
# Summarize Latest Email
# ---------------------------------------------------------

@tool
def summarize_latest_email() -> str:
    """
    Summarizes the latest email.
    """

    emails = gmail_service.get_recent_email_details(1)

    if not emails:
        return "No emails available."

    email = emails[0]

    summary = summary_service.summarize_email(
        sender=email["from"],
        subject=email["subject"],
        body=email["body"] or email["snippet"],
    )

    return summary


# ---------------------------------------------------------
# Summarize Unread Emails
# ---------------------------------------------------------

@tool
def summarize_unread_emails() -> str:
    """
    Summarizes unread emails.
    """

    emails = gmail_service.get_unread_email_details(10)

    if not emails:
        return "No unread emails."

    return summary_service.summarize_multiple_emails(emails)


# ---------------------------------------------------------
# Search Gmail
# ---------------------------------------------------------

@tool
def search_gmail(query: str) -> str:
    """
    Search Gmail using Gmail search operators.

    Examples:
    - from:google
    - from:hdfcbank
    - subject:invoice
    - has:attachment
    - newer_than:1d
    - is:unread
    """

    emails = gmail_service.search_emails(query)

    if not emails:
        return "No matching emails found."

    output = []

    for i, email in enumerate(emails, start=1):

        output.append(
            f"""
Email {i}

From: {email['from']}
Subject: {email['subject']}
Date: {email['date']}
Snippet: {email['snippet']}
"""
        )

    return "\n".join(output)


# ---------------------------------------------------------
# Extract Action Items
# ---------------------------------------------------------

@tool
def extract_action_items() -> str:
    """
    Extracts actionable tasks from recent emails.
    """

    emails = gmail_service.get_recent_email_details(10)

    if not emails:
        return "No emails available."

    return summary_service.extract_action_items(emails)


# ---------------------------------------------------------
# Detect Deadlines and Meetings
# ---------------------------------------------------------

@tool
def extract_deadlines_and_meetings() -> str:
    """
    Extracts meetings, interviews, deadlines,
    and important scheduled events from recent emails.
    """

    emails = gmail_service.get_recent_email_details(10)

    if not emails:
        return "No emails available."

    return summary_service.extract_deadlines_and_meetings(emails)

@tool
def search_and_extract_action_items(
    query: str
) -> str:
    """
    Search Gmail using a Gmail search query
    and extract action items from the matching
    emails.
    """

    emails = gmail_service.search_email_details(
        query=query,
        max_results=10
    )

    if not emails:
        return "No matching emails were found."

    return email_analysis_service.extract_action_items(
        emails
    )