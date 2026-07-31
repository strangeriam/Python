import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from windows import set_dpi_awareness

set_dpi_awareness()

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget Example")

image = Image.open("bordercollieS.png").resize((64, 64))
photo = ImageTk.PhotoImage(image)

# 插入文字在 Image 的左邊.
label = ttk.Label(root, text="Image with text.", image=photo, padding=5, compound="right")
label.pack()

root.mainloop()
