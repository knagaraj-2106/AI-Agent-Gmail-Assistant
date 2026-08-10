import uuid

from langchain_core.messages import HumanMessage

from agents.graph import graph


thread_id = str(uuid.uuid4())

config = {
    "configurable": {
        "thread_id": thread_id
    }
}


# -------------------------------------------------------
# First question
# -------------------------------------------------------

question_1 = """
Find my HDFC Bank emails and identify the action items.
"""


result_1 = graph.invoke(
    {
        "messages": [
            HumanMessage(content=question_1)
        ]
    },
    config=config
)


print("=" * 70)
print("FIRST RESPONSE")
print("=" * 70)

print(
    result_1["messages"][-1].content
)


# -------------------------------------------------------
# Second question
# -------------------------------------------------------

question_2 = """
Which of those actions are high priority?
"""


result_2 = graph.invoke(
    {
        "messages": [
            HumanMessage(content=question_2)
        ]
    },
    config=config
)


print("\n" + "=" * 70)
print("SECOND RESPONSE")
print("=" * 70)

print(
    result_2["messages"][-1].content
)