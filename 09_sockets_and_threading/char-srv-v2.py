import socket
import threading
import time

HOST = ''  # Комп'ютер для з'єднання
PORT = 5555  # Порт для з'єднання

def work_with_client(conn, address):
    print('New thread created for', address)
    user_nickname = None
    sinp = conn.makefile('rb', 0)  # створюємо файловий об'єкт для зчитування з сокету
    try:
        while True:
            data = sinp.readline()
            if len(data) == 0: # якщо сервер помітив, що клієнт відключився, то видалити його зі "списку розсилки"
                client_sockets.remove(conn)
                break
            # а іначе відправити повідомлення, отримане від клієнта, всім клієнтам:
            s = str(data, encoding='utf-8').rstrip()
            print('I received:', s, 'from', address)
            if user_nickname is None:
                user_nickname = s
                for cs in client_sockets:
                    cs.sendall( bytes(f'Hey! We have a new participant: {user_nickname} from {address}', encoding='utf-8') )
            else:
                s = user_nickname + ' --> ' + s
                for cs in client_sockets:
                    cs.sendall( bytes(s, encoding='utf-8') )
        #
        s = user_nickname + ' has left chat'
        for cs in client_sockets:
            cs.sendall(bytes(s, encoding='utf-8'))
    except socket.error as e:
        print(e)

try:
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # створити гніздо
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Reuse address
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)  # Reuse port

    srv.bind( (HOST, PORT) )  # зв'язати з комп'ютером та портом
    srv.listen(5)  # очікувати на з'єднання *до 5 клієнтів одночасно*
    print('=== Chat server ===')

    client_sockets = []

    while True:
        print('** waiting for connection **')
        conn, address = srv.accept()
        client_sockets.append(conn)
        th = threading.Thread(target=work_with_client, args=(conn, address))
        th.start()

except:
    print('End')
    pass

