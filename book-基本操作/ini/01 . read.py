## filename: setup.ini
## example content

[CFG]
MODEL=EAP111
SOURCE_FILE=Log_all_simple.csv

## ======================================
ENVPATH = 'D:/Dropbox/12-Office-Sync-MTS/33_ReportGenerator/021_RF_IQ_V7_Py/'

import configparser

# 建立物件 configparser 
config = configparser.ConfigParser()


# 讀取 ini 檔
config.read(ENVPATH + 'setup.ini', encoding='utf-8')

# 獲取 SOURCE_FILE 中 Log_all_simple.csv
modelname = config['CFG']['MODEL']
filename = config['CFG']['SOURCE_FILE']

print('Model name is ' + modelname + ' and ' + 'Filename is ' + filename)
輸出:
Model name is EAP111 and Filename is Log_all_simple.csv
