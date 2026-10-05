from mcp.server import MCPServer

mcp = MCPServer("OpenCart Selenium Server")


@mcp.tool()
def hello() -> str:
    """Test whether the OpenCart MCP server is working."""
    return "OpenCart MCP Server is working!"


if __name__ == "__main__":
    mcp.run()