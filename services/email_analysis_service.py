"""
email_analysis_service.py

Provides LLM-based analysis of Gmail emails.
"""

from langchain_core.messages import HumanMessage

from models.llm import llm


class EmailAnalysisService:

    def extract_action_items(self, emails):
        """
        Extract action items from a collection of emails.
        """

        if not emails:
            return "No emails available for analysis."

        email_text = ""

        for index, email in enumerate(
            emails,
            start=1
        ):

            email_text += f"""
EMAIL {index}

From:
{email.get("from", "")}

Subject:
{email.get("subject", "")}

Date:
{email.get("date", "")}

Body:
{email.get("body", "")}

----------------------------------------
"""

        prompt = f"""
You are an intelligent Gmail assistant.

Analyze the emails below and identify genuine
action items that the user needs to perform.

For every action item, provide:

1. Action
2. Sender
3. Subject
4. Deadline
5. Priority

Priority should be:

- High
- Medium
- Low

Important rules:

- Do not invent information.
- Do not invent deadlines.
- If a deadline is not explicitly mentioned,
  write "Not mentioned".
- Ignore promotional emails unless they
  contain a genuine action the user needs to take.
- If there are no action items, clearly say so.

Emails:

{email_text}
"""

        response = llm.invoke(
            [
                HumanMessage(
                    content=prompt
                )
            ]
        )

        return response.content