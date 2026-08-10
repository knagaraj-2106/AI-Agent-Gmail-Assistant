"""
test_memory.py

Tests LangGraph conversation memory.
"""

from langchain_core.messages import HumanMessage

from agents.graph import graph


# -------------------------------------------------------
# Conversation ID
# -------------------------------------------------------

config = {
    "configurable": {
        "thread_id": "gmail-test-user-1"
    }
}


# =======================================================
# QUESTION 1
# =======================================================

question_1 = "Find my emails from HDFC Bank"


print("=" * 60)
print("QUESTION 1")
print("=" * 60)

print(question_1)


result_1 = graph.invoke(
    {
        "messages": [
            HumanMessage(
                content=question_1
            )
        ]
    },
    config=config
)


print("\nANSWER 1")
print("=" * 60)

print(
    result_1["messages"][-1].content
)


# =======================================================
# QUESTION 2
# =======================================================

question_2 = "Which of those emails are unread?"


print("\n" + "=" * 60)
print("QUESTION 2")
print("=" * 60)

print(question_2)


result_2 = graph.invoke(
    {
        "messages": [
            HumanMessage(
                content=question_2
            )
        ]
    },
    config=config
)


print("\nANSWER 2")
print("=" * 60)

print(
    result_2["messages"][-1].content
)