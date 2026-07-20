import tkinter as tk
root = tk.Tk()

def _f_showPort():
	print('this is pront...')

btn_com = tk.Button(root, text='connect', command=_f_showPort)
btn_com.pack(pady=10)
btn_com.config(NORMAL)
