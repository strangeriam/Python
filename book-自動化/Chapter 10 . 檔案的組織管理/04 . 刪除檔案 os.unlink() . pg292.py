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

# 刪除 資料夾 result, 但資料夾內必須是空的
# ======================================
import os
from pathlib import Path

fname = Path(Path.cwd(), 'result')
print('fname:', fname)

os.rmdir(fname)

# 刪除 資料夾 result, 和其內所有檔案和子資料夾
# =========================================
import shutil, os
from pathlib import Path

os.chdir('D:\\BeeStation\\02_python\\coding')

p = Path(Path.cwd(), 'result')
print('p:', p)

# 如果資料夾存在, 就刪除.
if p.is_dir() == True:
	print('msg: path exist.')
	shutil.rmtree(p)
