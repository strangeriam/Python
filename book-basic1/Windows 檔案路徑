## 設定檔案路徑

# 方式 一:
from pathlib import Path
myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
	print(Path(r'D:\Dropbox\12-Office-TryTryLu\Learning_02_Python', filename))

## 輸出:
D:\Dropbox\12-Office-TryTryLu\Learning_02_Python\accounts.txt
D:\Dropbox\12-Office-TryTryLu\Learning_02_Python\details.csv
D:\Dropbox\12-Office-TryTryLu\Learning_02_Python\invite.docx


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

