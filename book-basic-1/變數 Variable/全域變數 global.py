import tkinter as tk

root = tk.Tk()
root.geometry('500x200')

def f_change():
	global port1, port2
	port1 = a.get()
	port2 = b.get()

a = tk.StringVar()
b = tk.StringVar()

a.set('')
b.set('')


port = ''

entry1 = tk.Entry(root, textvariable=a, state=tk.NORMAL)
entry1.pack()

btn1 = tk.Button(root, text='CHANGE', command=f_change).pack(pady=10)

root.mainloop()

# ==========================
print(port)
輸出: ''

在 Entry 輸入 8, 點擊 button "CHANGE"
print(port)
輸出: 8
