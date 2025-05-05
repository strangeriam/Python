>>> import pyinputplus as pyip

>>> response = pyip.inputStr(allowRegexes=[r'caterpillar', 'category'], blockRegexes=[r'cat'])
# 輸入 cat --> This response is invalid.
# 輸入 catastrophe --> This response is invalid.
# 輸入 category
>>>

>>> response # 'category'
