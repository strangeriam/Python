# 使用 threading 建立執行緒後,
# 可以使用 Lock() 方法建立一個執行緒的 '鎖',
# 當 Lock 建立後, 就能使用 acquire() 方法鎖定,
# 使用 release() 方法解除鎖定, 
# 如果有多個執行緒共用同一個 Lock, 則同一時間只會執行第一個鎖定的執行緒,
# 其他的執行緒要等到解鎖才能夠執行.

# 以下方的程式碼為例,
# 會先使用 threading.Lock() 建立一個 Lock,
# 當 aa() 和 bb() 執行時會先使用 lock.acquire() 進行鎖定 ( 以執行的順序表示誰先鎖定 ),
# 因為 aa() 比較先執行所以會先鎖定,
# 接著當 aa() 裡的 i 等於 2 時使用 lock.release() 解除鎖定,
# 這時 bb() 就可以開始執行.

# =================================
import threading
import time

def aa():
    lock.acquire() # 鎖定
    i = 0
    while i<5:
        i = i + 1
        time.sleep(0.5)
        print('A:', i)
        if i==2:
            lock.release() # i 等於 2 時解除鎖定

def bb():
    lock.acquire() # 鎖定
    i = 0
    while i<50:
        i = i + 10
        time.sleep(0.5)
        print('B:', i)
    lock.release()

lock = threading.Lock() # 建立 Lock
a = threading.Thread(target=aa)
b = threading.Thread(target=bb)

a.start()
b.start()

# 輸出:
A: 1
A: 2
B: A: 310

B: 20
A: 4
B: 30
A: 5
B: 40
B: 50
[Finished in 3.6s]

