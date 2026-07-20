import tkinter as tk

root = tk.Tk()
root.geometry('500x200')

frame1 = tk.Frame(root)
frame1.pack()

lbl_1 = tk.Label(frame1, text='COM: ')
lbl_1.pack(side=tk.LEFT)

var_portNum = tk.StringVar()
var_portNum.set('')
entry_1 = tk.Entry(frame1, textvariable=var_portNum)
entry_1.pack(side=tk.LEFT)

btn_1 = tk.Button(frame1, text='CONNECT')
btn_1.pack(side=tk.LEFT)

root.mainloop()
