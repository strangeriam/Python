
# 測試 3 : 呼叫 pack() 傳入 side=tk.RIGHT 為由右向左排列

# 此例程式碼與上面不同之處僅在於 command 與 run_btn 這兩個元件呼叫 pack() 時傳入 side=tk.RIGHT 而已, 結果兩個元件就由右向左排列 :

# 所以放入 Frame 容器的元件呼叫 pack() 時一律傳入 side_tk.LEFT 即可. 

# 如果要讓這些 Frame 內水平排列的元件有所區隔, 可以用一個無顯示字串的 Label 來當隱形的佔位元件, 可透過 width (字元數, 不是 px) 來控制間隔距離, 例如 :

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
command=tk.Entry(frame, width=20)  # 指令輸入框
command.pack(side=tk.RIGHT)  # 元件放入視窗
run_btn=tk.Button(frame, text='執行', command=run)  # 登入按鈕
run_btn.pack(side=tk.RIGHT)  # 元件放入視窗
# 建立執行結果文字區域
result=tk.Text(root)
result.pack(fill=tk.BOTH, expand=True)
result.pack()

root.mainloop()
