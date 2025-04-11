# shelve 擱置

# 實作前, 切換工作路徑.
import os
os.chdir('D:\\BeeStation\\02_python\\coding')

# 查看目前工作目錄
from pathlib import Path
Path.cwd()

# =================================
import shelve

shelfFile = shelve.open('mydata') # 新產生檔案 mydata.dat
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats # 新產生檔案 mydata.dir
shelfFile.close() # 新產生檔案 mydata.bak
