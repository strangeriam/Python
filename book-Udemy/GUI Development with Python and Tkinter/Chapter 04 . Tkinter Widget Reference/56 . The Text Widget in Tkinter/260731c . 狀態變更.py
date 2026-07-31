import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from windows import set_dpi_awareness

set_dpi_awareness()

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget Example")

text = tk.Text(root, height=8)
text.pack()

text.insert("1.0", "Please enter a comment...")

# disabled <-- 變更 不可輸入任何文字.
# normal <-- 允許輸入
text["state"] = "normal"

root.mainloop()
