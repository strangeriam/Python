
# Step 1:
# 先切換到執行實驗的 工作目錄.
# 工作目錄: D:\Dropbox\14-Office-TryTryLu\Python_01_RS232_RebootCycling\
import os
os.chdir('D:\\Dropbox\\14-Office-TryTryLu\\Python_01_RS232_RebootCycling')

# Step 2:
# 檢查目前所在目錄.
from pathlib import Path
pfile = Path.cwd()

# 輸出:
WindowsPath('D:/Dropbox/14-Office-TryTryLu/Python_01_RS232_RebootCycling')

# Step 3:
# 建立可 append 的檔案.
fname = (pfile / 'hello.log')
appendFile = open(fname, 'a')

# 只寫入 1 行
appendFile.write('this is line 1.')
appendFile.close()

# 再寫入 2 行
appendFile = open(fname, 'a')
appendFile.write('this is line 2.')
appendFile.write('this is line 3.')
appendFile.close()

