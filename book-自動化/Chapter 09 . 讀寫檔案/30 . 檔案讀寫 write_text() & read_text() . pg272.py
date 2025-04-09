# 事前準備
# 1. 切換工作目錄
import os
os.chdir('D:\\BeeStation\\02_python\\250402_mouseMove4')

# 2. 查看目前工作目錄
from pathlib import Path
Path.cwd() # WindowsPath('D:/BeeStation/02_python/250402_mouseMove4')


# Beginning
from pathlib import Path

p = Path('spam.txt')
p.write_text('Hello, World') # 12

p.read_text() # 'Hello, World'
