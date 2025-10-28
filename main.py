import random
import datetime
from fastmcp import FastMCP

mcp = FastMCP("Demo Remote MCP Server")

@mcp.tool
async def reverse_text(text: str) -> str:
    """Reverse the given text string."""
    return text[::-1]

@mcp.tool
async def current_datetime() -> str:
    """Return the current date and time as a string."""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@mcp.tool
async def random_number(start: int = 0, end: int = 100) -> int:
    """Generate a random number between start and end (inclusive)."""
    return random.randint(start, end)

@mcp.tool
async def word_count(text: str) -> int:
    """Return the number of words in the given text."""
    return len(text.split())

@mcp.tool
async def even_or_odd(number: int) -> str:
    """Check if a number is even or odd."""
    return "Even" if number % 2 == 0 else "Odd"

@mcp.tool
async def generate_password(length: int = 8) -> str:
    """Generate a random password of a given length."""
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    return "".join(random.choice(chars) for _ in range(length))

@mcp.tool
async def random_quote() -> str:
    """Return a random motivational quote."""
    quotes = [
        "Believe you can and you're halfway there.",
        "Do something today that your future self will thank you for.",
        "It always seems impossible until it's done.",
        "Dream big, work hard, stay humble.",
        "Success is not final; failure is not fatal: It is the courage to continue that counts."
    ]
    return random.choice(quotes)

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)
