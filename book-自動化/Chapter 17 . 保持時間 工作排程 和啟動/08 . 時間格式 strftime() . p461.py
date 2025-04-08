筆記日期: 2024 年 11 月 5 日 . 16 點 47 分 0 秒 . 星期二

strftime 指令 . 意義
%Y . 年 . 2024
%y . 年 . 24
%m . 月 . 11
%B . 月 . November
%b . 月 . Nov
%d . 日 . 5
%j . 一年的第幾天

%w . 星期 . 2 (0 Sunday ~ 6 Saturday)
%A . 星期 . Tuesday
%a . 星期 . Thu
%H . 時 . 16 (24 小時制)
%I . 時 . 4 (12 小時制)
%M . 分 . 47
%S . 秒 . 00
%p . PM . (AM or PM)
%% . % . 字元


import datetime

nov5st = datetime.datetime(2024, 11, 5, 16, 47, 0)
nov5st.strftime('%Y/%m/%d %H:%M:%S')
輸出: '2024/11/05 16:47:00'

nov5st.strftime('%I:%M %p')
輸出: '04:47 PM'

nov5st.strftime("%B of '%y")
輸出: "November of '24"

# 依格式, 反推時間.
import datetime

datetime.datetime.strptime('November 6, 2024', '%B %d, %Y')
輸出: datetime.datetime(2024, 11, 6, 0, 0)

datetime.datetime.strptime('2024/11/6 8:45:00', '%Y/%m/%d %H:%M:%S')
輸出: datetime.datetime(2024, 11, 6, 8, 45)

datetime.datetime.strptime("November of '24", "%B of '%y")
輸出: datetime.datetime(2024, 11, 1, 0, 0)

datetime.datetime.strptime("November of '63", "%B of '%y")
輸出: datetime.datetime(2063, 11, 1, 0, 0)



