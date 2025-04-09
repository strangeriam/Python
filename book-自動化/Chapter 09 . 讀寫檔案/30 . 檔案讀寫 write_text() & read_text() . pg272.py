
## 切換工作目錄
import os
os.chdir('D:\BeeStation\02_python\250402_mouseMove4\')

# Beginning
from pathlib import Path

newP = Path('C:\\Users\\Rlulu\\Dropbox\\12-Office-TryTryLu\\Learning_02_Python\\newDir1.txt')
newP.write_text('Hello, World')
輸出:
12

newP.read_text()
輸出:
'Hello, World'
