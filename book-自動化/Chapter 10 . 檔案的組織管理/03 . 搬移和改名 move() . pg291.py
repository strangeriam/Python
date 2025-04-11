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
import shutil

# 把檔案 bacon.txt 搬到資料夾 eggs 裡.
shutil.move('D:\\BeeStation\\02_python\\coding\\bacon.txt', 'D:\\BeeStation\\02_python\\coding\\eggs')

# OUTPUT:
'D:\\BeeStation\\02_python\\coding\\eggs\\bacon.txt'

# 把檔案 bacon.txt 搬到資料夾 eggs 裡, 並把 bacon.txt 改名 new_bacon.txt.
shutil.move('D:\\BeeStation\\02_python\\coding\\bacon.txt', 'D:\\BeeStation\\02_python\\coding\\eggs\\new_bacon.txt')

# OUTPUT:
'D:\\BeeStation\\02_python\\coding\\eggs\\new_bacon.txt'
