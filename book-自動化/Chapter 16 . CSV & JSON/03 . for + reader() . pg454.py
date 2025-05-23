reader 物件只能迴圈 1 次.
若要在讀取 csv, 則需要呼叫 csv.reader 來建立 reader 物件.

import csv

exampleFile = open('D:\\Dropbox\\12-Office-TryTryLu\\Learning_02_Python\\example.csv')
exampleReader = csv.reader(exampleFile)

for row in exampleReader:
   print('Row #' + str(exampleReader.line_num) + ' ' + str(row))


輸出
Row #1 ['10/16/2024 09:22', 'Apples', '73']
Row #2 ['10/16/2014 11:33', 'Cherries', '85']
Row #3 ['10/17/2024 12:46', 'Pears', '14']
Row #4 ['10/18/2024 8:59', 'Orangers', '52']
Row #5 ['10/20/2024 18:10', 'Bananas', '23']
Row #6 ['10/20/2024 2:40', 'Strawberries', '98']
>>> 
