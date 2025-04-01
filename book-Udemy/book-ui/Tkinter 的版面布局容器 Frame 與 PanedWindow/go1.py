
# 雖然 Frame 物件我還沒時間做一個較完整的測試, 
# 但這周在用 Tkinter 開發公司的維運小軟體時直接拿來上陣使用, 
# 發覺用 Frame 元件搭配最簡單常用的 pack 版面布局也可以將會疊串在一起的 Entry, 
# RadionButton, CheckButton, 與 Button 等元件水平擺放得很整齊.

# 下面以簡化的系統登入與操作按鈕等元件來說明 Frame 在排版上的妙用. 
# 視窗中包含帳號密碼輸入框, 登入按鈕, 指令輸入框, 執行按鈕, 以及一個執行結果文字區域等元件 : 

# 測試 1 : pack() 的堆疊式的版面布局 

account=tk.Entry(root, width=10)  # 帳號輸入框
account.pack()  # 元件放入視窗
password=tk.Entry(root, width=10, show='*')  # 密碼輸入框
password.pack()  # 元件放入視窗
login_btn=tk.Button(root, text='登入', command=login)  # 登入按鈕
login_btn.pack()  # 元件放入視窗
command=tk.Entry(root, width=20)  # 指令輸入框
command.pack()  # 元件放入視窗
run_btn=tk.Button(root, text='執行', command=run)  # 登入按鈕
run_btn.pack()  # 元件放入視窗
# 建立執行結果文字區域
result=tk.Text(root)
result.pack(fill=tk.BOTH, expand=True)
result.pack()

root.mainloop()
