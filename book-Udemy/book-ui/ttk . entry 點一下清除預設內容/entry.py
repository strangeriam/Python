
# UI 呈現說明:
# 兩個 Entry 元件都呼叫 bind() 方法監聽滑鼠左鍵的按一下鈕 (Button-1) 事件, 並綁定事件處理函式.
# 在事件處理函式中, 呼叫 Entry 物件的 delete(0, tk.END) 方法即可刪除 Entry 內預設值或先前輸入的內容.

import tkinter as tk
from tkinter import ttk

root=tk.Tk()  
root.title('點擊 Entry 清除內容測試') 
root.geometry('300x150') 

def clear_account_entry(event):   # 清除帳號框內容
    account_entry.delete(0, tk.END)    # 刪除開頭與結尾索引之間的 (全部) 內容
    
def clear_password_entry(event):  # 清除密碼框內容
    password_entry.delete(0, tk.END)   # 刪除開頭與結尾索引之間的 (全部) 內容
    
def login():
    pass
        
account=tk.StringVar()
account_entry=tk.Entry(root, textvariable=account)
account_entry.insert(0, '請輸入帳號')
account_entry.bind('<Button-1>', clear_account_entry)
account_entry.pack()
password=tk.StringVar()
password_entry=tk.Entry(root, textvariable=password)
password_entry.insert(0, '請輸入密碼')
password_entry.bind('<Button-1>', clear_password_entry)
password_entry.pack()
login_btn=ttk.Button(root, text='登入', command=login)
login_btn.pack()
root.mainloop()
