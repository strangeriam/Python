# 目的: 刪除 檔案和資料夾 到資源回收桶. 還可取回.

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

# 新增檔案
baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable.') # 25
baconFile.close()

# 將檔案丟到 資源回收桶
send2trash.send2trash('bacon.txt')
