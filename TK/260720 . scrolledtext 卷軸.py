import tkinter as tk
from tkinter import scrolledtext, messagebox

root = tk.Tk()

lblEvent = tk.Label(root, text='Event Log:')
lblEvent.pack()

logArea = scrolledtext.ScrolledText(root, width=60, height=25, state=tk.DISABLED)
logArea.pack(padx=10, pady=5)

root.mainloop()
