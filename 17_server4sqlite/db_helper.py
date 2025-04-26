import sqlite3
# Функції для роботи з базою даних SQLite (в цьому прикладі -- пошук книг за назвою або роком видання)

# Стврюємо SQL-запит до бази даних для пошуку книг за назвою
sql_books_by_title = """SELECT 
books.title as btitle, group_concat(authors.name, '; ') as authorlist, publishers.name as nmape, books.year as byear, genres.name as gname
FROM books 
JOIN ABlinks ON books.id=ABlinks.book_id 
JOIN authors ON ABlinks.author_id=authors.id 
JOIN publishers ON publishers.id=books.publisher_id 
JOIN genres ON genres.id=books.genre_id 
WHERE books.title LIKE ? GROUP BY books.id"""
# Важливо: Параметр ? буде замінено на значення, яке передамо як аргумент в метод execute()
# Це запобігає так званим SQL-ін'єкціям -- коли зловмисник може вставити свій SQL-код в текстовий рядок
# (як у нашому випадку частина назви книги для пошуку), про який точно відомо, що він буде використаний у запиті,
# і завдяки цьому -- перемістити його в SQL-запит. Наприклад, якщо ввести в поле пошуку назву книги
# "123%'; DROP TABLE books; SELECT * FROM books WHERE title LIKE '", то в SQL-запиті буде виконано команду DROP TABLE books
# а це би означало, що вся таблиця books буде видалена! Тому ми використовуємо параметри запиту (знаки '?'), які замінюються
# на значення лише в самому методі execute() і таким чином не можуть бути частиною SQL-запиту.

# Стврюємо SQL-запит до бази даних для пошуку книг за роком видання
sql_books_by_year = """SELECT 
books.title as btitle, group_concat(authors.name, '; ') as authorlist, publishers.name as nmape, books.year as byear, genres.name as gname
FROM books 
JOIN ABlinks ON books.id=ABlinks.book_id 
JOIN authors ON ABlinks.author_id=authors.id 
JOIN publishers ON publishers.id=books.publisher_id 
JOIN genres ON genres.id=books.genre_id 
WHERE books.year=? GROUP BY books.id"""

# Функція для пошуку книг у базі даних (за заданим SQL-запитом)
def find_book(sql_req, search_param):
    # Підключення до бази даних SQLite
    db = sqlite3.connect('../16_sqlite/2.db')
    # Створюємо "курсор" для виконання запитів
    cursor = db.cursor()
    cursor.row_factory = sqlite3.Row # щоб отримувати результати із метода .fetchall() у вигляді словників
    # Виконуємо запит до бази даних:
    cursor.execute(sql_req, (search_param,))

    found_books_html = ''
    res_count = 0
    # Отримуємо результати запиту у вигляді списку словників (кожен рядок -- це словник, в якому ключі -- це назви колонок):
    for row in cursor.fetchall():
        # Формуємо HTML-код для відображення результатів пошуку:
        item_html = f"""<li> <i> {row['authorlist']} </i>.  
        <b>{row['btitle']} </b> //
        {row['nmape']}, {row['byear']}
        <font color="green"></i>{row['gname']}</i></font>,  
        </li>"""
        # print(item_html)
        found_books_html += item_html
        res_count += 1
    # Закриваємо з'єднання з базою даних:
    db.close()

    return found_books_html, res_count
#

if __name__ == "__main__":
    # Тестуємо функцію find_book()
    r = find_book(sql_books_by_title, '%а%')
    print(r)
