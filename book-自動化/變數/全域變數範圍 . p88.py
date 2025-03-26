1: 函式外的變數, 都是 全域變數.

eggs = 42
spam()
print(eggs)
  
2: 函式宣告 global, 就是 全域變數.

def spam():
    global eggs
    eggs = 'spam'
  
3: 函式內, 沒被宣告為 區域變數的, 就是 全域變數.

def ham():
    print(eggs)
