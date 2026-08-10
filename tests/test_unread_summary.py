from services.gmail_service import GmailService
from services.summary_service import SummaryService

gmail = GmailService()
summary = SummaryService()

emails = gmail.get_unread_email_details(5)

result = summary.summarize_multiple_emails(emails)

print(result)