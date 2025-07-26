import asyncio
from dotenv import load_dotenv

import os

load_dotenv()
print(os.getenv("OPENAI_API_KEY"))

async def main():
    print("Hello from mcp-servers!")
    

if __name__ == "__main__":
    asyncio.run(main())
