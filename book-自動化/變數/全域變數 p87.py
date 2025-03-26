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
