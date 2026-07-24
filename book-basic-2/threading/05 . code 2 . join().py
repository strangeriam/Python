# 如果只加入 a.join() 而不加入 b.join(), 則 cc() 會在 aa() 執行結束就開始.

import threading, time

def aa():
    i = 0
    while i<5:
        i = i + 1
        time.sleep(0.5)
        print('A:', i)

def bb():
    i = 0
    while i<100:
        i = i + 10
        time.sleep(0.5)
        print('B:', i)

def cc():
    i = 0
    while i<500:
        i = i + 100
        time.sleep(0.5)
        print('C:', i)

a = threading.Thread(target=aa)
b = threading.Thread(target=bb)
c = threading.Thread(target=cc)

a.start()
b.start()
a.join()   # 加入等待 aa() 完成的方法
c.start()  # 當 aa() 完成後，就會開始執行 cc()

# 輸出:

A: 1
B: 10
A: 2
B: 20
A: 3B:
 30
B: 40
A: 4
B: 50
A: 5
B: 60
C: 100
B: 70
C: 200
B: 80
C: 300
B: 90
C: 400
B: 100
C: 500
[Finished in 5.1s]
