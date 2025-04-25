import re

batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
a = mo1.group()
print(a) # Batman

mo2 = batRegex.search('The Adventures of Batwoman')
b = mo2.group()
print(b)
