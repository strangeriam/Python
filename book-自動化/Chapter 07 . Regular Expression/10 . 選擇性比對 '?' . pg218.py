# 電話號碼, 有區號, 沒有區號.

## ========================================
import re

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 415-555-4242')
a = mo1.group()
print(a) # 415-555-4242

mo2 = phoneRegex.search('My number is 555-4242')
b = mo2.group()
print(b) # 555-4242
