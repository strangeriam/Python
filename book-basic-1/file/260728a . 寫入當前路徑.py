
# Step 1:
# 先切換到執行實驗的 工作目錄.
# 工作目錄: D:\Dropbox\14-Office-TryTryLu\Python_01_RS232_RebootCycling\
import os
pfile = 'D:\\Dropbox\\14-Office-TryTryLu\\Python_01_RS232_RebootCycling'
os.chdir(pfile)

# Step 2:
# 檢查目前所在目錄.
from pathlib import Path
Path.cwd()

# 輸出:
WindowsPath('D:/Dropbox/14-Office-TryTryLu/Python_01_RS232_RebootCycling')
