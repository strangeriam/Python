import datetime

today = datetime.date.today()
print(today)                 # 回傳目前的西元年、月、日
print(today.year)            # 取得西元年
print(today.month)           # 取得月份
print(today.day)             # 取得日期
print(replace(year=2020))    # 取代日期，產生新的物件
print(today.weekday())       # 回傳一星期中的第幾天，星期一為 0
print(today.isoweekday())    # 回傳一星期中的第幾天，星期一為 1
print(today.isocalendar())   # (2021, 42, 2)  ( 第三個數字是星期二，所以是 2 ) 回傳一個 tuple，內容分別是 ( 年、第幾週、isoweekday )
print(today.isoformat())     # 2021-10-19 . 回傳 ISO 格式的日期字串
print(today.ctime())         # Tue Oct 19 00:00:00 2021 . 回傳日期和時間的字串
print(today.strftime('%Y.%m.%d'))   # 2021.10.19 . 回傳特定格式字串所表示的時間


# 下方的程式執行後，會利用「.days」的屬性，計算出兩個日期差了幾天。
import datetime
d1 = datetime.date(2020, 6, 24)
d2 = datetime.date(2021, 11, 24)
print(abs(d1-d2).days)       # 518
