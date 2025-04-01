# trace顧名思義就是追蹤，有兩種trace，一種是write，一種是read
# 首先先示範write

import tkinter as tk

root = tk.Tk()

root.geometry("350x400+200+300")
root.title('cuteluluWindow')
root.configure(bg="#7AFEC6")
root.iconbitmap('heart_green.ico')
root.geometry('300x300')

def write(*args):
    print(" changing data ：",zE.get())

zE = tk.StringVar()#字串變數
entry = tk.Entry(root,textvariable=zE)
entry.pack()
zE.trace("w",write) #"w"就是寫入

root.mainloop()
