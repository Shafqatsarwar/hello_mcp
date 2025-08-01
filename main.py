from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name = "hello-mcp", stateless_http = True)

@mcp.tool()
def search_online(query: str) -> str:
    # TODO: Simulate an online search operation
    return f"Search results for '{query}'"

@mcp.tool()
async def get_weather(city: str) -> str:
    # TODO: Simulate an online search operation
    return f"Search weather for '{city}'"
# @mcp.tool()
# def hello(name: str) -> str:
#     return f"Hello, {name}!"

mcp_app = mcp.streamable_http_app()
