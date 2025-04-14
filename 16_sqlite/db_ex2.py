import sqlite3
con = sqlite3.connect("2.db")
cur = con.cursor()

sql_req = """SELECT books.title, 
	group_concat(authors.name, '; ') AS authrs,
	publishers.name, books.year, genres.name, 
	COUNT(*) as num_authors
FROM books 
JOIN ABlinks ON books.id = ABlinks.book_id
JOIN authors ON ABlinks.author_id = authors.id
JOIN genres ON books.genre_id = genres.id
JOIN publishers ON books.publisher_id=publishers.id
GROUP BY books.id;
"""
res = cur.execute(sql_req)
cur.row_factory = sqlite3.Row
for item in res.fetchall():
    print(item['title'], '--', item['authrs'])