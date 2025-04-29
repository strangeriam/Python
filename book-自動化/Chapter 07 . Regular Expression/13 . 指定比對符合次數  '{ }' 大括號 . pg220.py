
import re

haRegex = re.compile(r'(Ha){3}') # {3} ... 大括號中填入比對次數, 此例比對 3 次.

mo1 = haRegex.search('HaHaHa')
a = mo1.group()
print(a) # HaHaHa

mo2 = haRegex.search('Ha')
mo2 == None

輸出: True
