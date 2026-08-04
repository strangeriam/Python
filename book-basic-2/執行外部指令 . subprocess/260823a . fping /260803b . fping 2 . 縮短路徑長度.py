# 切換 fping.exe 工作路徑, 操作實驗.
# Path: D:\Dropbox\14-Office-TryTryLu\Python_01_RS232_RebootCycling\
import os
from pathlib import Path
import subprocess

os.chdir('D:\\Dropbox\\14-Office-TryTryLu\\Python_01_RS232_RebootCycling\\')
ENVPATH = Path.cwd()

# 定義 fping.exe 所在的子目錄 include\ 來執行 fping.exe
app = ENVPATH / 'include' / 'fping.exe'

subprocess.run([app, '127.0.0.1', '-n', '2'])

# 輸出
Fast pinger version 3.00
(c) Wouter Dhondt (http://www.kwakkelflap.com)

Pinging 127.0.0.1 with 32 bytes of data every 1000 ms:

Reply[1] from 127.0.0.1: bytes=32 time=0.1 ms TTL=128
Reply[2] from 127.0.0.1: bytes=32 time=0.1 ms TTL=128

Ping statistics for 127.0.0.1:
        Packets: Sent = 2, Received = 2, Lost = 0 (0% loss)
Approximate round trip times in milli-seconds:
        Minimum = 0.1 ms, Maximum = 0.1 ms, Average = 0.1 ms
CompletedProcess(args=[WindowsPath('D:/Dropbox/14-Office-TryTryLu/Python_01_RS232_RebootCycling/include/fping.exe'), '127.0.0.1', '-n', '2'], returncode=0)
>>>
