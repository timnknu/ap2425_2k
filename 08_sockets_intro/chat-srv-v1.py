import socket
import threading
import time

HOST = ''  # Комп'ютер для з'єднання
PORT = 5555  # Порт для з'єднання

def work_with_client(conn, address):
    print('New thread created for', address)
    try:
        data = conn.recv(1024)
        s = str(data, encoding='utf-8')
        print('I received:', s, 'from', address)
        while True:
            s = str(time.time()) + '\n'
            conn.sendall(s.encode())
            time.sleep(2)
    except socket.error as e:
        print(e)

try:
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # створити гніздо
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Reuse address
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)  # Reuse port

    srv.bind( (HOST, PORT) )  # зв'язати з комп'ютером та портом
    srv.listen(5)  # очікувати на з'єднання до 5 клієнтів одночасно
    print('=== Chat server ===')

    while True:
        print('** waiting for connection **')
        conn, address = srv.accept()
        th = threading.Thread(target=work_with_client, args=(conn, address))
        th.start()

except:
    print('End')
    pass

