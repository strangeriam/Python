# 測試 2 : 改用 Frame 來當元件容器 

# 此例先建立一個 Frame 元件, 然後先後建立以此 Frame 元件為父容器 (不是 root 了) 的輸入框 Entry 與 Button 按鈕等元件, 
# 但 Text 元件依然是以 root 為父元件. 結果如下 :

# 可見輸入框與按鈕都在 Frame 內呈水平排列. 注意, 
# Frame 內的所有元件呼叫 pack() 時均傳入 tk.LEFT, 
# 這表示元件是在 Frame 內由左向右依序排列之意, 並非定位在左邊 (定位要用 ANCHOR 參數); 同理, 
# tk.RIGHT 表示由右向左排列. 如果將上面範例的 command 與 run_btn 兩個元件的 pack() 改為傳入 tk.RIGHT 會讓此兩元件順序顛倒 : 

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
# 建立以 Frame 為父容器的元件
account=tk.Entry(frame, width=10)  # 帳號輸入框
account.pack(side=tk.LEFT)  # 元件放入視窗
password=tk.Entry(frame, width=10, show='*')  # 密碼輸入框
password.pack(side=tk.LEFT)  # 元件放入視窗
login_btn=tk.Button(frame, text='登入', command=login)  # 登入按鈕
login_btn.pack(side=tk.LEFT)  # 元件放入視窗
command=tk.Entry(frame, width=20)  # 指令輸入框
command.pack(side=tk.LEFT)  # 元件放入視窗
run_btn=tk.Button(frame, text='執行', command=run)  # 登入按鈕
run_btn.pack(side=tk.LEFT)  # 元件放入視窗
# 建立執行結果文字區域
result=tk.Text(root)
result.pack(fill=tk.BOTH, expand=True)
result.pack()

root.mainloop()
