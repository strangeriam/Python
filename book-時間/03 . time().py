datetime.time 可以處理時間相關的操作，本身包含下列幾個屬性：hour、minute、second、microsecond 和 tzinfo，分別用逗號區隔，下方的程式會印出指定的時間。

import datetime
thisTime = datetime.time(12,0,0,1)
print(thisTime)   # 12:00:00.000001
tzinfo 是時區的選項，預設 None 採用 UTC 時區，如果要轉換成台灣 UTC+8 的時區可採用下方的寫法：

import datetime
thisTime = datetime.time(14,0,0,1,tzinfo=datetime.timezone(datetime.timedelta(hours=8)))
print(thisTime)    # 14:00:00.000001+08:00
使用 datetime.time 將字串轉換為時間物件後，就能透過下面幾種常用的方法，取出時間的資訊進行下一步操作。

方法	說明
hour	取得小時
minute	取得分鐘
second	取得秒數
microsecond	取得微秒數 (1/1000000 秒)
replace()	取代時間，產生新的物件
isoformat()	回傳 ISO 格式的時間字串
tzname()	回傳目前時區資訊
strftime()	回傳特定格式字串所表示的時間 ( 詳細可參考 strftime() 和 strptime() )

import datetime
thisTime = datetime.time(14,0,0,1,tzinfo=datetime.timezone(datetime.timedelta(hours=8)))
print(thisTime)               # 14:00:00.000001+08:00
print(thisTime.isoformat())   # 14:00:00.000001+08:00
print(thisTime.tzname())      # UTC+08:00
print( thisTime.strftime('%H:%M:%S'))   # 14:00:00

newTime = today.replace(hour=20)
print(newTime)                # 20:00:00.000001+08:00
