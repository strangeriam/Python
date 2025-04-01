除了可以即時顯示文字，也可以使用 Button 元件，設定點擊按鈕後，再顯示輸入文字，同時也可搭配 delete 方法，設計點擊按鈕後清空輸入欄位的內容。

import tkinter as tk

root = tk.Tk()
root.title('oxxo.studio')
root.geometry('200x200')

a = tk.StringVar()
b = tk.StringVar()
a.set('')

def show():
    a.set(b.get())          # 顯示輸入的文字

def clear():
    b.set('')               # 設定變數 b 為空字串
    entry.delete(0,'end')   # 清空輸入欄位內容

label = tk.Label(root, textvariable=a)   # 放入標籤
label.pack()
entry = tk.Entry(root, textvariable=b)   # 放入輸入欄位 ( 變數為 b )
entry.pack()
btn1 = tk.Button(root, text='顯示', command=show)   # 放入顯示按鈕，點擊後執行 show 函式
btn1.pack()
btn2 = tk.Button(root, text='清除', command=clear)  # 放入清空按鈕，點擊後執行 clear 函式
btn2.pack()

root.mainloop()
