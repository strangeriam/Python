import tkinter as tk

root = tk.Tk()
root.geometry('500x200')

def f_change():
	global port
	port = a.get()

a = tk.StringVar()
a.set('')

port = ''

entry1 = tk.Entry(root, textvariable=a, state=tk.NORMAL)
entry1.pack()

btn1 = tk.Button(root, text='CHANGE', command=f_change).pack(pady=10)

root.mainloop()
