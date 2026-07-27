# 查看目前工作目錄
from pathlib import Path
Path.cwd()

輸出:
WindowsPath('C:/Users/Rlulu/AppData/Local/Programs/Python/Python311')

p = Path('spam.txt')
p.write_text('Hello, World') # 12

p.read_text() # 'Hello, World'
