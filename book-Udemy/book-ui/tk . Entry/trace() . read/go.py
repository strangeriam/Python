執行結果⬇⬇⬇
這邊用了一個set()方法，這方法就是可以按read按鈕後，顯示在介面上


import tkinter as tk

root = tk.Tk()

root.geometry("350x400+200+300")
root.title('cuteluluWindow')
root.configure(bg="#7AFEC6")
# root.iconbitmap('heart_green.ico')
root.geometry('300x150')


def callbackW(*args):#*args可以直接傳遞參數內容，因為目前還不需要傳遞參數
    zl.set(zE.get())

def callbackR(*args):
    print(" 資料被讀取了 ")

def read():
    print(" read the data :",zE.get())

zE = tk.StringVar()#字串變數
entry = tk.Entry(root,textvariable=zE)
entry.pack()
zE.trace("w",callbackW)#如有更改執行這行callbackW
zE.trace("r",callbackR)#如有讀取執行這行callbackR

zl = tk.StringVar()#字串變數
lab = tk.Label(root,textvariable=zl)
zl.set(" 顯示於此 ")
lab.pack(pady=5,padx=10)

btn = tk.Button(root,text=" read ",command=read)
btn.pack(pady=10)

root.mainloop()
