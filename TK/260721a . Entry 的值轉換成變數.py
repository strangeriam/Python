import tkinter as tk

root = tk.Tk()
root.geometry('500x200')

def f_change():
	a.set('5')

a = tk.StringVar()
a.set('3')

entry1 = tk.Entry(root, textvariable=a, state=tk.NORMAL).pack()
btn1 = tk.Button(root, text='CHANGE', command=f_change).pack(pady=10)

root.mainloop()
