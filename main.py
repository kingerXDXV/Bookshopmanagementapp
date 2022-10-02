import tkinter as tk

from Components.admin_page import Administrator
from Components.customer_page import openCustomer

frame = tk.Tk()
frame.geometry("700x350+20+20")
frame.title("Book Shop Management System")

customer = tk.Button(frame, text="Customer", width=11, height=4, command=lambda: openCustomer(frame))
customer.place(x=225, y=100)

# calling the administrator class
ad = Administrator()
admin = tk.Button(frame, text="Administrator", width=11, height=4, command=lambda: ad.openAdmin(frame))
admin.place(x=350, y=100)

tk.mainloop()
