# 取得目前所在工作目錄.
# 此程式需要額外 import os 才能顯示當前工作目錄.

from pathlib import Path
Path.cwd() # WindowsPath('C:/Users/Rlulu/AppData/Local/Programs/Python/Python311')

# 變更路徑
import os
os.chdir('C:\\Windows\\System32')
Path.cwd() # WindowsPath('C:/Windows/System32')
