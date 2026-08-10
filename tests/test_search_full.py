"""
test_search_full.py

Tests Gmail search with full email body.
"""

from services.gmail_service import GmailService


gmail = GmailService()

emails = gmail.search_emails(
    "from:google",
    max_results=3
)

print("=" * 60)
print("FULL GMAIL SEARCH TEST")
print("=" * 60)

if not emails:

    print("No emails found.")

else:

    for i, email in enumerate(emails, start=1):

        print("\n" + "=" * 60)
        print(f"EMAIL {i}")
        print("=" * 60)

        print("ID      :", email["id"])
        print("FROM    :", email["from"])
        print("SUBJECT :", email["subject"])
        print("DATE    :", email["date"])
        print("SNIPPET :", email["snippet"])

        print("\nBODY:")
        print(email["body"][:1000])