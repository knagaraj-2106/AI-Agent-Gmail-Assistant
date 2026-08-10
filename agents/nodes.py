"""
nodes.py

Defines the LangGraph nodes.
"""

from langgraph.prebuilt import ToolNode

from agents.agent import agent, TOOLS


# ---------------------------------------------------------
# Tool Node
# ---------------------------------------------------------

tool_node = ToolNode(TOOLS)


# ---------------------------------------------------------
# LLM Node
# ---------------------------------------------------------

def chatbot(state):
    """
    Invokes GPT-4o-mini.

    The LLM decides whether to:

    • Answer directly
    • Call one of the Gmail tools
    """

    response = agent.invoke(
        state["messages"]
    )

    return {
        "messages": [response]
    }