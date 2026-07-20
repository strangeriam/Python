import tkinter as tk

root = tk.Tk()
root.geometry('500x200')

def _f_change_port():
	var_portNum.set('5')

var_portNum = tk.StringVar()
var_portNum.set('3')

entry_com = tk.Entry(root, textvariable=var_portNum)
entry_com.pack()
entry_com.config(state=tk.DISABLED)

btn_com_connect = tk.Button(root, text='connect', command=_f_change_port)
btn_com_connect.pack(pady=10)
btn_com_connect.config(state=tk.NORMAL)

root.mainloop()

# ===========================================
輸出:
原本的 Entry 裡顯示的是 3,
按下 Button 後, Entry 的顯示變成 5.
