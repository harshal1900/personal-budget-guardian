import json

def get_user_profile(conn, user_id):
    """
    Fetches the user profile from the database based on the provided user_id.

    Parameters:
    conn (sqlite3.Connection): The SQLite database connection object.
    user_id (int): The ID of the user whose profile is to be fetched.

    Returns:
    dict: A dictionary containing the user's profile information, or None if the user does not exist.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    row = cursor.fetchone()
    
    if row:
        return {
            "id": row[0],
            "name": row[1],
            "monthly_income": row[2],
            "currency": row[3]
        }
    else:
        return None

def get_recent_transactions(conn, user_id, limit=10):
    """
    Fetches the most recent transactions for a given user from the database.

    Parameters:
    conn (sqlite3.Connection): The SQLite database connection object.
    user_id (int): The ID of the user whose transactions are to be fetched.
    limit (int): The maximum number of recent transactions to fetch. Default is 10.

    Returns:
    list: A list of dictionaries, each containing transaction details.
    """
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM transactions WHERE user_id = ? ORDER BY date DESC LIMIT ?",
        (user_id, limit)
    )
    
    transactions = []
    for row in cursor.fetchall():
        transactions.append({
            "id": row[0],
            "user_id": row[1],
            "date": row[2],
            "amount": row[3],
            "category": row[4],
            "merchant": row[5]
        })
    
    return transactions

def search_transactions_by_merchant(conn, user_id, search_term):
    """
    Searches for transactions by merchant name for a given user.

    Parameters:
    conn (sqlite3.Connection): The SQLite database connection object.
    user_id (int): The ID of the user whose transactions are to be searched.
    search_term (str): The term to search for in the merchant names.

    Returns:
    list: A list of dictionaries, each containing transaction details that match the search term.
    """
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM transactions WHERE user_id = ? AND merchant LIKE ?",
        (user_id, f"%{search_term}%")
    )
    
    transactions = []
    for row in cursor.fetchall():
        transactions.append({
            "id": row[0],
            "user_id": row[1],
            "date": row[2],
            "amount": row[3],
            "category": row[4],
            "merchant": row[5]
        })
    
    return transactions

def total_spend_by_category(conn, user_id):
    """
    Calculates the total spend by category for a given user.

    Parameters:
    conn (sqlite3.Connection): The SQLite database connection object.
    user_id (int): The ID of the user whose spend is to be calculated.

    Returns:
    dict: A dictionary where keys are categories and values are the total spend in that category.
    """
    cursor = conn.cursor()
    cursor.execute(
        "SELECT category, SUM(amount) FROM transactions WHERE user_id = ? AND amount > 0 GROUP BY category",
        (user_id,)
    )
    
    spend_by_category = {}
    for row in cursor.fetchall():
        spend_by_category[row[0]] = row[1]
    
    return spend_by_category

def list_top_merchants(conn, user_id, limit=5):
    """
    Lists the top merchants by total spend for a given user.

    Parameters:
    conn (sqlite3.Connection): The SQLite database connection object.
    user_id (int): The ID of the user whose top merchants are to be listed.
    limit (int): The maximum number of top merchants to return. Default is 5.

    Returns:
    list: A list of dictionaries, each containing merchant name and total spend.
    """
    cursor = conn.cursor()
    cursor.execute(
        "SELECT merchant, SUM(amount) as total_spend FROM transactions WHERE user_id = ? AND amount > 0 GROUP BY merchant ORDER BY total_spend DESC LIMIT ?",
        (user_id, limit)
    )
    
    top_merchants = []
    for row in cursor.fetchall():
        top_merchants.append({
            "merchant": row[0],
            "total_spend": row[1]
        })
    
    return top_merchants

def get_category_cap(conn, category):
    """Looks up the spending cap for a category from the caps reference file (not the DB)."""
    # not SQL — this reads from a small dict/JSON we haven't created yet, covered next
    with open('data/category_caps.json', 'r') as f:
        category_caps = json.load(f)
    return category_caps.get(category, 0)

def get_budget_template(conn, template_name):
    """Looks up a budget allocation template (e.g. 50/30/20) from a reference file (not the DB)."""
    # same as above — reference file, not SQL
    with open('data/budget_templates.json', 'r') as f:
        budget_templates = json.load(f)
    return budget_templates.get(template_name, {})