# 事前準備
# 1. 切換工作目錄
import os
os.chdir('D:\\BeeStation\\02_python\\250402_mouseMove4')

# 2. 查看目前工作目錄
from pathlib import Path
Path.cwd() # WindowsPath('D:/BeeStation/02_python/250402_mouseMove4')

# Beginning

# Step 1: 新增一文字檔 hello.txt 於工作目錄 'D:/BeeStation/02_python/250402_mouseMove4'
# Step 2: 開啟此文字檔.
# Way 1
p = Path('D:\\BeeStation\\02_python\\250402_mouseMove4')
helloFile = open(p / 'hello.txt')

# Way 2: 也可這樣開啟.
helloFile = open('D:\\BeeStation\\02_python\\250402_mouseMove4\\hello.txt')

# Way 3:
helloFile = open('D:\\BeeStation\\02_python\\250402_mouseMove4\\hello.txt', 'r')
