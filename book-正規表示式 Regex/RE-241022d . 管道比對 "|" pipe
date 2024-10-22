
Learning A: 第一次比對符合, 當成 Match 物件返回.
Learning B: 多個模式比對.


## =======================================
Learning A: 第一次比對符合, 當成 Match 物件返回.
## =======================================

import re

heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
mo1.group()

輸出:
'Batman'

mo2 = heroRegex.search('Tina Fey and Batman.')
mo2.group()

輸出:
'Tina Fey'

## =======================================
多個模式比對
以下字串, 以 Bat 開頭, 任何一個符合.
'Batman' 'Batmobile' 'Batcopter' 'Batbat'
## =======================================

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')

# 返回完整比對符合的文字 'Batmobile'.
mo.group()
輸出:
'Batmobile'

# 只要返回第 1 個括號分組比對符合的文字 'mobile'
mo.group(1)
輸出:
'mobile'
