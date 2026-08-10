"""
summary_service.py

Uses GPT-4o-mini to summarize emails.
"""

from langchain_core.messages import HumanMessage

from models.llm import llm


class SummaryService:

    def summarize_email(
        self,
        sender: str,
        subject: str,
        body: str,
    ) -> str:
        """
        Summarize an email using GPT-4o-mini.
        """

        prompt = f"""
You are an intelligent email assistant.

Summarize the email in 4-6 concise bullet points.

Mention:

- Sender
- Subject
- Main purpose
- Important dates
- Important action items

Sender:
{sender}

Subject:
{subject}

Email Body:
{body}
"""

        response = llm.invoke(
            [
                HumanMessage(content=prompt)
            ]
        )

        return response.content
    def summarize_multiple_emails(self, emails: list) -> str:
        """
        Summarize multiple emails into a single report.
        """

        if not emails:
            return "No emails available to summarize."

        email_text = ""

        for i, email in enumerate(emails, start=1):

            email_text += f"""
    =========================
    Email {i}

    Sender:
    {email['from']}

    Subject:
    {email['subject']}

    Date:
    {email['date']}

    Body:
    {email['body'] or email['snippet']}
    """

        prompt = f"""
    You are an intelligent Gmail Assistant.

    Below are multiple unread emails.

    Create a concise report.

    For each email mention:

    • Sender
    • Subject
    • One-line summary

    Then provide:

    1. Important action items
    2. Important dates
    3. Urgent emails (if any)
    4. Overall summary

    Emails:

    {email_text}
    """

        response = llm.invoke(
            [
                HumanMessage(content=prompt)
            ]
        )

        return response.content
    def detect_priority_emails(self, emails: list) -> str:
        """
        Detect high-priority emails using GPT.
        """

        if not emails:
            return "No emails found."

        email_text = ""

        for i, email in enumerate(emails, start=1):

            email_text += f"""
    Email {i}

    Sender:
    {email['from']}

    Subject:
    {email['subject']}

    Date:
    {email['date']}

    Body:
    {email['body'] or email['snippet']}
    """

        prompt = f"""
    You are an AI Executive Email Assistant.

    Analyze the following emails.

    Classify every email into ONE category:

    🔴 HIGH PRIORITY
    Examples:
    - Security alerts
    - Interview invitations
    - Payment failures
    - Bank fraud
    - OTP
    - Password reset
    - Meetings today
    - Deadlines

    🟡 MEDIUM PRIORITY
    Examples:
    - Bank transactions
    - Team updates
    - GitHub notifications
    - Delivery updates

    🟢 LOW PRIORITY
    Examples:
    - Promotions
    - Newsletters
    - Marketing
    - Advertisements

    Return your answer in this format:

    HIGH PRIORITY

    • Sender
    • Subject
    • Why it is urgent

    --------------------

    MEDIUM PRIORITY

    ...

    --------------------

    LOW PRIORITY

    ...

    Emails:

    {email_text}
    """

        response = llm.invoke(
            [
                HumanMessage(content=prompt)
            ]
        )

        return response.content
    def extract_action_items(self, emails: list) -> str:
        """
        Extract actionable tasks from emails using GPT.
        """

        if not emails:
            return "No emails found."

        email_text = ""

        for i, email in enumerate(emails, start=1):

            email_text += f"""
    =========================
    Email {i}

    Sender:
    {email['from']}

    Subject:
    {email['subject']}

    Date:
    {email['date']}

    Body:
    {email['body'] or email['snippet']}
    """

        prompt = f"""
    You are an intelligent executive email assistant.

    Analyze the emails below and identify ONLY actions that
    the user may need to take.

    Examples of actions:

    - Reply to an email
    - Confirm a meeting
    - Attend an interview
    - Complete an assessment
    - Make a payment
    - Verify a transaction
    - Reset a password
    - Review a security alert
    - Submit a document
    - Complete a registration
    - Respond before a deadline

    Do NOT consider newsletters, advertisements, promotions,
    or purely informational emails as action items unless
    they explicitly require user action.

    For every action item provide:

    1. Action
    2. Sender
    3. Related email subject
    4. Deadline, if mentioned
    5. Priority

    Use this format:

    ACTION ITEMS

    1. Action:
    Sender:
    Subject:
    Deadline:
    Priority:

    2. Action:
    Sender:
    Subject:
    Deadline:
    Priority:

    If there are no actionable emails, say:

    "No actionable items found."

    Emails:

    {email_text}
    """

        response = llm.invoke(
            [
                HumanMessage(content=prompt)
            ]
        )

        return response.content

    def extract_deadlines_and_meetings(self, emails: list) -> str:
        """
        Extract meetings, deadlines, and scheduled events from emails.
        """

        if not emails:
            return "No emails found."

        email_text = ""

        for i, email in enumerate(emails, start=1):

            email_text += f"""
    =========================
    Email {i}

    Sender:
    {email['from']}

    Subject:
    {email['subject']}

    Date:
    {email['date']}

    Body:
    {email['body'] or email['snippet']}
    """

        prompt = f"""
    You are an intelligent executive email assistant.

    Analyze the emails below and identify:

    1. Meetings
    2. Interviews
    3. Appointments
    4. Deadlines
    5. Assessments
    6. Events
    7. Scheduled calls
    8. Any other important date/time commitments

    Ignore:
    - Marketing emails
    - Advertisements
    - Newsletters
    - Promotional offers
    - General informational emails

    For every detected event provide:

    Event:
    Sender:
    Subject:
    Date:
    Time:
    Deadline:
    Action Required:
    Priority:

    If the information is not available, write:
    Not mentioned

    Group the result into:

    UPCOMING MEETINGS

    DEADLINES

    INTERVIEWS

    OTHER IMPORTANT EVENTS

    If nothing relevant is found, say:

    "No upcoming meetings or deadlines found."

    Emails:

    {email_text}
    """

        response = llm.invoke(
            [
                HumanMessage(content=prompt)
            ]
        )

        return response.content