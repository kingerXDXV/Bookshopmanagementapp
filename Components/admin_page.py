import tkinter as tk


class Administrator:
    def __init__(self):
        self.adminIsThere = False

    def openAdmin(self, f):
        new_win = tk.Toplevel(f)
        new_win.geometry("500x400")
        new_win.title("Administrator")
        text = tk.Label(new_win, text="Enter Admin Id")
        text.place(x=200, y=150)
        adminId = tk.Entry(new_win)
        adminId.place(x=200, y=200)
        submitId = tk.Button(new_win, text="Submit", command=lambda: self.getValue(adminId))
        submitId.place(x=200, y=250)

    def getValue(self, adminId):
        res = adminId.get()
        self.adminIsThere = False
        print(res)
