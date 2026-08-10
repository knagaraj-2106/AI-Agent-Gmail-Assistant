from services.gmail_service import GmailService
from services.summary_service import SummaryService


gmail = GmailService()
summary = SummaryService()

emails = gmail.get_recent_email_details(10)

result = summary.extract_deadlines_and_meetings(emails)

print("=" * 60)
print("DEADLINES AND MEETINGS")
print("=" * 60)

print(result)