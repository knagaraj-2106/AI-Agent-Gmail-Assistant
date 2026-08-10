from langchain_core.messages import HumanMessage

from agents.agent import agent


question = """
Search my HDFC Bank emails and identify the important
action items I need to take.
"""


print("=" * 70)
print("TESTING AGENT TOOL SELECTION")
print("=" * 70)

response = agent.invoke(
    [
        HumanMessage(
            content=question
        )
    ]
)


print("\nAI RESPONSE:")
print(response)

print("\n" + "=" * 70)
print("TOOL CALLS")
print("=" * 70)

print(response.tool_calls)