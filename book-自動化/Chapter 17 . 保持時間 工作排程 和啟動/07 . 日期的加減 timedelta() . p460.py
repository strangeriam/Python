
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
