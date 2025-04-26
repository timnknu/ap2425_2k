import sqlite3
con = sqlite3.connect("2.db")
cur = con.cursor()
res = cur.execute("SELECT * FROM authors")
for item in res.fetchall():
    print(item)