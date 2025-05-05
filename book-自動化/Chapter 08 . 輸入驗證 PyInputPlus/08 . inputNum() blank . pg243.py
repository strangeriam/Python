>>> import pyinputplus as pyip

>>> response = pyip.inputNum('Enter num: ')
Enter num: # 輸入空白 --> Blank values are not allowed.
Enter num: # 輸入 42
>>> 
>>> response # 42

>>> response = pyip.inputNum(blank=True)

>>> response
''
>>>
