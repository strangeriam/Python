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
text["state"] = "normal"

text_content = text.get("1.0", "end")

# 可加一 Button, 點擊後印出被輸入的文字.
print(text_content)


root.mainloop()
