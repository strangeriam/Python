# 下方的程式碼執行後, 會註冊一個 event 事件,
# 當 aa() 執行時使用 event.wait() 等待事件被觸發,
# 接著設定 bb() 執行到 i 等於 30 的時候就會觸發事件,
# 這時 aa() 才會開始運作.

import threading, time

def aa():
    event.wait() # 等待事件被觸發
    event.clear() # 觸發後將事件回歸原本狀態
    for i in range(1,6):
        print('A:',i)
        time.sleep(0.5)

def bb():
    for i in range(10,60,10):
        if i == 30:
            event.set() # 觸發事件
        print('B:',i)
        time.sleep(0.5)

event = threading.Event() # 註冊事件
a = threading.Thread(target=aa)
b = threading.Thread(target=bb)

a.start()
b.start()

# 輸出:

B: 10
B: 20
B:A: 30
 1
A:B: 40
 2
A:B:  50
3
A: 4
A: 5
[Finished in 3.6s]
