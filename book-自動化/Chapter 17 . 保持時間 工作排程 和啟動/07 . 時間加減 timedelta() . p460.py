
## 計算今天之後第 1000 天的日期為何?
import datetime

dt = datetime.datetime.now()
dt
輸出: datetime.datetime(2024, 11, 5, 14, 35, 21, 715453)

thousanDays = datetime.timedelta(days=1000)
dt + thousanDays
輸出: datetime.datetime(2027, 8, 2, 14, 35, 21, 715453)

# 加減乘除
import datetime

dec31st = datetime.datetime(2024, 11, 5, 14, 40, 0)
aboutThirtyYears = datetime.timedelta(days=365 * 30)

dec31st
輸出: datetime.datetime(2024, 11, 5, 14, 40)

dec31st - aboutThirtyYears
輸出: datetime.datetime(1994, 11, 13, 14, 40)

dec31st - (2 * aboutThirtyYears)
輸出: datetime.datetime(1964, 11, 20, 14, 40)

# 暫停到指定日期
import datetime
import time

halloween2024 = datetime.datetime(2024, 11, 11, 0, 0 ,0)
while datetime.datetime.now() < halloween2024:
  time.sleep(1)

輸出:
直到 2024年11月11日 0時0分0秒 才跳出 while 迴圈.
