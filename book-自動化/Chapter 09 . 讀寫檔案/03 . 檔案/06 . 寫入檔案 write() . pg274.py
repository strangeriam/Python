# 切換工作目錄
import os
os.chdir('D:\\BeeStation\\02_python\\coding')

# Coding now
baconFile = open('bacon.txt', 'w')
baconFile.write('Hello world!\n') # 13
baconFile.close()

baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable.') # 25
baconFile.close()

baconFile = open('bacon.txt')
content = baconFile.read()
baconFile.close()

print(content)

# OUTPUT:
Hello world!
Bacon is not a vegetable.
