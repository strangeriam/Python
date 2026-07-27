import os
os.chdir('D:\\Dropbox\\14-Office-TryTryLu\\Python_01_RS232_RebootCycling')

# 寫入新檔
fname = open('hello.log', 'w')
fname.write('this is line 1.\n')
fname.close()

# Append 到下一行
fname = open('hello.log', 'a')
fname.write('this is line 2.')
fname.close()

# 讀取檔案
fname = open('hello.log')
content = fname.read()
fname.close()

print(content)

輸出:
this is line 1.
this is line 2.
