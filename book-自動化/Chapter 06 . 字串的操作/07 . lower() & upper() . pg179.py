spam = 'Hello world!'
spam = spam.upper()
spam
輸出:
'HELLO WORLD!'

spam = spam.lower()
spam
輸出:
'hello world!'

## 
print('How are you?')
feeling = input()
if feeling.lower() == 'great':
  print('I feel great too.')
else:
  print('I hope the rest of your day is good.')

輸出 1:
How are you?
great
I feel great too.
>>> 

輸出 2:
How are you?
great
I feel great too.
>>> 

## upper() & lower() 方法會返回字串.
'Hello'.upper()
輸出: 'HELLO'

'Hello'.upper().lower()
輸出: 'hello'

'Hello'.upper().lower().upper()
輸出: 'HELLO'

'Hello'.lower()
輸出: 'hello'

'HELLO'.lower().islower
輸出: True
