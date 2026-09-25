"""
Chunk 3: Tool registry.

Each function below becomes an LLM-callable tool via LangChain's @tool
decorator. The decorator turns the docstring into the tool's description
(the LLM reads this to decide when to call it) — so write docstrings like
you're explaining the tool to the agent, not to a teammate.

Pattern for each:
    from langchain_core.tools import tool

    @tool
    def get_user_profile(user_id: int) -> dict:
        \"\"\"Fetch a user's id, name, monthly income and currency.\"\"\"
        # TODO: open sqlite3 connection, SELECT * FROM users WHERE id=?,
        # return as dict, close connection.
        raise NotImplementedError

Fill in the same pattern for the remaining six. Signatures/sources, per
the spec table:

    get_transactions(user_id: int, days: int = 30) -> list[dict]
        source: transactions table, filter by date >= today - days

    search_notes(user_id: int, query: str) -> list[dict]
        source: transactions.note, simple substring or LIKE match

    get_category_spend(user_id: int, category: str, days: int) -> dict
        source: transactions, SUM(amount) grouped, return {total, avg, count}

    list_recent_merchants(user_id: int, limit: int = 10) -> list[dict]
        source: transactions, GROUP BY merchant ORDER BY total spend DESC

    lookup_category_rule(category: str) -> dict
        source: data/category_rules.json — load once at module import,
        not on every call (it's static reference data)

    get_budget_template(template_name: str) -> list[dict]
        source: data/budget_templates.csv via pandas.read_csv, filter rows

Once all seven are decorated with @tool, export them as a list:

    ALL_TOOLS = [get_user_profile, get_transactions, ...]

agent.py binds this list to the LLM with llm.bind_tools(ALL_TOOLS).
"""

import json

import pandas as pd

from config import CATEGORY_RULES_PATH, BUDGET_TEMPLATES_PATH, DB_PATH

# TODO: load static reference files once here, not inside each tool call
# _category_rules = json.load(open(CATEGORY_RULES_PATH))
# _budget_templates = pd.read_csv(BUDGET_TEMPLATES_PATH)

# TODO: define the 7 @tool-decorated functions described above

ALL_TOOLS: list = []  # TODO: populate once functions are defined
