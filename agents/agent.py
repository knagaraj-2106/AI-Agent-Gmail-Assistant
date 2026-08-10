"""
agent.py

Creates the LangGraph AI Agent by binding GPT-4o-mini
with all available Gmail tools.
"""

from models.llm import llm

from tools.gmail_tools import (
    get_recent_emails,
    get_unread_email_count,
    summarize_latest_email,
    summarize_unread_emails,
    search_gmail,
    extract_action_items,
    extract_deadlines_and_meetings,
    search_and_extract_action_items,
)


TOOLS = [
    get_unread_email_count,
    get_recent_emails,
    summarize_latest_email,
    summarize_unread_emails,
    search_gmail,
    extract_action_items,
    extract_deadlines_and_meetings,
    search_and_extract_action_items,
]


SYSTEM_PROMPT = """
You are an intelligent Gmail AI Assistant.

You help users search, understand, summarize,
and analyze their Gmail emails.

You have access to Gmail tools.

IMPORTANT TOOL-USAGE RULES:

1. Use get_unread_email_count when the user asks
   about the number of unread emails.

2. Use get_recent_emails when the user asks for
   recent/latest emails.

3. Use summarize_latest_email when the user asks
   to summarize the latest email.

4. Use summarize_unread_emails when the user asks
   to summarize unread emails.

5. Use search_gmail when the user asks to find,
   search, filter, or locate specific emails.

6. Use extract_action_items when the user asks
   what actions they need to take.

7. Use extract_deadlines_and_meetings when the user
   asks about meetings, interviews, appointments,
   deadlines, or scheduled events.

GMAIL SEARCH QUERY EXAMPLES:

User:
"Find emails from Google"

Use:
from:google

User:
"Find unread emails from Google"

Use:
from:google is:unread

User:
"Find emails from HDFC"

Use:
from:hdfc

User:
"Find emails with attachments"

Use:
has:attachment

User:
"Find emails with invoice in the subject"

Use:
subject:invoice

User:
"Find emails from the last day"

Use:
newer_than:1d

User:
"Find unread emails with attachments"

Use:
is:unread has:attachment

IMPORTANT:

When searching Gmail, construct the appropriate
Gmail search query yourself.

Do NOT ask the user to provide Gmail search syntax
unless the request is genuinely ambiguous.

After receiving search results, answer the user's
question using the retrieved email information.

Do not invent email information.

If no matching emails are found, clearly say so.
"""


def create_agent_messages(messages):

    return [
        {
            "role": "system",
            "content": SYSTEM_PROMPT,
        }
    ] + messages


def invoke_agent(messages):

    return llm.bind_tools(TOOLS).invoke(
        create_agent_messages(messages)
    )


agent = type(
    "GmailAgent",
    (),
    {
        "invoke": staticmethod(invoke_agent)
    }
)