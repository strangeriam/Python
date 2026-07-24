# 切換工作路徑
import os
os.chdir('D:\\BeeStation\\03_python_project\\250414_mouseScreenControl\\Material')

# 檢查工作路徑
from pathlib import Path
p = Path.cwd()

print(p) # D:\BeeStation\03_python_project\250414_mouseScreenControl\Material
