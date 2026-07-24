import datetime
nowDate = datetime.datetime.now().strftime('%Y%m%d')
nowTime = datetime.datetime.now().strftime('%H%M%S')

print('Date: ', nowDate) # Date:  20250408
print('Time: ', nowTime) # Time:  104957

filename = 'report_' + nowTime + '.txt'

print(filename) # report_104957.txt
