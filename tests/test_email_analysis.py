from services.gmail_service import GmailService
from services.email_analysis_service import EmailAnalysisService


gmail = GmailService()

analysis_service = EmailAnalysisService()


print("=" * 70)
print("TESTING EMAIL ANALYSIS SERVICE")
print("=" * 70)


emails = gmail.search_email_details(
    query="from:hdfcbank",
    max_results=5
)


print(
    f"\nEmails retrieved: {len(emails)}"
)


result = analysis_service.extract_action_items(
    emails
)


print("\n" + "=" * 70)
print("ACTION ITEMS")
print("=" * 70)

print(result)