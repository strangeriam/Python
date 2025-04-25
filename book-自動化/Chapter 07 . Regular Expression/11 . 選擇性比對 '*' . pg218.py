# 正規表示式 (wo)* 比對 wo 的結果為 0.
## ========================================
import re

batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
mo1.group() # Batman


正規表示式 (wo)* 比對 wo 的結果為 1.
## ========================================
import re

mo2 = batRegex.search('The Adventures of Batwoman')
mo2.group()
輸出: 'Batwoman'
說明: 正規表示式 (wo)* 比對 wo 的結果為 1.


正規表示式 (wo)* 比對 wo 的結果為 4.
## ========================================
import re

mo3 = batRegex.search('The Adventures of Batwowowowoman')
mo3.group()
輸出: 'Batwowowowoman'
說明: 正規表示式 (wo)* 比對 wo 的結果為 4.
