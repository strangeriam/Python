# 清除 shell
import os
os.system('cls||clear')

# 實作前, 切換工作路徑.
import os
os.chdir('D:\\BeeStation\\02_python\\coding')

# 查看目前工作目錄
from pathlib import Path
Path.cwd()

# =================================
import pprint

cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
pprint.pformat(cats) # "[{'desc': 'chubby', 'name': 'Zophie'}, {'desc': 'fluffy', 'name': 'Pooka'}]"
fileObj = open('myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n') # 83
fileObj.close()

# =================================
import myCats

myCats.cats # [{'desc': 'chubby', 'name': 'Zophie'}, {'desc': 'fluffy', 'name': 'Pooka'}]
myCats.cats[0] # {'desc': 'chubby', 'name': 'Zophie'}
myCats.cats[0]['name'] # 'Zophie'
