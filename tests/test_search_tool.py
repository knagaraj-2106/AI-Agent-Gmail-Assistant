from tools.gmail_tools import search_gmail

result = search_gmail.invoke(
    {
        "query": "from:google"
    }
)

print(result)