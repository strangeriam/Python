import os
from pathlib import Path
import datetime

# 實驗前先切換到工作區.
os.chdir('D:\\Dropbox\\14-Office-TryTryLu\\Python_01_RS232_RebootCycling')


pfile = Path.cwd() # --> 輸出: WindowsPath('D:/Dropbox/14-Office-TryTryLu/Python_01_RS232_RebootCycling')
filename = 'hello_' + (datetime.datetime.now().strftime('%H%M%S')) + '.log' # --> 輸出: 'hello_142453.log'
fname = pfile / filename # --> 輸出: WindowsPath('D:/Dropbox/14-Office-TryTryLu/Python_01_RS232_RebootCycling/hello_142453.log')

appendFile = open(fname, 'a')
appendFile.write('this is line 1.' + '\n')
appendFile.write('this is line 2.' + '\n')
appendFile.close()

appendFile = open(fname)
content = appendFile.read()

# 輸出:
this is line 1.
this is line 2.
