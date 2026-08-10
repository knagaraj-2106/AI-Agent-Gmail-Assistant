"""
test_agent_search.py

Tests whether the AI agent can intelligently
use the Gmail search tool.
"""

from langchain_core.messages import HumanMessage

from agents.agent import agent


question = "Find my emails from Google"


response = agent.invoke(
    [
        HumanMessage(content=question)
    ]
)


print("=" * 60)
print("AGENT SEARCH TEST")
print("=" * 60)

print(response)

print("\n" + "=" * 60)
print("TOOL CALLS")
print("=" * 60)

print(response.tool_calls)