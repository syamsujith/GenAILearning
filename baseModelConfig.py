from dotenv import load_dotenv
from pydantic import BaseModel
import os
from langgraph.prebuilt import create_react_agent

load_dotenv()

class MailResponse(BaseModel):
   subject: str
   body: str

class createSampleInterviewQuestion(BaseModel):
   Question: str
   answer: str

agent = create_react_agent(
    model="groq:llama-3.3-70b-versatile",  
    tools=[],  
    response_format= MailResponse
)

agent = create_react_agent(
    model="groq:llama-3.3-70b-versatile",  
    tools=[],  
    response_format= createSampleInterviewQuestion
)

config = {"configurable": {"thread_id": "1"}}

#response = agent.invoke(
  #  {"messages": [{"role": "user", "content": "write a mail to client to regarding requirement change"}]}, config
#)

response = agent.invoke(
    {"messages": [{"role": "user", "content": "CREATE JAVA Interview Questions and Answers for 10+ years of experience"}]}, config
)


print(response["messages"][-1].content)

print("--------------------------------------------------------------------------------------------------------")

print(response["structured_response"])

print("----------------------------------------------------------------------------------------------------------")
print(response["structured_response"].Question)


print("------------------------------------------------------------------------------------------------------")
print(response["structured_response"].answer)