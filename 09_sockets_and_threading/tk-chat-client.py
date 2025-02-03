import socket
import threading
import tkinter as tk

#------------------------------------------------------------------------------------------------
# Графічний інтерфейс:

root = tk.Tk()

root.title("chat client")
width=600
height=500
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)

myMessasaEntry=tk.Entry(root)
myMessasaEntry.place(x=30,y=350,width=490,height=43)

sendMyMessageButton=tk.Button(root)
sendMyMessageButton["text"] = "Send"
sendMyMessageButton.place(x=530,y=360,width=70,height=25)

msgsFromOthers=tk.Listbox(root)
msgsFromOthers.place(x=30,y=30,width=499,height=298)

#------------------------------------------------------------------------------------------------
# Робота з сокетами:


#HOST = '212.80.197.117'    # Комп'ютер для з'єднання з сервером
HOST='localhost'
PORT = 5555          # Порт для з'єднання з сервером

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # створити гніздо
sock.connect((HOST, PORT)) # з'єднатися з сервером

# потік для моніторингу повідомлень від сервера
def monitor_replies(sock):
    while True:
        data = sock.recv(1024)  # отримати відповідь сервера
        s = str(data, encoding='utf-8')
        print('>>', s)
        msgsFromOthers.insert(tk.END, s)
        msgsFromOthers.yview(tk.END)

th = threading.Thread(target=monitor_replies, args=(sock,), daemon=True)
th.start()

# функція для відправки повідомлення на сервер, яка викликається при натисканні кнопки
def send_msg_to_server():
    s = myMessasaEntry.get()
    print("send>>", s)
    sock.sendall(bytes(s, encoding='utf-8'))

sendMyMessageButton["command"] = send_msg_to_server

root.mainloop()

sock.close()                   # завершити з'єднання
