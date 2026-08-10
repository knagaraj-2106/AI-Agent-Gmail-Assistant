from services.gmail_service import GmailService
from services.summary_service import SummaryService

gmail = GmailService()
summary_service = SummaryService()

emails = gmail.get_recent_email_details(1)

email = emails[0]

summary = summary_service.summarize_email(
    sender=email["from"],
    subject=email["subject"],
    body=email["body"] or email["snippet"],
)

print("=" * 70)
print("EMAIL SUMMARY")
print("=" * 70)

print(summary)