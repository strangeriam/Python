import tkinter as tk
from tkinter import scrolledtext, messagebox

root = tk.Tk()
root.geometry('400x500')

frameMID1 = tk.Frame(root)
frameMID1.pack()

lblEvent = tk.Label(frameMID1, text='Event Log:')
lblEvent.pack()

logArea = scrolledtext.ScrolledText(frameMID1, width=60, height=25, state=tk.DISABLED)
logArea.pack(padx=10, pady=5)

root.mainloop()
