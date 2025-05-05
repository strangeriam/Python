while True:
  print('who are you?')
  name = input()
  if name != 'Lu':
    continue
  print('hello, Lu. What is the password? (It is a fish.)')
  password = input()
  if password == 'swordfish':
    break
print('Access granted.')
