
import re

batRegex = re.compile(r'Bat(wo)*man')

mo1 = batRegex.search('The Adventures of Batman') # # 正規表示式 (wo)* 比對 wo 的結果為 0.
a = mo1.group()
print(a) # Batman

mo2 = batRegex.search('The Adventures of Batwoman') # # 正規表示式 (wo)* 比對 wo 的結果為 1.
b = mo2.group()
print(b) # Batwoman

mo3 = batRegex.search('The Adventures of Batwowowowoman') # 正規表示式 (wo)* 比對 wo 的結果為 4.
c = mo3.group()
print(c) # Batwowowowoman
