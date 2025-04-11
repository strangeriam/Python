# 切換工作目錄
import os
os.chdir('D:\\BeeStation\\02_python\\coding')

# =================================
# 寫入新檔
baconFile = open('bacon.txt', 'w')
baconFile.write('Hello world!\n') # 13
baconFile.close()

# 遞增文字至下一行
baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable.') # 25
baconFile.close()

# 讀取檔案
baconFile = open('bacon.txt')
content = baconFile.read()
baconFile.close()

print(content)

# OUTPUT:
Hello world!
Bacon is not a vegetable.
