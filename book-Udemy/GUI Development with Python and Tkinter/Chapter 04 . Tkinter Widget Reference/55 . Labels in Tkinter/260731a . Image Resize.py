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
# image = Image.open("bordercollieS.png")
photo = ImageTk.PhotoImage(image)
label = ttk.Label(root, image=photo, padding=5)
label.pack()

root.mainloop()
