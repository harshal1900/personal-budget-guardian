"""
Chunk 4: Agent graph.

Concepts before code:
- AgentState is just a TypedDict that gets passed between nodes and
  updated at each step. It's the "memory" of one conversation turn.
- The Agent Node calls the LLM (with tools bound) and gets back either
  a tool_call or a final text answer.
- The Tool Execution Node actually runs whichever tool the LLM asked for,
  and appends the result as a ToolMessage.
- The Conditional Edge decides: if the last AI message has tool_calls,
  loop back to the Tool Node; otherwise, END.
- This loop (Agent -> Tool -> Agent -> Tool -> ... -> END) IS the ReAct
  pattern. LangGraph just gives you a formal way to draw and run it.

TODO:
1. Define AgentState(TypedDict) with at least:
     messages: Annotated[list[BaseMessage], add_messages]
     user_id: int
2. Write SYSTEM_PROMPT as a string — this is where your negative
   constraints live (no writes, no investment advice, escalate on
   tax/legal/investment questions or after 2 failed tool calls).
3. agent_node(state) -> dict: call llm_with_tools.invoke(messages), return
   {"messages": [response]}
4. tool_node: LangGraph ships a prebuilt ToolNode(ALL_TOOLS) — use it
   instead of writing your own dispatcher.
5. should_continue(state) -> str: check state["messages"][-1].tool_calls;
   return "tools" or END.
6. Build the graph:
     graph = StateGraph(AgentState)
     graph.add_node("agent", agent_node)
     graph.add_node("tools", tool_node)
     graph.set_entry_point("agent")
     graph.add_conditional_edges("agent", should_continue, {"tools": "tools", END: END})
     graph.add_edge("tools", "agent")
     app = graph.compile()
7. Save the diagram: app.get_graph().draw_mermaid_png() or draw_mermaid()
   -> paste into docs/architecture.md
8. In main(), loop over the 5 test cases from tests/test_cases.py, invoke
   the graph, and print BOTH the final answer and the full message trace
   (every tool call + observation) — the rubric explicitly asks you to
   print the trace, not just the answer.
"""

from config import DB_PATH  # noqa: F401
from tools import ALL_TOOLS  # noqa: F401

SYSTEM_PROMPT = """TODO: write the full system prompt here.
Cover: persona, scope (read-only, this user's data + reference rules only),
tool-selection order (profile first), negative constraints (no writes, no
investment/tax/legal advice, never invent numbers), and the exact
escalation trigger + message."""


def main() -> None:
    # TODO: import test_cases, run each through the compiled graph, print trace + answer
    raise NotImplementedError


if __name__ == "__main__":
    main()
