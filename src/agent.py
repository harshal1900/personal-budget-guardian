import os
import sqlite3

from dotenv import load_dotenv
from typing import TypedDict, Annotated
from langchain_openai import ChatOpenAI
from langgraph.graph.message import add_messages
from agent_tools import build_agent_tools
from langchain_core.messages import SystemMessage, HumanMessage
from langgraph.prebuilt import ToolNode
from langgraph.graph import StateGraph, END


load_dotenv()

class AgentState(TypedDict):
    messages: Annotated[list, add_messages]

llm = ChatOpenAI(
    model="openrouter/free",
    openai_api_key=os.environ.get("OPENROUTER_API_KEY", ""),
    openai_api_base="https://openrouter.ai/api/v1",
)

conn = sqlite3.connect("data/budget_guardian.db", check_same_thread=False)
tools = build_agent_tools(conn)
tool_node = ToolNode(tools)
llm_with_tools = llm.bind_tools(tools)

def agent_node(state: AgentState):
    response = llm_with_tools.invoke(state["messages"])
    return {"messages": [response]}

def should_continue(state: AgentState):
    last_message = state["messages"][-1]
    if last_message.tool_calls:
        return "tools"
    return "end"


graph = StateGraph(AgentState)
graph.add_node("agent", agent_node)
graph.add_node("tools", tool_node)
graph.set_entry_point("agent")
graph.add_conditional_edges("agent", should_continue, {"tools": "tools", "end": END})
graph.add_edge("tools", "agent")

app = graph.compile()

if __name__ == "__main__":
    initial_state = {
        "messages": [
            SystemMessage(content="" \
            "You are a read-only budget assistant for user_id=1"
            "Always use user_id=1 when calling tools that require it"
            "You may report spending data, category caps, and budget templates."
            "You must NOT give investment, tax or legal advice and must NOT tell the user "
            "what to do with their money beyond reporting facts from the tools."
            "If asked for advice outside this scope, respond only with: "
            "'That's outside what I can help with — please talk to a human financial advisor.'"
            ),
            HumanMessage(content="Should I invest my savings in stocks or crypto?")
        ]
    }
    result = app.invoke(initial_state)
    print(result["messages"][-1].content)