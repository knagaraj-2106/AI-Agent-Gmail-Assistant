from services.gmail_service import GmailService

gmail = GmailService()

emails = gmail.get_unread_email_details(5)

for i, email in enumerate(emails, start=1):

    print("=" * 60)
    print(f"Email {i}")
    print("=" * 60)
    print("From   :", email["from"])
    print("Subject:", email["subject"])
    print("Date   :", email["date"])
    print("Body   :", email["body"][:300])
    print()