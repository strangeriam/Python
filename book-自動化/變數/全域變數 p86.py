# 區域變數 和 全域變數 避免取一樣的 變數名.

# Example Code A
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


# Example Code B
# 全域 和 區域 變數名稱相同.
# 以下程式取了 3 個相同名子的 變數 eggs.
def spam():
    eggs = 'spam local'
    print(eggs)

def bacon():
    eggs = 'bacon local'
    print(eggs)
    spam()
    print(eggs)

eggs = 'global'
bacon()
print(eggs)

# OUTPUT:
bacon local
spam local
bacon local
global

# 說明
eggs 1: 在 spam() 的 eggs = 'spam local'
eggs 2: 在 bacon() 的 eggs = 'bacon local'
eggs 3: 在 全域面數 eggs = 'global'
