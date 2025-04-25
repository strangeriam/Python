# 把區域碼從電話號碼中分開. 使用 groups()

分組: (第一組)-(第二組)
      (\d\d\d)-(\d\d\d-\d\d\d\d)

## =======================
import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')

mo.groups() # ('415', '555-4242')

areaCode, mainNumber = mo.groups() # 可多重指定, 將每個值指定給獨立變數.
print(areaCode) # 415
print(mainNumber) # 555-4242
