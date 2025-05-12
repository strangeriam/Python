# 將 aa(), bb() & cc() 三個函式分別建立為執行緒,
# 接著當使用 a.start() 和 b.start() 方法啟用後,
# 因為有加入 a.join() 和 b.join() 的等待方法
# 所以 c.start() 會在 aa() 與 bb() 執行完成後,才會啟用.

import threading, time

def aa():
    i = 0
    while i<5:
        i = i + 1
        time.sleep(0.5)
        print('A:', i)

def bb():
    i = 0
    while i<50:
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
b.join()   # 加入等待 bb() 完成的方法
c.start()  # 當 aa() 與 bb() 都完成後，才會開始執行 cc()


# 輸出:

A: B: 10
1
B: 20
A: 2
A:B: 30
 3
A:B: 40
 4
B: 50
A: 5
C: 100
C: 200
C: 300
C: 400
C: 500
[Finished in 5.1s]
