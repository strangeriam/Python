import tkinter as tk

root = tk.Tk()

def _f_showPort():
	print('This is _f_showPort.')

btn_com = tk.Button(root, text="connect", command=_f_showPort, width=15)
btn_com.pack(pady=10)
btn_com.config(state=tk.DISABLED)

root.mainloop()

# =======================
state=tk.DISABLED <-- Button 不給點選
state=tk.NORMAL <-- Button 開放點選
