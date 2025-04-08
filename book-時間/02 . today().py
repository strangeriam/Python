
# 方法	說明
# today()	回傳目前的西元年、月、日

import datetime
today = datetime.date.today()
print(today)

# 取得日期後, 可以使用下面幾種常用的方法, 進一步取出日期的資訊進行操作.
# 方法	說明
# year	取得西元年
# month	取得月份
# day	取得日期
# replace()	取代日期，產生新的物件
# weekday()	回傳一星期中的第幾天，星期一為 0
# isoweekday()	回傳一星期中的第幾天，星期一為 1
# isocalendar()	回傳一個 tuple，內容分別是 ( 年、第幾週、isoweekday )
# isoformat()	回傳 ISO 格式的日期字串
# ctime()	回傳日期和時間的字串
# strftime()	回傳特定格式字串所表示的時間 ( 詳細可參考 strftime() 和 strptime() )
import datetime
today = datetime.date.today()
print(today)                 # 2021-10-19
print(today.year)            # 2021
print(today.month)           # 10
print(today.day)             # 19
print(today.weekday())       # 1    ( 因為是星期二，所以是 1 )
print(today.isoweekday())    # 2    ( 因為是星期二，所以是 2 )
print(today.isocalendar())   # (2021, 42, 2)  ( 第三個數字是星期二，所以是 2 )
print(today.isoformat())     # 2021-10-19
print(today.ctime())         # Tue Oct 19 00:00:00 2021
print(today.strftime('%Y.%m.%d'))    # 2021.10.19

newDay = today.replace(year=2020)
print(newDay)                # 2020-10-19

# 下方的程式執行後，會利用「.days」的屬性，計算出兩個日期差了幾天。
import datetime
d1 = datetime.date(2020, 6, 24)
d2 = datetime.date(2021, 11, 24)
print(abs(d1-d2).days)       # 518
