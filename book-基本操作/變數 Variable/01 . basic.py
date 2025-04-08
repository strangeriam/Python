
aaa = 40
aaa
# output: 40

bbb = aaa + 2
bbb
# output: 42

ccc = 30
aaa + ccc
# output: 70

ccc = aaa + ccc
ccc
# output: 70

帶入變數的是字串, 就要用 '' 括起來.
aaa = 'hello'

# 跳出錯誤訊息
>>> aaa = hello
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'hello' is not defined. Did you mean: 'help'?
>>>

aaa = 'hello'
aaa
# output: 'hello'

