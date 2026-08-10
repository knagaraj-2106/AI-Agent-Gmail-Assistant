from services.gmail_service import GmailService


gmail = GmailService()


query = "newer_than:7d"


print("=" * 70)
print("TESTING SEARCH EMAIL DETAILS")
print("=" * 70)

emails = gmail.search_email_details(
    query=query,
    max_results=5
)


print(f"\nEmails found: {len(emails)}")


for index, email in enumerate(
    emails,
    start=1
):

    print("\n" + "=" * 70)

    print(f"EMAIL {index}")

    print("=" * 70)

    print("ID      :", email["id"])

    print("From    :", email["from"])

    print("Subject :", email["subject"])

    print("Date    :", email["date"])

    print("Snippet :", email["snippet"])

    print("\nBody:")
    print(email["body"][:1000])