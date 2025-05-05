import pyinputplus as pyip

response = pyip.inputNum(limit=2, default='N/A')
# 輸入 hello --> 'hello' is not a number.
# 輸入 world --> 'world' is not a number.
response # 'N/A'
