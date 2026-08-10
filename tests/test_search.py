from services.gmail_service import GmailService

gmail = GmailService()

emails = gmail.search_emails("from:google")

for email in emails:
    print("=" * 60)
    print("From   :", email["from"])
    print("Subject:", email["subject"])
    print("Date   :", email["date"])
    print("Snippet:", email["snippet"])