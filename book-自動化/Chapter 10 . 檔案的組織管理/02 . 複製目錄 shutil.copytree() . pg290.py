# 語法: shutil.copytree(source, destination)

# 清除 shell
import os
os.system('cls||clear')

# 實作前, 切換工作路徑.
import os
os.chdir('D:\\BeeStation\\02_python\\coding')

# 查看目前工作目錄
from pathlib import Path
Path.cwd()

# =======================================
import shutil, os
from pathlib import Path

p = Path.cwd()

# 將 目錄 folder1 (含內含檔案) 複製到另一個 新目錄 folder_backup.
shutil.copytree(p / 'folder1', p / 'folder_backup') # WindowsPath('D:/BeeStation/02_python/coding/folder_backup')
