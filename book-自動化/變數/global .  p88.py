# 在 函式的頂端加 "global 變數名"
# 告訴 Python 此 變數名 是全域變數.

def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)

# OUTPUT:
spam

# 程式說明
1: 函式 spam() 宣告 eggs 是全域變數 'global eggs'.

