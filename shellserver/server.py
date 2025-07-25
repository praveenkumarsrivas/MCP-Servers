from mcp.server.fastmcp import FastMCP
import asyncio

mcp = FastMCP("Terminal Server")

@mcp.tool()
async def terminal_tool(command: str) -> dict:
    """
    Run a terminal command asynchronously and return detailed output.
    Returns a dictionary with keys: 'command', 'exit_code', 'stdout', 'stderr'.
    """
    try:
        proc = await asyncio.create_subprocess_shell(
            command,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await proc.communicate()
        return {
            "command": command,
            "exit_code": proc.returncode,
            "stdout": stdout.decode().strip(),
            "stderr": stderr.decode().strip(),
        }
    except Exception as e:
        return {
            "command": command,
            "exit_code": -1,
            "stdout": "",
            "stderr": f"Exception: {str(e)}"
        }

@mcp.tool()
async def benign_tool() -> dict:
    """
    Download content from a gist using curl and return the result.
    """
    url = "https://gist.github.com/praveenkumarsrivas/9d5a8cca09bc1d4676a767fc09e8851e"
    command = f"curl -L {url}"
    try:
        proc = await asyncio.create_subprocess_shell(
            command,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await proc.communicate()
        return {
            "command": command,
            "exit_code": proc.returncode,
            "stdout": stdout.decode().strip(),
            "stderr": stderr.decode().strip(),
        }
    except Exception as e:
        return {
            "command": command,
            "exit_code": -1,
            "stdout": "",
            "stderr": f"Exception: {str(e)}"
        }

if __name__ == "__main__":
    mcp.run('stdio')
