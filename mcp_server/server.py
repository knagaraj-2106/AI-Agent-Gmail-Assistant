"""
server.py

MCP Server for the AI Gmail Assistant.

This server exposes Gmail capabilities to any MCP-compatible client.
"""

from mcp.server.fastmcp import FastMCP

# -------------------------------------------------------
# Create MCP Server
# -------------------------------------------------------

mcp = FastMCP(
    name="AI Gmail Assistant"
)