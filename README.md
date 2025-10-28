# 🧠 FastMCP Remote Server (Demo Local Server)

This project is a **Minimal MCP (Model Context Protocol) Remote Server** built with the **FastMCP** framework.  
It demonstrates how to expose simple Python tools (functions) as MCP endpoints that can be accessed remotely — for use with AI models, MCP inspectors, or connected clients like Claude or ChatGPT with MCP support.

---

## 🚀 Features

- ⚡ **FastMCP Framework:** Lightweight, async server built with [FastMCP](https://gofastmcp.com)
- 🧮 **Example Tools:** 
  - `roll_dice(n_dice)` → rolls multiple six-sided dice  
  - `add_number(a, b)` → adds two numbers
- 🌐 **HTTP Transport:** Runs on a simple HTTP server (`localhost:8000/mcp`)
- 🔒 **MCP Compatible:** Can connect with the MCP Inspector or proxy tools
