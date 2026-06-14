import pymysql

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="web"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM users")
data = cursor.fetchall()

for row in data:
    print(row)

conn.close()