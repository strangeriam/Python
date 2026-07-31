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

# 1.0 <-- 文字放的位置.
# 1 --> 第幾行, 此為 第一行.
# 0 --> 第幾個字串, 此為第一個字.
text.insert("1.0", "Please enter a comment...")

root.mainloop()
