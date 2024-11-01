birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', "Carol": "Mar 4"}

while True:
  print('Enter a name: (blank to quit)')
  name = input()

  if name == '':
    print('you enter blank')
    break

  if name in birthdays:
    print(birthdays[name] + ' is the birthday of ' + name)
  else:
    print('I do not have birthday information for ' + name)
    print('What is their birthday?')
    bday = input()
    birthdays[name] = bday
    print('Birthday database updated.')

輸出 A:
# 如果輸入 Enter, 則離開 while 迴圈.
Enter a name: (blank to quit)

you enter blank
>>> 

輸出 B:
# 如果輸入在 birthdays 含的名子.
Enter a name: (blank to quit)
Alice
Apr 1 is the birthday of Alice
Enter a name: (blank to quit)

輸出 C:
# 如果輸入不在 birthdays 所含清單裡的名子, 則建立新的 名子 和 生日.
Enter a name: (blank to quit)
Lu
I do not have birthday information for Lu
What is their birthday?
Dec 30
Birthday database updated.
Enter a name: (blank to quit)
Lu
Dec 30 is the birthday of Lu
Enter a name: (blank to quit)

