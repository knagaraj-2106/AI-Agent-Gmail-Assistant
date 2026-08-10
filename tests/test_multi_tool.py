from tools.gmail_tools import search_and_extract_action_items


query = "from:hdfcbank"


print("=" * 70)
print("TESTING SEARCH + ACTION ITEM TOOL")
print("=" * 70)


result = search_and_extract_action_items.invoke(
    {
        "query": query
    }
)


print("\n" + "=" * 70)
print("RESULT")
print("=" * 70)

print(result)