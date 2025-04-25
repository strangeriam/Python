這些字元有特別意義: . ^ $ * + ? { } [ ] \ | ( )
| . 管道 pipe 比對
? . 選擇性比對
* . 零次 或 多次比對

{3} . 比對這個模式３次
    eg: 415-555-1011
    表示: \d{3}-\d{3}-\d{4}

其他功能:
search() : 沒找到符合, 返回 None, 找到符合, 返回 Match 物件.
group() : Match 物件 group() : 返回被尋找字串中符合文字.
groups()
findall()

## ======================================
import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # \d . 一位數字字元 (0 ~ 9)
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group()) # Phone number found: 415-555-4242
