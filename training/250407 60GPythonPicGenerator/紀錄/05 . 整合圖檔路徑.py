
# common
def f_establish_directory():
	from pathlib import Path
	import os, datetime

	d = datetime.datetime.now().strftime('%Y%m%d')
	p = Path(Path.cwd(), 'result' + '\\' + d)
	# print('Lu-250410:', p)

	if p.is_dir() == False:
		print('Lu-250409: establish directory.')
		os.makedirs(p)

	return p

def f_get_clock():
	import os, datetime
	t = datetime.datetime.now().strftime('%H%M%S')
	return t

# go.py
from common import f_establish_directory
from common import f_get_clock
from pathlib import Path

worktmp = f_establish_directory()
nowTime = f_get_clock()
theta = 'AAA'

fname = 'report_' + str(theta) + '_' + nowTime + '.png'

print('worktmp:',worktmp )
print('fname:', fname )

pfile = Path(str(worktmp) + '\\' + fname)
print('pfile:', pfile )
