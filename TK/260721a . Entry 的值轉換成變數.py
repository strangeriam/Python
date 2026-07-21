import tkinter as tk

root = tk.Tk()
root.geometry('500x200')

def _f_change_port():
	var_portNum.set('5')

var_portNum = tk.StringVar()
var_portNum.set('3')

entry_com = tk.Entry(root, textvariable=var_portNum, state=tk.NORMAL)
entry_com.pack()

btn_com_connect = tk.Button(root, text='connect', command=_f_change_port)
btn_com_connect.pack(pady=10)

root.mainloop()
