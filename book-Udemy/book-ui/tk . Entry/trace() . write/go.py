# trace顧名思義就是追蹤，有兩種trace，一種是write，一種是read

執行結果⬇⬇⬇
邊輸入就會邊在Shell window顯示出來

import tkinter as tk

root = tk.Tk()

root.geometry("350x400+200+300")
root.title('cuteluluWindow')
root.configure(bg="#7AFEC6")
# root.iconbitmap('heart_green.ico')
root.geometry('300x300')

def write(*args):
    print(" changing data ：",zE.get())

zE = tk.StringVar()#字串變數
entry = tk.Entry(root,textvariable=zE)
entry.pack()
zE.trace("w",write) #"w"就是寫入

root.mainloop()
