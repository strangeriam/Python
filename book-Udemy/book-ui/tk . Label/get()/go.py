import tkinter as tk

root = tk.Tk()

root.geometry("350x400+200+300")
root.title('cuteluluWindow')
root.configure(bg="#7AFEC6")
# root.iconbitmap('heart_green.ico')  # 沒圖, 所以 Remark
root.geometry('300x300')

def GET():
    if Z.get() == "":
        Z.set("cuteluluWindow")
    else:
        Z.set("")

Z = tk.StringVar() #字串變數

L= tk.Label (root, textvariable=Z,fg="#FFAAD5",bg="#7AFEC6", font=("Algerian","16","bold"),width=25,height=2)
L.pack()

btn = tk.Button(root,text="Click Me",relief="sunken",command=GET)
btn.pack()

root.mainloop()
