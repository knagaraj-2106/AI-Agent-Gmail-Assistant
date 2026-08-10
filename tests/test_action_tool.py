"""
test_action_tool.py

Tests the extract_action_items LangChain tool.
"""

from tools.gmail_tools import extract_action_items


print("=" * 60)
print("ACTION ITEMS TOOL TEST")
print("=" * 60)

result = extract_action_items.invoke({})

print(result)