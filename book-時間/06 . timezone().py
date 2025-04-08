datetime.timezone 負責時區的轉換，主要和 datetime.datetime、datetime.time 互相搭配使用。

datetime.timedelta 裡 hours 的數值，可以參考：時區列表，台灣處在 GMT+8 的時區，所以 hours 等於 8，如果是日本，因為是 GTM+9，hours 就要設定為 9。

import datetime
tzone = datetime.timezone(datetime.timedelta(hours=8))
now = datetime.datetime.now(tz=tzone)
print(now)    # 2021-10-19 15:07:51.128092+08:00
