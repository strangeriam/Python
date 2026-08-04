# 在已經定義的 目錄 變數, 再加子目錄.

import os
from pathlib import Path

# Step A: 先切換至實驗路徑.
os.chdir('D:\\Dropbox\\14-Office-TryTryLu\\Python_01_RS232_RebootCycling\\')

# Step B: 原已經定義好路徑.
ENVPATH = Path.cwd()

# 輸出:
WindowsPath('D:/Dropbox/14-Office-TryTryLu/Python_01_RS232_RebootCycling')

# Step C: 再加入延伸子目錄 & 執行檔 --> include/fping.exe
app = ENVPATH / 'include' / 'fping.exe'

# 輸出:
WindowsPath('D:/Dropbox/14-Office-TryTryLu/Python_01_RS232_RebootCycling/include/fping.exe')
