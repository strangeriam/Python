# APC DOS command: 
# snmpget -v 1 -c public 192.168.0.200 .1.3.6.1.4.1.17420.1.2.9.1.13.0
# snmpset -v 1 -c public 192.168.0.200 .1.3.6.1.4.1.17420.1.2.9.1.13.0 s "A,B,-1,-1,-1,-1,-1,-1" 

import subprocess

command = 'D:\worktmp\plink.exe'
r = subprocess.run([command, '-ssh', '192.168.2.1', '-l', 'root'], capture_output=True, text=True)

print(r.stdout)
