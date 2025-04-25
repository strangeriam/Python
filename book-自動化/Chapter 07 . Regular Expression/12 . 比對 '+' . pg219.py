# '+' 必須至少出現一次. 這不是可選擇性的.
# 正規表示式 Bat(wo)+man 比對 'The Adventures of Batman' 時找不到符合, 因為至少要出現一次, 所以返回 None.

## ============================================
import re

batRegex = re.compile(r'Bat(wo)+man')

mo1 = batRegex.search('The Adventures of Batwoman')
a = mo1.group()
print(a) # Batwoman

mo2 = batRegex.search('The Adventures of Batwowowowoman')
b = mo2.group()
print(b) # Batwowowowoman

mo3 = batRegex.search('The Adventures of Batman')
c = mo3 == None
print(c) # True
