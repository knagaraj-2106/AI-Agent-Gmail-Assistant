"""
test_graph_search.py

Tests the complete LangGraph Gmail agent.
"""

from langchain_core.messages import HumanMessage

from agents.graph import graph


question = "Find my emails from Google"


print("=" * 60)
print("USER QUESTION")
print("=" * 60)

print(question)


result = graph.invoke(
    {
        "messages": [
            HumanMessage(content=question)
        ]
    }
)


print("\n" + "=" * 60)
print("LANGGRAPH RESULT")
print("=" * 60)


for message in result["messages"]:

    print("\nMessage Type:", type(message).__name__)

    if hasattr(message, "content") and message.content:
        print("Content:")
        print(message.content)

    if hasattr(message, "tool_calls") and message.tool_calls:
        print("Tool Calls:")
        print(message.tool_calls)