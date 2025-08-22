import os
from dotenv import load_dotenv
import streamlit as st
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import InMemorySaver

# Load environment variables
load_dotenv()

# Initialize agent
agent = create_react_agent(
    model="groq:llama-3.3-70b-versatile",
    tools=[],
    prompt="You are a helpful assistant"
)

# Memory checkpointer
checkpointer = InMemorySaver()

# Streamlit Page Config
st.set_page_config(page_title="AI Chatbot", page_icon="🤖", layout="centered")

# Title
st.title("AI Chatbot")
#st.caption("Powered by Groq LLaMA-3.3-70B + LangGraph")

# Initialize session state for messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask me anything..."):
    # Store user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Invoke the agent
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = agent.invoke(
                    {"messages": [{"role": "user", "content": prompt}]},
                    config={"configurable": {"thread_id": "1"}}
                )
                ai_message = response["messages"][-1].content
            except Exception as e:
                ai_message = f"⚠️ Error: {e}"

        st.markdown(ai_message)
        st.session_state.messages.append({"role": "assistant", "content": ai_message})
