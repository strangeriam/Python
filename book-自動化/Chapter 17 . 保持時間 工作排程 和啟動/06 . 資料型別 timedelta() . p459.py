import datetime

delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
delta.days, delta.seconds, delta.microseconds
輸出: (11, 36548, 0)

delta.total_seconds()
輸出: 986948.0

str(delta)
輸出: '11 days, 10:09:08'

