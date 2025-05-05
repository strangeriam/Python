# 條件 A
if 'A':
    ...
elif 'B':
    ...
else:
    ...

# 條件 B
'=='
'!='
'<'
'>'

## =========================================
name = 'Mary'
password = 'swordfish'

if name == 'Mary':
    print('Hello Mary')
    if password == 'swordfish':
        print('Access granted.')
    else:
        print('Wrong password.')
# 輸出:
Hello Mary
Access granted.
[Finished in 88ms]

## =========================================
name = 'Lu'
age = 3000

# '=='
if name == 'Lu':
    print('Hello Lu')
elif age < 12:
    print('You are not Lu, Kiddo.') ;# kiddo 小子
elif age > 2000:
    print('Unlike you, Lu is not an undead, immprtal vampire.')
elif age > 100:
    print('You are not Lu, grannie.')

# 輸出:
Hello Lu
[Finished in 103ms]

## =========================================
name = 'Carol'
age = 3000

if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, Kiddo')
else:
    print('You are neither Alice nor a little kid.')

# 輸出:
You are neither Alice nor a little kid.

