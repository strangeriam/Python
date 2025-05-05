>>> import pyinputplus as pyip

>>> response = pyip.inputNum(blockRegexes=[r'[02468]$'])
# 輸入 42 --> This response is invalid.
# 輸入 44 --> This response is invalid.
# 輸入 43
>>> response # 43
