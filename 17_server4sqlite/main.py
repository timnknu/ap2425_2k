import server_cls # модуль, який реалізує сервер
import user_sessions # модуль, який реалізує сесії користувачів
import db_helper # модуль, який реалізує функції для роботи з базою даних SQLite

# Основна частина програми, яка реалізує логіку обробки запитів упродовж "сеансу" взаємодії з користувачем
# (реалізована у класі BookFinder, який успадковує клас BaseHandler з модуля user_sessions)
class BookFinder(user_sessions.BaseHandler):
    def main(self):
        print(f'Debug: session for {self.uid} started')
        self.nsteps = 0
        while True:
            # Початок "сеансу" користувача: Показуємо вітальну сторінку з формою для введення назви книги:
            environ, form_data = self.remote_input(self.fmt_html_page('welcome.html'))
            print('>>1') # Відлагоджувальне повідомлення, яке дозволяє відслідковувати хід виконання програми

            # Перевіряємо, який тип пошуку вибрав користувач -- за назвою чи за роком видання
            search_type = form_data.get('search_type', ['title'])[0] # отримуємо значення поля "search_type" з форми
            if search_type == 'title':
                # Показуємо форму для введення (частини)назви книги
                environ, form_data = self.remote_input(self.fmt_html_page('find_by_title.html'))
                print('>>2/title', form_data)

                # Обробляємо отримані дані (які були введені користувачем у формі сторінці 'welcome.html')
                title = form_data.get('title', [''])[0] # отримуємо назву книги з форми
                # Готуємо параметр для запиту:
                search_param = f'%{title}%'  # Тут % -- це символ, який в SQL означає "будь-яка кількість будь-яких символів", див. також: https://www.sqlite.org/lang_corefunc.html#like
                found_books, rcnt = db_helper.find_book(db_helper.sql_books_by_title, search_param)
                if title != '':
                    req_descr = f"частина назви=<b>{title}</b>" # повідомлення для користувача, яке буде показано на сторінці результатів пошуку
                else:
                    req_descr = "(всі книги)"
            else:
                # Показуємо форму для введення (частини)назви книги
                environ, form_data = self.remote_input(self.fmt_html_page('find_by_year.html'))
                print('>>2/year', form_data)

                # Обробляємо отримані дані (які були введені користувачем у формі сторінці 'welcome.html')
                year = form_data.get('year', [''])[0] # отримуємо назву книги з форми
                found_books, rcnt = db_helper.find_book(db_helper.sql_books_by_year, year)
                req_descr = f"рік видання=<b>{year}</b>" # повідомлення для користувача, яке буде показано на сторінці результатів пошуку
            #

            # Показуємо сторінку із результатами пошуку та нашим наступним питанням до користувача (у цьому випадку --
            # чи потрібно ще раз шукати книгу):
            prompt = self.fmt_html_page('search_results.html', html_search_results=found_books, res_count=rcnt, req_descr=req_descr)
            environ, form_data = self.remote_input(prompt)
            print('>>3')

            again = int(form_data.get('again', ['0'])[0]) # отримуємо значення поля "again" з форми
            print('>>4', again)

            if again==0:
                break
            # але якщо again == 'true', то цикл while продовжиться і ми знову покажемо форму для введення назви книги
            self.nsteps += 1
        #
        print('>>5')

        return self.plain_text('Сеанс користувача завершено!')


if __name__ == "__main__":
    # При запуску програми створюємо сервер, який буде обробляти запити користувачів, та передаємо йому
    # обробник запитів -- клас BookFinder, який реалізує основну логіку роботи програми
    s = server_cls.WebInputEnvironmentServer(BookFinder)
    s.run() # запускаємо сервер

