import tkinter as tk
from tkinter import ttk
from windows import set_dpi_awareness

set_dpi_awareness()

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget Example")

label = ttk.Label(root, text="Hello, world !!!", padding=20)
label.config(font=("segoe UI", 20))
label.pack()

root.mainloop()
