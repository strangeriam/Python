import datetime

# Way 1
nowTime = datetime.datetime.now().strftime('%H%M%S')
fname = 'hello_' + nowTime + '.log'

# Way 2 + 當前完整工作路徑
import os
from pathlib import Path

pfile = Path.cwd()
filename = 'hello_' + (datetime.datetime.now().strftime('%H%M%S')) + '.log'

fname = pfile / filename

輸出:
WindowsPath('D:/Dropbox/14-Office-TryTryLu/Python_01_RS232_RebootCycling/hello_141756.log')
