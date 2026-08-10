"""
graph.py

Builds the LangGraph workflow with conversation memory.
"""

from langgraph.graph import StateGraph, START
from langgraph.prebuilt import tools_condition
from langgraph.checkpoint.memory import MemorySaver

from agents.state import AgentState
from agents.nodes import chatbot, tool_node


# -------------------------------------------------------
# Create Graph
# -------------------------------------------------------

builder = StateGraph(AgentState)


# -------------------------------------------------------
# Add Nodes
# -------------------------------------------------------

builder.add_node(
    "chatbot",
    chatbot
)

builder.add_node(
    "tools",
    tool_node
)


# -------------------------------------------------------
# Entry Point
# -------------------------------------------------------

builder.add_edge(
    START,
    "chatbot"
)


# -------------------------------------------------------
# Conditional Edge
# -------------------------------------------------------

builder.add_conditional_edges(
    "chatbot",
    tools_condition
)


# -------------------------------------------------------
# Return to Chatbot
# -------------------------------------------------------

builder.add_edge(
    "tools",
    "chatbot"
)


# -------------------------------------------------------
# Memory
# -------------------------------------------------------

memory = MemorySaver()


# -------------------------------------------------------
# Compile Graph
# -------------------------------------------------------

graph = builder.compile(
    checkpointer=memory
)