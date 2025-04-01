測試 6 : 使用 PanedWindow 的 add() 方法將元件加入容器 

結果與上面範例相同. 

import tkinter as tk
from tkinter import ttk

def login():
    pass

def run():
    pass

# 建立視窗
root=tk.Tk()  # 建立視窗物件
root.title('pw + Pack 布局測試') # 設定視窗標題
root.geometry('800x600')  # 設定視窗尺寸

# 建立登入介面與指令輸入介面
pw=tk.PanedWindow(root)  # 外部 pw 元件
pw.pack()

account=tk.Entry(pw, width=10)  # 帳號輸入框
pw.add(account)  # 元件放入視窗
password=tk.Entry(pw, width=10, show='*')  # 密碼輸入框
pw.add(password)  # 元件放入視窗
login_btn=tk.Button(pw, text='登入', command=login)  # 登入按鈕
pw.add(login_btn)  # 元件放入視窗
placeholder=tk.Label(pw, width=10)  # 佔位用的 Label
pw.add(placeholder)
command=tk.Entry(pw, width=20)  # 指令輸入框
pw.add(command)  # 元件放入視窗
run_btn=tk.Button(pw, text='執行', command=run)  # 登入按鈕
pw.add(run_btn)  # 元件放入視窗
# 建立執行結果文字區域
result=tk.Text(root)
result.pack(fill=tk.BOTH, expand=True)
result.pack()

root.mainloop()
