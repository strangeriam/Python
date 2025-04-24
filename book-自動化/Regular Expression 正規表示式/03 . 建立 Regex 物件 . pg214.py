
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())

輸出:
Phone number found: 415-555-4242

## ======================================
{3} . 比對這個模式３次
| . 管道 pipe 比對
? . 選擇性比對
* . 零次 或 多次比對

這些字元有特別意義: . ^ $ * + ? { } [ ] \ | ( )


\d . 一位數字字元 (0 ~ 9)
    eg: 415-555-1011
    表示: \d\d\d-\d\d\d-\d\d\d\d

{3} . 比對這個模式３次
    eg: 415-555-1011
    表示: \d{3}-\d{3}-\d{4}

search()
group()
groups()
findall()


search()
    沒找到符合, 返回 None.
    找到符合, 返回 Match 物件.

Match 物件 group()
    返回被尋找字串中符合文字.




