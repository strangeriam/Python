以下字串, 以 Bat 開頭, 任何一個符合.
'Batman' 'Batmobile' 'Batcopter' 'Batbat'

## =======================================
import re

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
a = mo.group()
print(a) # Batmobile

b = mo.group()
print(b) # mobile
