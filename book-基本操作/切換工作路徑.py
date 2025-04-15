# 切換工作路徑
import os
os.chdir('C:\\Windows\\System32')

# 檢查工作路徑
from pathlib import Path
Path.cwd() # WindowsPath('C:/Windows/System32')
