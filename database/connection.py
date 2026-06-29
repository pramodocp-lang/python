import sqlite3 as sql

connection = sql.connect("company.db")

print("Database connected successfully!")

connection.close()