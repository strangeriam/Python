def spam():
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0

spam()

# OUTPUT
99

程式流程:
1: 呼叫函式 spam(), 區域變數 eggs = 99
2: 呼叫函式 bacon(), 區域變數 ham = 101, 區域變數 eggs = 0
3: 函式 bacon() 返回時, 其區域變數 ham 和 eggs 就會被銷毀.
4: 函式 spam() 繼續執行 print(eggs), 此 eggs 是 spam() 的區域變數值 99
5: 所以印出來的值是 99
