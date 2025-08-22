from dotenv import load_dotenv
load_dotenv()
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
import os


GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")


async def run_agent():
   client = MultiServerMCPClient(
       {
    "McpFileSystem": {
               "command": "python",
               "args": [
                   "./mcpServerCreation.py"
               ],
               "transport":"stdio"
           }
       }
   )
   tools = await client.get_tools()
  # print("Tools:", tools)
   agent = create_react_agent("groq:llama-3.3-70b-versatile", tools)
   response = await agent.ainvoke({"messages": "delete NewMCPServer1 file"})
   print(response)
   #print(response["messages"][-1].content)

if __name__ == "__main__":
        asyncio.run(run_agent())