# 目的: 將刪除的檔案先 放到資源回收桶. 還可取回.

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

# 安裝 send2trash
pip install --user send2trash

# Log:
C:\Users\Rlulu>
C:\Users\Rlulu>pip install --user send2trash
Collecting send2trash
  Downloading Send2Trash-1.8.3-py3-none-any.whl.metadata (4.0 kB)
Downloading Send2Trash-1.8.3-py3-none-any.whl (18 kB)
Installing collected packages: send2trash
  WARNING: The script send2trash.exe is installed in 'C:\Users\Rlulu\AppData\Roaming\Python\Python311\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed send2trash-1.8.3

C:\Users\Rlulu>


import send2trash

baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable.')
