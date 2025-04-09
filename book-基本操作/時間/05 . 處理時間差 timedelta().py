如果要進行日期或時間的計算，可以透過 datetime.timedelta 增加或減少日期或時間，本身包含 days、seconds、microseconds、milliseconds、minutes、hours、weeks 的屬性，屬性的預設值都是 0。

使用 datetime.timedelta 只需要將其放在日期或時間物件後方，就回傳計算後的時間，下方的程式會計算出昨天、明天、下星期同一天的日期。


import datetime
today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)
nextweek = today + datetime.timedelta(weeks=1)
print(today)       # 2021-10-19 07:01:22.669886
print(yesterday)   # 2021-10-18 07:01:22.669886
print(tomorrow)    # 2021-10-20 07:01:22.669886
print(nextweek)    # 2021-10-26 07:01:22.669886
