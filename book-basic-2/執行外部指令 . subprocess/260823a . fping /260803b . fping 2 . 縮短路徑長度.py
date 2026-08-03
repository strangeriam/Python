# 切換 fping.exe 工作路徑, 操作實驗.
# Path: D:\Dropbox\14-Office-TryTryLu\Python_01_RS232_RebootCycling\

import os
import subprocess
from pathlib import Path

ENVPATH = Path('D:\\Dropbox\\14-Office-TryTryLu\\Python_01_RS232_RebootCycling\\')

# 然後再進入 fping.exe 所在的子目錄 include\ 來執行 fping.exe



subprocess.run(['D:\\Dropbox\\14-Office-TryTryLu\\Python_01_RS232_RebootCycling\\fping.exe', '127.0.0.1', '-n', '2'])
# 輸出
>>> subprocess.run(['D:\\Dropbox\\14-Office-TryTryLu\\Python_01_RS232_RebootCycling\\fping.exe', '127.0.0.1', '-n', '2'])

Fast pinger version 3.00
(c) Wouter Dhondt (http://www.kwakkelflap.com)

Pinging 127.0.0.1 with 32 bytes of data every 1000 ms:

Reply[1] from 127.0.0.1: bytes=32 time=0.1 ms TTL=128
Reply[2] from 127.0.0.1: bytes=32 time=0.0 ms TTL=128

Ping statistics for 127.0.0.1:
        Packets: Sent = 2, Received = 2, Lost = 0 (0% loss)
Approximate round trip times in milli-seconds:
        Minimum = 0.0 ms, Maximum = 0.1 ms, Average = 0.1 ms
CompletedProcess(args=['D:\\Dropbox\\14-Office-TryTryLu\\Python_01_RS232_RebootCycling\\fping.exe', '127.0.0.1', '-n', '2'], returncode=0)
>>>

# 建立 路徑變數 縮短指令長度.
os.chdir('D:\\Dropbox\\14-Office-TryTryLu\\Python_01_RS232_RebootCycling\\')
ENVPATH = Path.cwd()

subprocess.run(['fping.exe', '127.0.0.1', '-n', '2'])


輸出:
>>> import subprocess
>>> subprocess.run(['ping', '127.0.0.1'])

Ping 127.0.0.1 (使用 32 位元組的資料):
回覆自 127.0.0.1: 位元組=32 時間<1ms TTL=128
回覆自 127.0.0.1: 位元組=32 時間<1ms TTL=128
回覆自 127.0.0.1: 位元組=32 時間<1ms TTL=128
回覆自 127.0.0.1: 位元組=32 時間<1ms TTL=128

127.0.0.1 的 Ping 統計資料:
    封包: 已傳送 = 4，已收到 = 4, 已遺失 = 0 (0% 遺失)，
大約的來回時間 (毫秒):
    最小值 = 0ms，最大值 = 0ms，平均 = 0ms
CompletedProcess(args=['ping', '127.0.0.1'], returncode=0)
>>>
