import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from windows import set_dpi_awareness

set_dpi_awareness()

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget Example")

greeting = tk.StringVar()

label = ttk.Label(root, padding=10, textvariable=greeting)
label.pack()

greeting.set("Hello, Lu !")

root.mainloop()
