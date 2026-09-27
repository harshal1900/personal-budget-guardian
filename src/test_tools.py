import sqlite3
from tools import (
    get_user_profile, 
    get_recent_transactions, 
    search_transactions_by_merchant,
    total_spend_by_category, 
    list_top_merchants,
    get_category_cap, 
    get_budget_template
)

conn = sqlite3.connect('data/budget_guardian.db')

print(get_user_profile(conn, 1))
print(get_recent_transactions(conn, 1, limit=3))
print(search_transactions_by_merchant(conn, 1, "SAM"))
print(total_spend_by_category(conn, 1))
print(list_top_merchants(conn, 1, limit=3))
print(get_category_cap(conn, "Merchandise & Supplies-Groceries"))
print(get_budget_template(conn, "50-30-20"))

conn.close()