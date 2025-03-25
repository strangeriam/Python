import tkinter as tk
from tkinter import ttk

import sys, time, datetime

def f_timeNow():
	dt = datetime.datetime.now()
	return dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second

def f_normal():
	nowTime = f_timeNow()
	print('click normal .. ', nowTime)

def f_active():
	nowTime = f_timeNow()
	print("click active .. ", nowTime)

def f_exit():
	nowTime = f_timeNow()
	print("click exit .. ", nowTime)
	time.sleep(1)
	sys.exit()


root = tk.Tk()

main = ttk.Frame(root)
main.pack(side="left", fill="both", expand=True)

buttonNormal = ttk.Button(main, text="normal", command=f_normal).pack(side="top", fill="both", expand=True)
buttonActive = ttk.Button(main, text="active", command=f_active).pack(side="top", fill="both", expand=True)
buttonExit = ttk.Button(root, text="exit", command=f_exit).pack(side="top", fill="both", expand=True)

root.mainloop()
