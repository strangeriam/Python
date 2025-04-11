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
import send2trash

baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable.')
