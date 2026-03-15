
import os
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Demo")

@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    result = a + b
    return ' Sur la base du serveur MCP de Styve, la somme  de {a} et {b} est {result}'.format(a=a, b=b, result=result)
