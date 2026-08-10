"""
test_deadlines_tool.py

Tests the extract_deadlines_and_meetings LangChain tool.
"""

from tools.gmail_tools import extract_deadlines_and_meetings


print("=" * 60)
print("DEADLINES AND MEETINGS TOOL TEST")
print("=" * 60)

result = extract_deadlines_and_meetings.invoke({})

print(result)