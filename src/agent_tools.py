from tools import (
    get_recent_transactions, 
    get_user_profile,
    search_transactions_by_merchant,
    total_spend_by_category,
    list_top_merchants,
    get_category_cap,
    get_budget_template
)
from langchain_core.tools import tool

def make_get_user_profile_tool(conn):
    @tool
    def get_user_profile_tool(user_id: int) -> dict:
        """Get user profile information (name, monthly income, currency) by user ID."""
        return get_user_profile(conn, user_id)
    return get_user_profile_tool

def make_get_recent_transactions_tool(conn):
    @tool
    def get_recent_transactions_tool(user_id: int, limit: int = 10) -> list:
        """Get a user's most recent transactions, newest first."""
        return get_recent_transactions(conn, user_id, limit)
    return get_recent_transactions_tool

def make_search_transactions_by_merchant_tool(conn):
    @tool
    def search_transactions_by_merchant_tool(user_id: int, merchant_name: str) -> list:
        """Search a user's transactions by merchant name (partial match)."""
        return search_transactions_by_merchant(conn, user_id, merchant_name)
    return search_transactions_by_merchant_tool

def make_total_spend_by_category_tool(conn):
    @tool
    def total_spend_by_category_tool(user_id: int) -> dict:
        """Get a user's total spend broken down by category."""
        return total_spend_by_category(conn, user_id)
    return total_spend_by_category_tool

def make_list_top_merchants_tool(conn):
    @tool
    def list_top_merchants_tool(user_id: int, limit: int = 5) -> list:
        """List a user's top merchants by total amount spent."""
        return list_top_merchants(conn, user_id, limit)
    return list_top_merchants_tool

def make_get_category_cap_tool(conn):
    @tool
    def get_category_cap_tool(category: str) -> float:
        """Look up the spending cap set for a given category."""
        return get_category_cap(conn, category)
    return get_category_cap_tool

def make_get_budget_template_tool(conn):
    @tool
    def get_budget_template_tool(template_name: str) -> dict:
        """Look up a named budget allocation template (e.g. '50-30-20')."""
        return get_budget_template(conn, template_name)
    return get_budget_template_tool


def build_agent_tools(conn):
    """Build a list of agent tools for financial data access."""
    return [
        make_get_user_profile_tool(conn),
        make_get_recent_transactions_tool(conn),
        make_search_transactions_by_merchant_tool(conn),
        make_total_spend_by_category_tool(conn),
        make_list_top_merchants_tool(conn),
        make_get_category_cap_tool(conn),
        make_get_budget_template_tool(conn)
    ]


## real check to test tools call
if __name__ == "__main__":
    import sqlite3
    conn = sqlite3.connect("data/budget_guardian.db")
    tools = build_agent_tools(conn)
    print(len(tools))
    for t in tools:
        print(t.name)