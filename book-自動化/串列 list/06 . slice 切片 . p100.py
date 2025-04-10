spam[0:4]
中括號 [] 裏頭有兩個整數. 
整數 1, 是切片 (slice) 的起始.
整數 2, 是切片 (slice) 的結尾.
其求值為一個新的串列值.

== 方式 A ==
spam = ['cat', 'bat', 'rat', 'elephant']

spam[0:4]
輸出:
['cat', 'bat', 'rat', 'elephant']
--> 從第 0 個開始, 共取 4 個.
--> 'cat', 'bat', 'rat', 'elephant' . 從 'cat', 'bat', 'rat', 'elephant'

spam[1:3]
輸出:
['bat', 'rat']
--> 從第 1 個開始, 共取 3 個.
-- 'bat', 'rat' . 從 'cat', 'bat', 'rat'

;# 取到倒數第 1 個 rat (倒數第 0 個是 elephant)
spam[0:-1]
輸出:
['cat', 'bat', 'rat']


== 方式 B ==
spam = ['cat', 'bat', 'rat', 'elephant']

spam[:2]
輸出:
['cat', 'bat']
--> 相當於 spam[0:2]
--> 從 0 個開始, 共取 2 個.

;# 取到最後 1 個 elephant.
spam[1:]
輸出:
['bat', 'rat', 'elephant']
相當於 spam[1:]

spam[:]
輸出:
['cat', 'bat', 'rat', 'elephant']
