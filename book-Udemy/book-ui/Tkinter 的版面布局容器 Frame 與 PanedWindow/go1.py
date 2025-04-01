
# 雖然 Frame 物件我還沒時間做一個較完整的測試, 
# 但這周在用 Tkinter 開發公司的維運小軟體時直接拿來上陣使用, 
# 發覺用 Frame 元件搭配最簡單常用的 pack 版面布局也可以將會疊串在一起的 Entry, 
# RadionButton, CheckButton, 與 Button 等元件水平擺放得很整齊.

# 下面以簡化的系統登入與操作按鈕等元件來說明 Frame 在排版上的妙用. 
# 視窗中包含帳號密碼輸入框, 登入按鈕, 指令輸入框, 執行按鈕, 以及一個執行結果文字區域等元件 : 

# 測試 1 : pack() 的堆疊式的版面布局 

# 可見 pack 版面管理員的布局方式基本上就是由上而下堆疊,
# 雖然可以在呼叫 pack() 時傳入 side=tk.RIGHT/LEFT/TOP/BOTTOM 指定上下左右之垂直水平位置,
# 或傳入 anchor=tk.E/W/S/N/CENTER/NW/NE/SW/SE 來定位元件在父容器中的位置,
# 但光用 side 與 anchor 參數無法達成讓上方輸入框與按鈕元件以水平方式排在最上方, 且登入在左, 執行在右的需求. 

# 解決辦法之一是使用 Frame 容器來放置元件,
# 並且每個元件在呼叫 pack() 時傳入 side=tk.LEFT 指定由左向右水平排列, 版面結構如下圖所示 :

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
