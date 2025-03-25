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

buttonNormal = ttk.Button(root, text="normal", command=f_normal)
buttonActive = ttk.Button(root, text="active", command=f_active)
buttonExit = ttk.Button(root, text="exit", command=f_exit)

buttonNormal.pack(side="top", fill="both", expand=True)
buttonActive.pack(side="top", fill="both", expand=True)
buttonExit.pack(side="top", fill="both", expand=True)

root.mainloop()
