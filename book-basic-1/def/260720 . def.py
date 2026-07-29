
# Way 1: 簡單函數.
# ====================
def sayHello():
  print('hello world')

sayHello()
# 輸出: hello world

# Way 2: 簡單函數 加 return.
# ====================
def sayHello():
  print('hello world')
  return 1

sayHello()
# 輸出:
hello world
1

# Way 3: 帶入 1 個變數.
# ====================
def hello(name):
	print('Hello ' + name)

hello('Lu')
# OUTPUT: Hello Lu

# Way 4: 帶入 多個 變數.
# ====================
def hello(dad_mom, name):
	print('My ' + dad_mom + ' is ' + name + '.')

hello('dad', 'Lu')

輸出:
My dad is Lu.

