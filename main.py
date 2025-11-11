import random 
from fastmcp import FastMCP
import json
## create a FastMCP instance
mcp = FastMCP(name = "Dice and Adder Bot")

## decorator
@mcp.tool
def roll_dice(n_dice:int = 1)->list[int]:
    """Roll n 6-sided dice and return the results as a list of integers."""
    return [random.randint(1, 6) for _ in range(n_dice)]

@mcp.tool
def add_numbers(a:float, b:float)->float:
    """Return the sum of two numbers."""
    return a + b

# resource server information
@mcp.resource("info://server")
def server_info()->str:
    """Return information about the server."""
    info={
        "name":"    Dice and Adder Bot Server",
        "version":"1.0.0",
        "description":"A server that hosts the Dice and Adder Bot using FastMCP.",
        "tool":["roll_dice","add_numbers"],
        "author":"Sushil verma",
    }
    return json.dumps(info ,indent = 2)
if __name__ == "__main__":
    mcp.run(transport = "http", host="0.0.0.0",port=8000)