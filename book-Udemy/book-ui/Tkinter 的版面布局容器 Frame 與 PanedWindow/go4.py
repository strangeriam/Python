# 測試 4 : 利用無顯示字串的 Label 元件佔位

# 此例在 login 鈕與 command 輸入框之間插入一個無顯示字串 (即 text='') 且設定 width=10 的 Lable 元件當佔位元件 (空元件), 這樣就在兩元件之間製造了 10 個字元寬度的間隔, 結果如下 :

# 注意, 間隔寬度若設太大, 撐破 Frame 的寬度時, 後面的元件可能會跳到下一行而影響版面外觀. 

# 除了 Frame 容器外, 也可以用 PanedWindow 來做版面布局, 茲將上面範例中的 Frame 改成 PanedWindow, 結果相同 :


import tkinter as tk
from tkinter import ttk

def login():
    pass

def run():
    pass

# 建立視窗
root=tk.Tk()  # 建立視窗物件
root.title('Frame + Pack 布局測試') # 設定視窗標題
root.geometry('800x600')  # 設定視窗尺寸

# 建立登入介面與指令輸入介面
frame=tk.Frame(root)  # 外部 Frame 元件
frame.pack()

account=tk.Entry(frame, width=10)  # 帳號輸入框
account.pack(side=tk.LEFT)  # 元件放入視窗
password=tk.Entry(frame, width=10, show='*')  # 密碼輸入框
password.pack(side=tk.LEFT)  # 元件放入視窗
login_btn=tk.Button(frame, text='登入', command=login)  # 登入按鈕
login_btn.pack(side=tk.LEFT)  # 元件放入視窗
placeholder=tk.Label(frame, width=10)  # 佔位用的 Label
placeholder.pack(side=tk.LEFT)
command=tk.Entry(frame, width=20)  # 指令輸入框
command.pack(side=tk.LEFT)  # 元件放入視窗
run_btn=tk.Button(frame, text='執行', command=run)  # 登入按鈕
run_btn.pack(side=tk.LEFT)  # 元件放入視窗
# 建立執行結果文字區域
result=tk.Text(root)
result.pack(fill=tk.BOTH, expand=True)
result.pack()

root.mainloop()
