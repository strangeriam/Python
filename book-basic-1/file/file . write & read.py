# 查看目前工作目錄
from pathlib import Path
Path.cwd()

輸出:
WindowsPath('C:/Users/Rlulu/AppData/Local/Programs/Python/Python311')

# 切換工作目錄 
import os
os.chdir('D:\\Dropbox\\14-Office-TryTryLu\\Python_01_RS232_RebootCycling')

# 寫入檔案
fname = Path('hello.log')
fname.write_text('Hello, World')

# 讀取檔案
fname.read_text()
