# 實作前, 切換工作路徑.
import os
os.chdir('D:\\BeeStation\\02_python\\coding')

# 查看目前工作目錄
from pathlib import Path
Path.cwd()

# 刪除 所有副檔名為 .png
# =================================
import os
from pathlib import Path

for filename in Path.cwd().glob('*.png'):
  os.unlink(filename)
  # print(filename)
