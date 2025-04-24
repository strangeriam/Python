多個模式比對
以下字串, 以 Bat 開頭, 任何一個符合.
'Batman' 'Batmobile' 'Batcopter' 'Batbat'

## =======================================
import re

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')

mo.group() # 'Batmobile'
