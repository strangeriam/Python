# 檢查目錄是否存在, 如果不存在, 則新建立目錄.
# 實驗前先切換到工作區.
os.chdir('D:\\Dropbox\\14-Office-TryTryLu\\Python_01_RS232_RebootCycling')

# 實驗開始.
import os
from pathlib import Path
import datetime

dayTime = datetime.datetime.now().strftime('%y%m%d')
pfile = Path.cwd() / dayTime
# or
pfile = Path.cwd() / (datetime.datetime.now().strftime('%y%m%d'))

if pfile.exists() and pfile.is_dir():
    print("Dir Exist:", pfile)
else:
    os.makedirs(pfile)
