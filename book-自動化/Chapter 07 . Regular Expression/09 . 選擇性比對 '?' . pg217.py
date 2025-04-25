# ? 表示它前面的括號分組在這模式中是 可選擇性的.
# (wo)? 是可選擇性的, wo 是否出現都可以.

## ========================================
import re

batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
a = mo1.group()
print(a) # Batman

mo2 = batRegex.search('The Adventures of Batwoman')
b = mo2.group()
print(b)
