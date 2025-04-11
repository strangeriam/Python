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

# 將檔案 spam.txt 複製到同 工作目錄下的目錄 some_folder 內.
shutil.copy(p / 'spam.txt', p / 'some_folder') # 'D:\\BeeStation\\02_python\\coding\\some_folder\\spam.txt'

# 將檔案 eggs.txt 複製到下一層目錄 some_folder 內, 並將之改檔名為 eggs2.txt.
shutil.copy(p / 'eggs.txt', p / 'some_folder/eggs2.txt') # WindowsPath('D:/BeeStation/02_python/coding/some_folder/eggs2.txt')
