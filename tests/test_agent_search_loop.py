"""
test_agent_search_loop.py

Tests the complete AI Gmail search loop.

Flow:

User Question
      ↓
GPT-4o-mini
      ↓
Tool Selection
      ↓
Gmail Search
      ↓
Tool Result
      ↓
GPT-4o-mini
      ↓
Final Answer
"""

from langchain_core.messages import HumanMessage, ToolMessage

from agents.agent import agent
from tools.gmail_tools import search_gmail


# -------------------------------------------------------
# User Question
# -------------------------------------------------------

question = "Find my emails from Google"


print("=" * 60)
print("USER QUESTION")
print("=" * 60)

print(question)


# -------------------------------------------------------
# Step 1 — Ask LLM
# -------------------------------------------------------

response = agent.invoke(
    [
        HumanMessage(content=question)
    ]
)


print("\n" + "=" * 60)
print("LLM TOOL CALL")
print("=" * 60)

print(response.tool_calls)


# -------------------------------------------------------
# Step 2 — Execute Tool
# -------------------------------------------------------

if response.tool_calls:

    tool_call = response.tool_calls[0]

    tool_name = tool_call["name"]

    tool_args = tool_call["args"]

    print("\n" + "=" * 60)
    print("EXECUTING TOOL")
    print("=" * 60)

    print("Tool :", tool_name)
    print("Args :", tool_args)


    if tool_name == "search_gmail":

        tool_result = search_gmail.invoke(
            tool_args
        )

        print("\n" + "=" * 60)
        print("GMAIL SEARCH RESULT")
        print("=" * 60)

        print(tool_result)


        # ------------------------------------------------
        # Step 3 — Send Tool Result Back To LLM
        # ------------------------------------------------

        messages = [
            HumanMessage(content=question),
            response,
            ToolMessage(
                content=tool_result,
                tool_call_id=tool_call["id"],
            ),
        ]


        final_response = agent.invoke(
            messages
        )


        print("\n" + "=" * 60)
        print("FINAL AI ANSWER")
        print("=" * 60)

        print(final_response.content)

else:

    print("\nThe LLM did not request a tool.")
    print("LLM Response:")
    print(response.content)