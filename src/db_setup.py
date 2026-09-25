"""
Chunk 1: Data layer.

TODO:
1. Connect to sqlite3 at DB_PATH (config.DB_PATH), creating the file if absent.
2. CREATE TABLE IF NOT EXISTS for: users, transactions, goals
   — use the exact column list from the project spec:
   users(id INTEGER PK, name TEXT, monthly_income REAL, currency TEXT)
   transactions(id INTEGER PK, user_id INTEGER FK, date TEXT, amount REAL,
                category TEXT, merchant TEXT, note TEXT)
   goals(id INTEGER PK, user_id INTEGER FK, name TEXT, target_amount REAL,
         deadline TEXT)
3. Seed one sample user (e.g. "Alex Rivera", income 4200) and ~15-20 sample
   transactions across a few categories/dates so get_category_spend has
   something real to sum. Seed one goal too.
4. Commit + close the connection.
5. Guard against re-seeding on every run (check `if cursor.fetchone() is None`
   before inserting, or wrap in a --reset CLI flag).

Run this once before agent.py. It should be idempotent.
"""

import sqlite3

from config import DB_PATH


def create_schema(conn: sqlite3.Connection) -> None:
    """TODO: run the three CREATE TABLE IF NOT EXISTS statements."""
    raise NotImplementedError


def seed_sample_data(conn: sqlite3.Connection) -> None:
    """TODO: insert one user, several transactions, one goal — only if empty."""
    raise NotImplementedError


def main() -> None:
    conn = sqlite3.connect(DB_PATH)
    create_schema(conn)
    seed_sample_data(conn)
    conn.commit()
    conn.close()
    print(f"Database ready at {DB_PATH}")


if __name__ == "__main__":
    main()
