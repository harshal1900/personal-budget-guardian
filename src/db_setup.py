import sqlite3

conn = sqlite3.connect('data/budget_guardian.db')
conn.execute("""
CREATE TABLE IF NOT EXISTS transactions (
 id INTEGER PRIMARY KEY,
 user_id INTEGER,
 date TEXT,
 amount REAL,
 category TEXT,
 merchant TEXT
)
""")
conn.commit()


conn.execute("""
CREATE TABLE IF NOT EXISTS users (
 id INTEGER PRIMARY KEY,
 name TEXT,
 monthly_income REAL,
 currency TEXT
)
""")
conn.commit()

conn.execute("""
CREATE TABLE IF NOT EXISTS goals (
 id INTEGER PRIMARY KEY,
 user_id INTEGER,
 name TEXT,
 target_amount REAL,
 deadline TEXT
)
""")
conn.commit()

count = conn.execute("SELECT COUNT(*) FROM users").fetchone()[0]
if count == 0:
    conn.execute(
        "INSERT INTO users (name, monthly_income, currency) VALUES (?, ?, ?)",
        ("Navin", 9854.42, "USD")
    )
    conn.commit()

for row in conn.execute("SELECT * FROM users"):
    print(row)
conn.close()