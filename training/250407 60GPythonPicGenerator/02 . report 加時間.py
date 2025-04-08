import datetime
nowDate = datetime.datetime.now().strftime('%Y%m%d')
nowTime = datetime.datetime.now().strftime('%H%M%S')

print('Date: ', nowDate)
print('Time: ', nowTime)

filename = 'report_', nowTime
