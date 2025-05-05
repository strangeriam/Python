# 接受一般常規數字, 還能接受 羅馬數字.

>>> import pyinputplus as pyip

>>> response = pyip.inputNum(allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero'])
# 輸入 XLII
>>> response # 'XLII'

>>> response = pyip.inputNum(allowRegexes=[r'(i|v|x|l|c|d|m)+', r'zero'])
# 輸入 xlii
>>> response # 'xlii'
