
# common.py
def f_new_picture():
	from pathlib import Path
	import os, datetime

	nowDate = datetime.datetime.now().strftime('%Y%m%d')
	nowTime = datetime.datetime.now().strftime('%H%M%S')

	p = Path(Path.cwd(), 'result' + '\\' + nowDate)

	if p.is_dir():
	  	print('Debug: directory exists')
	else:
		print('Debug: no directory')
		os.makedirs(p)

	fname = 'report_' + nowTime + '.png'
	pf = Path(Path.cwd(), 'result' + '\\' + nowDate + '\\' + fname)

	return pf


# go.py
from common import f_new_picture
fname = f_new_picture()
print('Debug-Lu: fname is', fname)

