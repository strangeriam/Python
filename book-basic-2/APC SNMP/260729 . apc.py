# APC DOS command: 
# SnmpGet.exe -r:192.168.0.200 -o:.1.3.6.1.4.1.17420.1.2.9.1.13.0

# $SPort / $SPort2 : 1 (ON) 0 (OFF)
# SnmpSet.exe -r:192.168.0.200 -c:public -o:.1.3.6.1.4.1.17420.1.2.9.1.13.0 -val:$SPort,$PORT2,-1,-1,-1,-1,-1,-1

# Power OFF A & B Both
# SnmpSet.exe -r:192.168.0.200 -c:public -o:.1.3.6.1.4.1.17420.1.2.9.1.13.0 -val:0,0,-1,-1,-1,-1,-1,-1

# 實驗前的準備
# 切換到當前 工作目錄, 然後顯示 當前工作路徑.
import os
os.chdir('D:\\Dropbox\\14-Office-TryTryLu\\Python_01_RS232_RebootCycling')
from pathlib import Path
Path.cwd()


import subprocess

# 打開 PORT A 電源.
subprocess.run(['SnmpSet.exe', '-r:192.168.0.200', '-c:public', '-o:.1.3.6.1.4.1.17420.1.2.9.1.13.0', '-val:1,0,-1,-1,-1,-1,-1,-1'], capture_output=True, text=True)

# 關閉 PORT A 電源.
subprocess.run(['SnmpSet.exe', '-r:192.168.0.200', '-c:public', '-o:.1.3.6.1.4.1.17420.1.2.9.1.13.0', '-val:0,0,-1,-1,-1,-1,-1,-1'], capture_output=True, text=True)

# 讀取 A/B 資訊.
r = subprocess.run(['SnmpGet.exe', '-r:192.168.0.200', '-o:.1.3.6.1.4.1.17420.1.2.9.1.13.0'], capture_output=True, text=True)

print(r.stdout)
