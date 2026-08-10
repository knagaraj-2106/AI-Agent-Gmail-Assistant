"""
test_graph_action_search.py

Tests the complete LangGraph workflow
for Gmail search + action item extraction.
"""

import uuid

from langchain_core.messages import HumanMessage

from agents.graph import graph


# -------------------------------------------------------
# Create conversation/thread ID
# -------------------------------------------------------

thread_id = str(uuid.uuid4())


# -------------------------------------------------------
# LangGraph configuration
# -------------------------------------------------------

config = {
    "configurable": {
        "thread_id": thread_id
    }
}


# -------------------------------------------------------
# User question
# -------------------------------------------------------

question = """
Search my HDFC Bank emails and tell me what action items
I need to take.
"""


print("=" * 70)
print("TESTING LANGGRAPH ACTION SEARCH")
print("=" * 70)

print("\nThread ID:")
print(thread_id)


# -------------------------------------------------------
# Run LangGraph
# -------------------------------------------------------

result = graph.invoke(
    {
        "messages": [
            HumanMessage(
                content=question
            )
        ]
    },
    config=config
)


# -------------------------------------------------------
# Final response
# -------------------------------------------------------

print("\n" + "=" * 70)
print("FINAL RESPONSE")
print("=" * 70)


final_message = result["messages"][-1]

print(final_message.content)