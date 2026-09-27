import pandas as pd
import sqlite3

df = pd.read_csv('data/raw/amex.csv')

df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y').dt.strftime('%Y-%m-%d')

small_df = df[['Date', 'Description', 'Amount', 'Category']]

conn = sqlite3.connect('data/budget_guardian.db')

list_of_tuples = [
    (1, row['Date'], row['Amount'], row['Category'], row['Description'])
    for _, row in small_df.iterrows()
]

count = conn.execute("SELECT COUNT(*) FROM transactions").fetchone()[0]
if count == 0:
    conn.executemany(
        "INSERT INTO transactions (user_id, date, amount, category, merchant) VALUES (?, ?, ?, ?, ?)",
        list_of_tuples
    )
    conn.commit()


print(conn.execute("SELECT COUNT(*) FROM transactions").fetchone())
print(conn.execute("SELECT * FROM transactions LIMIT 3").fetchone())