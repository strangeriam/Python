;# ====================================================
;# ttk.Frame
;# title . 為視窗命名
;# ====================================================
import tkinter as tk
from tkinter import ttk

def f_greet():
	print(f"Hello, {user_name.get() or 'World'}!")

root = tk.Tk()
root.title("Greeter")

user_name = tk.StringVar()

input_frame = ttk.Frame(root, padding=(20, 10, 20, 0))
input_frame.pack(fill="both")

name_label = ttk.Label(input_frame, text="Name: ")
name_label.pack(side="left", padx=(0, 10))

name_entry = ttk.Entry(input_frame, width=15, textvariable=user_name)
name_entry.pack(side="left", fill="x")
name_entry.focus()

buttons = ttk.Frame(root, padding=(20, 10))
buttons.pack(fill="both")

greet_button = ttk.Button(buttons, text="Greet", command=f_greet)
greet_button.pack(side="left", fill="both", expand=True)

quit_button = ttk.Button(buttons, text="Quit", command=root.destroy)
quit_button.pack(side="left")

root.mainloop()
