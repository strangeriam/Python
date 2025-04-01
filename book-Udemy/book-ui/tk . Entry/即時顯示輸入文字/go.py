下方的程式碼放入一個 Label 和一個 Entry，兩個元件都使用 textvariable 共用變數 a，執行後當輸入框內容發生改變，Label 的內容也會跟著變化。


import tkinter as tk

root = tk.Tk()
root.title('oxxo.studio')
root.geometry('200x200')

a = tk.StringVar()   # 建立文字變數
a.set('')            # 一開始設定沒有內容

tk.Label(root, textvariable=a).pack()  # 放入 Label
tk.Entry(root, textvariable=a).pack()  # 放入 Entry

root.mainloop()
