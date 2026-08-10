from tools.gmail_tools import (
    get_recent_emails,
    get_unread_email_count,
    summarize_latest_email,
)

print("=" * 60)
print("Unread Emails")
print("=" * 60)

print(get_unread_email_count.invoke({}))

print()

print("=" * 60)
print("Recent Emails")
print("=" * 60)

print(get_recent_emails.invoke({}))

print()

print("=" * 60)
print("Summary")
print("=" * 60)

print(summarize_latest_email.invoke({}))