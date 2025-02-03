import tkinter as tk

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

def send_msg_to_server():
    print("send")

sendMyMessageButton["command"] = send_msg_to_server


root.mainloop()
