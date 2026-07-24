# 事前準備: 目錄 'D:\\BeeStation\\02_python\\250402_mouseMove4' 內已存在檔案 hello.txt

# Way 1
import os.path
os.path.isfile('D:\\BeeStation\\02_python\\250402_mouseMove4\hello.txt') # True

# True --> 有此檔
# False --> 沒有

# Way 2
from pathlib import Path
fname = Path('D:\\BeeStation\\02_python\\250402_mouseMove4\\hello.txt')

if fname.is_file():
  print('file exist')
else:
  print('no file')
