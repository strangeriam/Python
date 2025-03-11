;# ====================================================
;# 基本 Button 的語法
;# ====================================================
import tkinter as tk
from tkinter import ttk

def f_greet():
	print("Hello, World!")

root = tk.Tk()

greet_button = ttk.Button(root, text="Greet", command=f_greet)
greet_button.pack()

root.mainloop()


;# ====================================================
;# 預設物件 root.destroy
;# ====================================================
import tkinter as tk
from tkinter import ttk

def f_greet():
	print("Hello, World!")

root = tk.Tk()

greet_button = ttk.Button(root, text="Greet", command=f_greet)
greet_button.pack(side="left", fill="both", expand=True)

quit_button = ttk.Button(root, text="Quit", command=root.destroy)
quit_button.pack(side="left")

root.mainloop()
