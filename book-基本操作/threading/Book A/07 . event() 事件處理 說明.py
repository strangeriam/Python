# 事件 的方式, 就能讓不同的執行續之間彼此溝通,
# 也能輕鬆做到「等待 A 執行緒完成某件事後, B 執行緒再繼續」的功能.

方法	說明
threading.Event()	註冊一個事件。
set()	觸發事件。
wait()	等待事件被觸發。
clear()	清除事件觸發，事件回到未被觸發的狀態。

