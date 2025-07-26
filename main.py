import asyncio
from imaplib import Commands
from dotenv import load_dotenv
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

import os
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)


stdio_server_params = StdioServerParameters(
    command = 'python',
    args = ['/Users/praveensrivas/Documents/MCP/MCP-Servers/servers/math_server.py'],
)


async def main():
    print("Hello from mcp-servers!")
    

if __name__ == "__main__":
    asyncio.run(main())
