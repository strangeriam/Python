import subprocess

command = 'D:\worktmp\plink.exe'
r = subprocess.run([command, '-ssh', '192.168.2.1', '-l', 'root'], capture_output=True, text=True)

print(r.stdout)
