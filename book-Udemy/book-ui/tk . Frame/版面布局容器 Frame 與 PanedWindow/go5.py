
# 測試 5 : 使用 PanedWindow 排版 

此例建立一個 PanedWindow 物件 pw, 然後底下程式碼中的 frame 全部改成 pw, 結果如下 :

可見結果與上面用 Frame 排版的效果一模一樣. 

除了直接呼叫元件的 pack() 方法將元件加入父容器 PanedWindow 物件外, 也可以呼叫該物件的 add() 方法, 它預設也是用 tk.LEFT 由左向右將元件放入容器中, 例如 :

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
account.pack(side=tk.LEFT)  # 元件放入視窗
password=tk.Entry(pw, width=10, show='*')  # 密碼輸入框
password.pack(side=tk.LEFT)  # 元件放入視窗
login_btn=tk.Button(pw, text='登入', command=login)  # 登入按鈕
login_btn.pack(side=tk.LEFT)  # 元件放入視窗
placeholder=tk.Label(pw, width=10)  # 佔位用的 Label
placeholder.pack(side=tk.LEFT)
command=tk.Entry(pw, width=20)  # 指令輸入框
command.pack(side=tk.LEFT)  # 元件放入視窗
run_btn=tk.Button(pw, text='執行', command=run)  # 登入按鈕
run_btn.pack(side=tk.LEFT)  # 元件放入視窗
# 建立執行結果文字區域
result=tk.Text(root)
result.pack(fill=tk.BOTH, expand=True)
result.pack()

root.mainloop()
