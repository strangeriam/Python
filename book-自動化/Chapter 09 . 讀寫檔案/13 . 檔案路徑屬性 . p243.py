
# 實作前, 切換工作路徑.
import os
os.chdir('D:\\BeeStation\\02_python\\coding')

from pathlib import Path
p = Path('D:/BeeStation/02_python/coding/spam.txt')
p.anchor # 'D:\\'
p.parent # WindowsPath('D:/BeeStation/02_python/coding')
p.name # 'spam.txt'
p.stem # 'spam' --> 基本名稱
p.suffix # '.txt' --> 副檔名
p.drive # 'D:' --> 實體儲存裝置
