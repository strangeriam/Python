
'Hello, world!'.partition('w')
輸出:
('Hello, ', 'w', 'orld!')

'Hello, world!'.partition('world')
輸出:
('Hello, ', 'world', '!')

partition() 呼叫的字串出現很多個, 則以第 1 個出現的分隔字串為中心來分拆.
'Hello, world!'.partition('o')
輸出:
('Hell', 'o', ', world!')

如果找不到分隔字串, 則返回的多元組中會以原本整個字串為第 1 個項目, 第 2 和 第 3 個項目為空字串.
'Hello, world!'.partition('XYZ')
輸出:
('Hello, world!', '', '')

多重指定處理, 把返回的內容指定到 3 個變數中.
before, sep, after = 'Hello, world!'.partition(' ')

before
輸出:
'Hello,'

sep
輸出:
' '

after
輸出:
'world!'
