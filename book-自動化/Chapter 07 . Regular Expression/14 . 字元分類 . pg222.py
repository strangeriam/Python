
\d . 0 ~ 9 的任何數字, 像是 (0|1|2|3|4|5|6|7|8|9)
\D . 除了 0 ~ 9 的數字以外的任何字元.
\w . 任何字母, 數字, 底線 字元 (想成是 比對單字字元).
\W . 除了字母, 數字, 底線 以外的任何字元.
\s . 空格, 定位符號, 換行符號 (想成是 比對空白字元).
\S . 除了空格, 定位符號, 換行符號 以外的任何字元.

[0-5] . 只比對 數字 0 到 5.
[a-zA-Z] . 僅比對字母.

# ===========================================
import re

xmasRegex = re.compile(r'\d+\s\w+')
d = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')

print(d)

# OUTPUT:
['12 drummers', '11 pipers', '10 lords', '9 ladies', '8 maids', '7 swans', '6 geese', '5 rings', '4 birds', '3 hens', '2 doves', '1 partridge']
