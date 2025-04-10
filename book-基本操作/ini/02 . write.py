## filename: setup.ini

[CFG]
MODEL=EAP111
SOURCE_FILE=Log_all_simple.csv

## ======================================
from pathlib import Path
import configparser

# 建立物件 configparser
config = configparser.ConfigParser()

ENVPATH = 'D:/Dropbox/12-Office-Sync-MTS/33_ReportGenerator/021_RF_IQ_V7_Py/'
inifile = Path(ENVPATH + 'setup.ini')

# Updating existing entry. (Item 會被轉換成小寫.)
config.read(inifile)
config.set('CFG', 'MODEL','EAP999')
config.write(inifile.open("w"))


輸出
## ======================================
[CFG]
model = EAP999
source_file = Log_all_simple.csv

