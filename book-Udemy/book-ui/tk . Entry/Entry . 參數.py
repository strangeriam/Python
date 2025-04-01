tk.Entry(f2_fflow1, textvariable=var_flow1_x, fg="#FFAAD5", bg="#7AFEC6", font=("Algerian","16","bold"), width=5)

textvariable=var_flow1_x
fg="#FFAAD5"
bg="#7AFEC6"
font=("Algerian","16","bold")
width=25

Entry 參數設定 
加入 Entry 之後，可以透過 Entry 的參數調整內容的樣式，下方列出 Entry 和其他元件相同的參數：

參數	說明
width	寬度，單位是字元數。
height	高度，單位是字元數。
padx	內容和標籤左右邊界的間距 ( px )，預設 1。
pady	內容和標籤上下邊界的間距 ( px )，預設 1。
bg/background	背景顏色，可以使用十六進位色碼或顏色名稱。
fg/foreground	文字顏色，可以使用十六進位色碼或顏色名稱。
font	字型設定，包含字體、大小 ( px )、粗體 ( bold )、斜體 ( italic )。
justify	多行文字的對齊方式，可以設定 left、right、center，預設 center。
cursor	滑鼠移動到標籤的樣式，可以設定 arrow、circle、cross、plus...等，預設 arrow。
relief	邊框樣式，可以設定 flat、sunken、raised、groove、ridge、solid，預設 flat。
bd/borderwidth	邊框粗細，預設 1。
textvariable	文字內容的變數名稱，如果變數被修改，文字就會發生變化。
wraplength	一段文字超過多少寬度 ( px ) 會換行。



下方是 Entry 單行輸入框行為相關的參數：

參數	說明
show	指定顯示的字元為某個符號，例如輸入密碼，可以指定 show='*'，輸入的內容就會變成星號。
selectborderwidth	選取輸入框內容的外框寬度。
selectbackground	選取輸入框內容的背景顏色。
selectforeground	選取輸入框內容的文字顏色。
xscrollcommand	與 set() 方法搭配，加上水平捲軸。
state	狀態，tk.NORMAL 可使用 ( 預設 )、tk.DISABLED 不可使用。


Entry 內容操作方法 
透過下列方法，可以取得或刪除 Entry 單行輸入框的內容，或針對內容進行一些相關操作：

方法	參數	說明
get()		取得輸入框的內容。
delete()	first, last=None	指定刪除 first～last 區間的內容。
icursor()	index	移動輸入標記到指定內容索引值。
index()	index	取得指定的索引值。
insert()	index, s	在指定索引的位置插入內容。
select_adjust()	index	選取索引值位置和之前的內容。
select_clear()		清空輸入欄位內容。
select_from()	index	設定選取的位置。
select_present()		如果有選取則回傳 True，否則 False。
select_range()	start, end	回傳 start～end 範圍內的值。
select_to()	index	選擇指定索引值的內容。
xview()	index	如果文字過長，指定要看到哪個索引值。
xview_scroll()	number, what	捲動捲軸到指定位置。
