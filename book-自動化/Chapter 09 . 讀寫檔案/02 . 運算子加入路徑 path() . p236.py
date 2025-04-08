# 方式 二:
>>>
>>> from pathlib import Path
>>> Path('spam') / 'bacon' / 'eggs'
WindowsPath('spam/bacon/eggs')
>>>
>>>
>>> Path('spam') / Path('bacon/eggs')
WindowsPath('spam/bacon/eggs')
>>>
>>>
>>> Path('spam') / Path('bacon', 'eggs')
WindowsPath('spam/bacon/eggs')
>>>
