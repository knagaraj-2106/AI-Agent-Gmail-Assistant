"""
gmail_mcp_tools.py

Registers Gmail tools with the MCP Server.
"""

from services.gmail_service import GmailService
from services.summary_service import EmailSummaryService

from mcp.server import mcp

gmail = GmailService()
summarizer = EmailSummaryService()


@mcp.tool()
def get_unread_email_count() -> int:
    """
    Returns the total unread email count.
    """

    return gmail.get_unread_count()


@mcp.tool()
def get_recent_emails(limit: int = 5) -> list:
    """
    Returns recent emails.
    """

    return gmail.get_recent_emails(limit)


@mcp.tool()
def summarize_latest_email() -> str:
    """
    Returns GPT summary of latest email.
    """

    latest = gmail.get_recent_emails(1)

    if not latest:
        return "Inbox is empty."

    return summarizer.summarize_email(
        latest[0]
    )