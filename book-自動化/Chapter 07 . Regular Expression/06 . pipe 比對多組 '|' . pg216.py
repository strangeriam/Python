# 第一次比對符合, 當成 Match 物件返回.

import re

heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')

mo1.group() # 'Batman'

mo2 = heroRegex.search('Tina Fey and Batman.')
mo2.group() # 'Tina Fey'
