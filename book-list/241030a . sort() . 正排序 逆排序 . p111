Note 1: 支援 數值型 和 字串型 的串列.
Note 2: 不能對有 數值 和 字串 的串列進行排序.
Note 3: 字串排序, 依照 ASCII 順序來排. (不是以字母 aA ~ zZ. 小寫 a 排在大寫 Z 的後面.)
Note 4: 使用字典排序, 就要用 key=str.lower

# 正排序. 數值型, 由大至小.
spam = [2, 5, 3.14, 1, -7]
spam.sort()
spam
輸出:
[-7, 1, 2, 3.14, 5]

# 正排序. 字串型, 依照 ASCII
spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
spam.sort()
spam
輸出:
['ants', 'badgers', 'cats', 'dogs', 'elephants']


# 逆排序. 數值型, 由小至大.
spam = [2, 5, 3.14, 1, -7]
spam.sort(reverse=True)
spam
輸出:
[5, 3.14, 2, 1, -7]

# 逆排序. 字串型, 字母 zZ ~ aA
spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
spam.sort(reverse=True)
spam
輸出:
['elephants', 'dogs', 'cats', 'badgers', 'ants']

# 依照 ASCII 排序 (一般)
spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
輸出:
['Alice', 'Bob', 'Carol', 'ants', 'badgers', 'cats']

## 依照 字典 排序.
spam = ['a', 'z', 'A', 'Z']
spam.sort(key=str.lower)
spam
輸出:
['a', 'A', 'z', 'Z']
