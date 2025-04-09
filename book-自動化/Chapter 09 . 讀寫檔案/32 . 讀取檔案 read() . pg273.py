# 事前準備: 切換工作目錄 & 查看目前工作目錄
import os
os.chdir('D:\\BeeStation\\02_python\\250402_mouseMove4')

from pathlib import Path
Path.cwd() # WindowsPath('D:/BeeStation/02_python/250402_mouseMove4')

# Beginning

# Step 1: 新增一文字檔 hello.txt 並儲存以下文字於工作目錄.
# Papa I love u <-- D:/BeeStation/02_python/250402_mouseMove4/hello.txt

# Step 2: 開請檔案.
p = Path('D:\\BeeStation\\02_python\\250402_mouseMove4')
helloFile = open(p / 'hello.txt')

# Step 3: 讀取檔案
helloContent = helloFile.read()
helloContent # 'Papa I love u.'
