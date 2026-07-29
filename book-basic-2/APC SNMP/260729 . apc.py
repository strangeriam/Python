# APC DOS command: 
# SnmpGet.exe -r:192.168.0.200 -o:.1.3.6.1.4.1.17420.1.2.9.1.13.0

# $SPort / $SPort2 : 1 (ON) 0 (OFF)
# SnmpSet.exe -r:192.168.0.200 -c:public -o:.1.3.6.1.4.1.17420.1.2.9.1.13.0 -val:$SPort,$PORT2,-1,-1,-1,-1,-1,-1

# Power A & B OFF Both
# SnmpSet.exe -r:192.168.0.200 -c:public -o:.1.3.6.1.4.1.17420.1.2.9.1.13.0 -val:0,0,-1,-1,-1,-1,-1,-1

import subprocess

command = 'D:\worktmp\plink.exe'
r = subprocess.run([command, '-ssh', '192.168.2.1', '-l', 'root'], capture_output=True, text=True)

print(r.stdout)
