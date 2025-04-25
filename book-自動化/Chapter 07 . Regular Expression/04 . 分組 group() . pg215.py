# 把區域碼從電話號碼中分開.
group() : Match 物件 group() : 返回被尋找字串中符合文字.

分組: (第一組)-(第二組)
      (\d\d\d)-(\d\d\d-\d\d\d\d)

## =======================
import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')

mo.group(1) # '415'
mo.group(2) # '555-4242'
mo.group(0) # '415-555-4242'
mo.group() # '415-555-4242'
