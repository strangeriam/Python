
# 切換工作目錄
import os
os.chdir('D:/BeeStation/02_python/coding')

from pathlib import Path
Path('my/relative/path') # WindowsPath('my/relative/path')
Path.cwd() / Path('my/relative/path') # WindowsPath('D:/BeeStation/02_python/coding/my/relative/path')

# 如果相對路徑 在目前工作目錄之外
# 以下是在 家目錄, 不在目前工作目錄.
from pathlib import Path
Path('my/relative/path') # WindowsPath('my/relative/path')
Path.home() / Path('my/relative/path') # WindowsPath('C:/Users/Rlulu/my/relative/path')
