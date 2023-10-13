import sqlite3

conn = sqlite3.connect('tutorial1.db')
cur = conn.cursor()
cur.execute('SELECT*FROM Users')
rows = cur.fetchall()
for row in rows:
	print(row)

cur.close()