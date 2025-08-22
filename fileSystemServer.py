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
           "github": {
               "command": "npx",
               "args": [
                   "-y",
                   "@modelcontextprotocol/server-github"
               ],
               "env": {
                   "GITHUB_PERSONAL_ACCESS_TOKEN": GITHUB_TOKEN
               },
               "transport": "stdio"
           },
           "filesystem": {
               "command": "npx",
               "args": [
                   "-y",
                   "@modelcontextprotocol/server-filesystem",
                   "C:\\work\\LearnAI\\AIBootcamp"
               ],
               "transport":"stdio"
           }
       }
   )
   tools = await client.get_tools()
  # print("Tools:", tools)
   agent = create_react_agent("groq:llama-3.3-70b-versatile", tools)
   response = await agent.ainvoke({"messages": "what are the files present in AIBootcamp Directory"})
   print(response)
   #print(response["messages"][-1].content)

if __name__ == "__main__":
        asyncio.run(run_agent())