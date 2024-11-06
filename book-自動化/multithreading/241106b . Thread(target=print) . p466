## 呼叫 threadObj.start() 時會建立一個新的 執行緒 來執行 print() 函式.
## 它會傳入 'Cats', 'Dogs' & 'Frogs' 作為引數, 以及 '&' 作為 sep 關鍵字引數.

import threading
threadObj = threading.Thread(target=print, args=['Cats', 'Dogs', 'Frogs'], kwargs={'sep': ' & '})
threadObj.start()

輸出: Cats & Dogs & Frogs
