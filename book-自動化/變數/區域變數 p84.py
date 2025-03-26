# 錯誤變數的使用
def spam():
    eggs = 31337
spam()

print(eggs)

# Error message
Traceback (most recent call last):
  File "D:\BeeStation\02_python\250326_mouseMove2\try.py", line 4, in <module>
    print(eggs)
          ^^^^
NameError: name 'eggs' is not defined

# 說明
eggs 變數只作用於 呼叫 spam() 的區域變數.
當 spam 函數返回後, 區域變數 eggs 就銷毀.
所以會出現 "NameError: name 'eggs' is not defined".
