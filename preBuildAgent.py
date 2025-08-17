import os
from dotenv import load_dotenv
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import InMemorySaver

load_dotenv()

agent = create_react_agent(
    model="groq:llama-3.3-70b-versatile",  
    tools=[],  
    prompt="You are a helpful assistant"  
)

#for memory check 
checkpointer = InMemorySaver()

#graph creation
#try:
 #  img = agent.get_graph().draw_mermaid_png()
  # with open("agent_graph.png", "wb") as f:
   #    f.write(img)
#except Exception:
#   pass

config = {"configurable": {"thread_id": "1"}}
# Run the agent
response1 = agent.invoke(
    {"messages": [{"role": "user", "content": "who is modi?"}]}, config
)

ai_message1 = response1["messages"][-1].content
print(ai_message1)

# Run the agent with memory
response = agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in Hyderabad?"}]}
)

#ai_message = response["messages"][-1].content
#print(ai_message)

#print(respose)  # Output the response from the agent
