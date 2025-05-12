# 下方的程式碼註冊了兩個事件.
# event_a 會在輸入任意內容後觸發,
# 觸發後就會印出 1～5 的數字,
# 印出完成後會觸發 event_b,
# 這時才又可以繼續輸入文字,
# 不斷重複兩個事件的觸發與執行續的執行.

# ====================================
import threading, time

def aa():
    i = 0
    while True:
        event_a.wait()        # 等待 event_a 被觸發
        event_a.clear()       # 還原 event_a 狀態
        for i in range(1,6):
            print(i)
            time.sleep(0.5)
        event_b.set()         # 觸發 event_b

def bb():
    while True:
        input('輸入任意內容')
        event_a.set()         # 觸發 event_a
        event_b.wait()        # 等待 event_b 被觸發
        event_b.clear()       # 還原 event_b 狀態

event_a = threading.Event()   # 註冊 event_a
event_b = threading.Event()   # 註冊 event_b
a = threading.Thread(target=aa)
b = threading.Thread(target=bb)

a.start()
b.start()

# 輸出:

輸入任意內容a
1
2
3
4
5
輸入任意內容b
1
2
3
4
5
輸入任意內容
