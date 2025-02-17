import socket
import threading
import time

HOST = ''  # Комп'ютер для з'єднання
PORT = 5556  # Порт для з'єднання

def work_with_client(conn, address):
    print('New thread created for', address)
    # sinp = conn.makefile('rb', 0)  # створюємо файловий об'єкт для зчитування з сокету
    # request_lines = []
    # while True:
    #     data = sinp.readline()
    #     if len(data) == 0:  # в HTTTP-запитах порожній рядок означає кінець запиту
    #         break
    #     request_lines.append( str(data, encoding='utf-8') )
    s = ''
    while True:
        b = conn.recv(1)
        s = s + str(b, encoding='utf-8')
        if s.endswith('\r\n\r\n'):
            break
    request_lines = s.split('\r\n')

    print('Request lines', request_lines)
    resp_str = "HTTP/1.1 200 OK\n"
    resp_str = resp_str + "Content-Type: text/html\n"
    resp_str = resp_str + "\n"
    resp_str = resp_str + "Hello, world!\n\n"
    resp_str = resp_str + "the first line of request was: " + request_lines[0] + "\n"
    conn.sendall( bytes(resp_str, encoding='utf-8') )
    conn.close()
#



    #


try:
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # створити гніздо
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Reuse address
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)  # Reuse port

    srv.bind( (HOST, PORT) )  # зв'язати з комп'ютером та портом
    srv.listen(5)  # очікувати на з'єднання *до 5 клієнтів одночасно*
    print('=== Chat server ===')

    while True:
        print('** waiting for connection **')
        conn, address = srv.accept()
        th = threading.Thread(target=work_with_client, args=(conn, address))
        th.start()

except:
    print('End')
    pass

