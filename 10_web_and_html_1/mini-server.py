import socket
import threading
import time

HOST = ''  # Комп'ютер для з'єднання
PORT = 5556  # Порт для з'єднання

def work_with_client(conn, address):
    print('New thread created for', address)
    while True:
        b = conn.recv(1)
        if len(b) == 0:
            break
        #print(b.decode('utf-8'), end='')
        print(str(b, encoding='utf-8'), end='')
    #


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

