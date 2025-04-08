
# common.py
def f_new_dirName():
	from pathlib import Path
	import os, datetime

	nowDate = datetime.datetime.now().strftime('%Y%m%d')
	nowTime = datetime.datetime.now().strftime('%H%M%S')

	resultPath = Path(Path.cwd(), 'result' + '\\' + nowDate)
	os.makedirs(resultPath)

	return resultPath


# go.py
from common import f_new_dirName

var = f_new_dirName()
print( 'Return: ', var )
