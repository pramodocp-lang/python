import sqlite3 as sql

connection = sql.connect("company.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary REAL
)
""")

connection.commit()
connection.close()

print("Table created successfully!")