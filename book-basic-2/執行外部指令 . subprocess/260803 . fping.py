# 切換 fping.exe 工作路徑
# Path: D:\Dropbox\14-Office-TryTryLu\Python_01_RS232_RebootCycling\include\

import os
os.chdir('D:\\BeeStation\\03_python_project\\250414_mouseScreenControl\\Material')

import subprocess
subprocess.run(['ping', '127.0.0.1'])


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
