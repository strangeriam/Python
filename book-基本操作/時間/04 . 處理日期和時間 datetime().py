# year、month、dayhour、minute、second、microsecond 和 tzinfo

import datetime
thisTime = datetime.datetime(2020,1,1,20,20,20,20)
print(thisTime)    # 2020-01-01 20:20:20.000020

# 主要的方法
today()	回傳目前的日期與時間
now()	回傳目前的日期與時間，可加入 tz 參數設定時區
utcnow()	回傳目前的日期與時間

import datetime
print(datetime.datetime.today())     # 2025-04-08 09:45:17.886388
print(datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8)))) # 2025-04-08 09:45:52.077623+08:00
print(datetime.datetime.utcnow())   # 2025-04-08 01:46:12.785093

# 使用 datetime.datetime 將字串轉換為日期時間物件後，就能透過下面幾種常用的方法，將取出的日期時間資訊進行下一步操作。
year	取得西元年
month	取得月份
day	取得日期
hour	取得小時
minute	取得分鐘
second	取得秒數
microsecond	取得微秒數 (1/1000000 秒)
weekday()	回傳一星期中的第幾天，星期一為 0
isoweekday()	回傳一星期中的第幾天，星期一為 1
isocalendar()	回傳一個 tuple，內容分別是 ( 年、第幾週、isoweekday )
isoformat()	回傳 ISO 格式的日期字串
ctime()	回傳日期和時間的字串
timetuple()	回傳日期與時間所組成的 time.struct_time 物件
strftime()	回傳特定格式字串所表示的時間 ( 詳細可參考 strftime() 和 strptime() )

import datetime
now = datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8)))
print(now)                # 2021-10-19 14:25:46.962975+08:00
print(now.date())         # 2021-10-19
print(now.time())         # 14:25:46.962975
print(now.tzname())       # UTC+08:00
print(now.weekday())      # 1
print(now.isoweekday())   # 2
print(now.isocalendar())  # (2021, 42, 2)
print(now.isoformat())    # 2021-10-19 14:25:46.962975+08:00
print(now.ctime())        # Tue Oct 19 14:48:38 2021
print(now.strftime('%Y/%m/%d %H:%M:%S'))  # 2021/10/19 14:48:38
print(now.timetuple())    # time.struct_time(tm_year=2021, tm_mon=10, tm_mday=19, tm_hour=16, tm_min=8, tm_sec=6, tm_wday=1, tm_yday=292, tm_isdst=-1)

