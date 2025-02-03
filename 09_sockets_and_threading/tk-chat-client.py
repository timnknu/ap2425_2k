import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLineEdit_370=tk.Entry(root)
        GLineEdit_370["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_370["font"] = ft
        GLineEdit_370["fg"] = "#333333"
        GLineEdit_370["justify"] = "center"
        GLineEdit_370["text"] = "Entry"
        GLineEdit_370.place(x=30,y=350,width=490,height=43)

        GButton_952=tk.Button(root)
        GButton_952["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_952["font"] = ft
        GButton_952["fg"] = "#000000"
        GButton_952["justify"] = "center"
        GButton_952["text"] = "Button"
        GButton_952.place(x=530,y=360,width=70,height=25)
        GButton_952["command"] = self.GButton_952_command

        GListBox_318=tk.Listbox(root)
        GListBox_318["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_318["font"] = ft
        GListBox_318["fg"] = "#333333"
        GListBox_318["justify"] = "center"
        GListBox_318.place(x=30,y=30,width=499,height=298)

    def GButton_952_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
