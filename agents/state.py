"""
state.py

Defines the shared state for the LangGraph workflow.
"""

from typing import Annotated, TypedDict

from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage


class AgentState(TypedDict):
    """
    Shared state passed between LangGraph nodes.
    """

    messages: Annotated[list[BaseMessage], add_messages]