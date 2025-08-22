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
           }
       }
   )
   tools = await client.get_tools()
   agent = create_react_agent("groq:llama-3.3-70b-versatile", tools)
   #response = await agent.ainvoke({"messages": "what are the files present in repository /syamsujith/syam-sujith-digital-garden"})
   response = await agent.ainvoke({"messages": "generate code for binary search and push to test.txt file of main branch of respository /syamsujith/githubMcpConnection "})
  # response = await agent.ainvoke({"messages": "push the current C:/work/LearnAI/AIBootcamp/code/GitHubAgent1.py file including content inside the file ready write permission to main branch of respository /syamsujith/githubMcpConnection "})
   print(response["messages"][-1].content)


if __name__ == "__main__":
   asyncio.run(run_agent())
