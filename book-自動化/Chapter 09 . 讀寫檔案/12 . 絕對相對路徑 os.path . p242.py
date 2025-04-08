import os

os.path.abspath('.') # 'C:\\Users\\Rlulu\\AppData\\Local\\Programs\\Python\\Python311'

os.path.abspath('.\\Scripts') # 'C:\\Users\\Rlulu\\AppData\\Local\\Programs\\Python\\Python311\\Scripts'

os.path.isabs('.') # False

# 由於 os.path.abspath() 時,
# C:\Users\Rlulu\AppData\Local\Programs\Python\Python311 是工作目錄,
# 因此 點 (.) 資料夾所代表的是 絕對路徑 'C:\\Users\\Rlulu\\AppData\\Local\\Programs\\Python\\Python311'
os.path.isabs(os.path.abspath('.')) # True

os.path.relpath('C:\\Windows', 'C:\\') # 'Windows'

os.path.relpath('C:\\Windows', 'C:\\spam\\eggs') # '..\\..\\Windows'
