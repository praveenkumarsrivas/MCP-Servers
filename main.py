import asyncio
from email import message
from imaplib import Commands
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
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


from pprint import pprint
from langchain_core.messages import AIMessage
async def main():
    async with stdio_client(stdio_server_params) as (read, write):
        async with ClientSession(read_stream=read, write_stream=write) as session:
            await session.initialize()
            print("session initialized")

            tools = await load_mcp_tools(session)
            print("Loaded tools:", [t.name for t in tools])
            agent = create_react_agent(llm, tools)
            result = await agent.ainvoke({"messages": [HumanMessage(content="What is 52+2*3?")]})
            for message in result['messages']:
                if isinstance(message, AIMessage) and message.content:
                    print("OUTPUT:", message.content)


    

if __name__ == "__main__":
    asyncio.run(main())
