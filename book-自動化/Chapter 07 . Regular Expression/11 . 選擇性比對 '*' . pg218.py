# 正規表示式 (wo)* 比對 wo 的結果為 0.
## ========================================
import re

batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
a = mo1.group()
print(a) # Batman

# 正規表示式 (wo)* 比對 wo 的結果為 1.
## ========================================
import re

batRegex = re.compile(r'Bat(wo)*man')
mo2 = batRegex.search('The Adventures of Batwoman')
b = mo2.group()
print(b) # Batwoman

# 正規表示式 (wo)* 比對 wo 的結果為 4.
## ========================================
import re

batRegex = re.compile(r'Bat(wo)*man')
mo3 = batRegex.search('The Adventures of Batwowowowoman')
c = mo3.group()
print(c) # Batwowowowoman
