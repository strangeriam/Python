# moose 駝鹿

# 注意 1, 不可使用
# spam = spam.append('moose')
# spam = spam.insert(1, 'chicken')

# 注意 2, 不可數字和字串混搭.

# append() . 把引數 加到串列的尾端.
spam = ['cat', 'dog', 'bat']
spam.append('moose')
spam # ['cat', 'dog', 'bat', 'moose']

# insert() . 把引數 加到 索引 (0 ~) 的位置.
spam = ['cat', 'dog', 'bat']
spam.insert(1, 'chicken')
spam #['cat', 'chicken', 'dog', 'bat']
