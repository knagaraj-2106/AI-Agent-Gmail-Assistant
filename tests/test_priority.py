from services.gmail_service import GmailService
from services.summary_service import SummaryService

gmail = GmailService()
summary = SummaryService()

emails = gmail.get_recent_email_details(10)

result = summary.detect_priority_emails(emails)

print(result)