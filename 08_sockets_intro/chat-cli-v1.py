import socket
import threading

#HOST = '212.80.197.117'    # Комп'ютер для з'єднання з сервером
HOST='localhost'
PORT = 5555          # Порт для з'єднання з сервером

def monitor_replies(sock):
    while True:
        data = sock.recv(1024)  # отримати відповідь сервера
        s = str(data, encoding='utf-8')
        print('>>', s)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # створити гніздо
s.connect((HOST, PORT)) # з'єднатися з сервером

th = threading.Thread(target=monitor_replies, args=(s,))
th.start()

while True:
    to_send = input('?: ') # ввести рядок для перевірки
    if not to_send:
        break
    s.sendall(bytes(to_send, encoding='utf-8'))
s.close()                   # завершити з'єднання

