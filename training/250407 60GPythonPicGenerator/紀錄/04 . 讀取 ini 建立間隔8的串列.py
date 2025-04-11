
# common.py
def f_getIni_targetTheta():
	from pathlib import Path
	import configparser

	cfg = configparser.ConfigParser()
	cfg.read(Path(Path.cwd(), 'config.ini', encoding='utf-8'))

	n1 = int(cfg['PARAMETER']['TARGET_THETA'])
	n2 = int(cfg['PARAMETER']['THETA_INTERVAL'])
	# print('n1: ', n1, ' . ', 'n2: ', n2)

	nStart = int(-n1)
	nEnd = int(n1) + int(n2)

	nList = []
	for i in range(nStart, nEnd, n2):
		nList.append(i)

	# print('nList: ', nList)

	return nList

# go.py
from common import f_getIni_targetTheta

get_ini = f_getIni_targetTheta()
print(get_ini)

