import subprocess

command = 'D:\worktmp\plink.exe'
subprocess.run([command, '-ssh', '192.168.2.1'], capture_output=True, text=True)

