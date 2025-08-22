from mcp.server.fastmcp import FastMCP
import os

mcp = FastMCP("mcpServerCreation")

@mcp.tool()
def add_file(file_name: str):
    """Create a new file in the current directory."""
    if not os.path.exists(file_name):
        with open(file_name, 'w') as f:
            pass
        print(f"File '{file_name}' created.")
    else:
        print(f"File '{file_name}' already exists.")

@mcp.tool()
def add_directory(directory_name: str):
    """Create a new directory in the current directory."""
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
        print(f"Directory '{directory_name}' created.")
    else:
        print(f"Directory '{directory_name}' already exists.")

@mcp.tool()
def delete_file(file_name: str):
    """Delete a file in the current directory."""
    if os.path.exists(file_name):
        os.remove(file_name)
        print(f"File '{file_name}' deleted.")
    else:
        print(f"File '{file_name}' does not exist.")

@mcp.tool()
def delete_directory(directory_name: str):
    """Delete a directory in the current directory."""
    if os.path.exists(directory_name):
        os.rmdir(directory_name)
        print(f"Directory '{directory_name}' deleted.")
    else:
        print(f"Directory '{directory_name}' does not exist.")


if __name__ == "__main__":
    mcp.run(transport="stdio")
    print("MCP Server is running...")