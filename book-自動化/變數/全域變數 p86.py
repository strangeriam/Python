# 區域變數 和 全域變數 避免取一樣的 變數名.

def spam():
    print(eggs)

eggs = 42

spam()
print(eggs)

# OUTPUT
42
42

# 說明:
函式 spam() 沒定義 變數 eggs,
當 spam() 使用 變數 eggs 時,
Python 會認定取用的是 全域變數(外部) 的變數 eggs
所以從 spam() 印出 42
