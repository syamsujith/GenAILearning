from dotenv import load_dotenv
load_dotenv()
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.prebuilt import create_react_agent
from langchain_tavily import TavilySearch


import streamlit as st


st.title("Educosys Chatbot App")


if "messages" not in st.session_state:
   st.session_state.messages = []

# Initialize Tavily Search Tool
tavily_search_tool = TavilySearch(
    max_results=5,
    topic="general",
)


checkpointer = InMemorySaver()


agent = create_react_agent(
   model="openai:gpt-4o", 
   tools=[tavily_search_tool], 
   checkpointer=checkpointer,
   prompt="You are a helpful assistant" 
)


def stream_graph_updates(user_input : str):
   assistant_response = ""


   with st.chat_message("assistant"):
       message_placeholder = st.empty()
       for event in agent.stream({"messages": [{"role": "user", "content": user_input}]}, {"configurable": {"thread_id": "def"}}):
           for value in event.values():
               new_text = value["messages"][-1].content
               assistant_response += new_text
               message_placeholder.markdown(assistant_response)


   st.session_state.messages.append(("assistant", assistant_response))


# Display previous chat history
for role, message in st.session_state.messages:
   with st.chat_message(role):
       st.markdown(message)

