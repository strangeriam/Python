
# common.py
def f_new_dirName():
	from pathlib import Path
	import os, datetime

	nowDate = datetime.datetime.now().strftime('%Y%m%d')
	nowTime = datetime.datetime.now().strftime('%H%M%S')

	worktmp = Path.cwd()
	resultPath = 'result' + '\\' + nowDate
	print(Path(worktmp, resultPath))
	os.makedirs(Path(worktmp, resultPath))


# go.py
from common import f_new_dirName

f_new_dirName()
