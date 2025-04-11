
def f_new_picture():
	from pathlib import Path
	import os, datetime, configparser

	nowDate = datetime.datetime.now().strftime('%Y%m%d')
	nowTime = datetime.datetime.now().strftime('%H%M%S')

	p = Path(Path.cwd(), 'result' + '\\' + nowDate)

	if p.is_dir():
	  	print('Lu-250409: directory exists')
	else:
		# print('Lu-250409: no directory')
		os.makedirs(p)

	fname = 'report_' + nowTime + '.png'
	pfile = Path(Path.cwd(), 'result' + '\\' + nowDate + '\\' + fname)

	return pfile

#; ..........................................
#; THETA_TARGET= 48  . 角度測試範圍 -48 ~ 48
#; THETA_INTERVAL= 8 . 角度間隔 8 (-48 -40 -32 -24 -16 -8 0 8 16 24 32 40 48)
#;
#; THETA_X1_SWITCH . 單一角度模擬開關
#; 		0 . 模擬範圍, 例: 範圍 -48 ~ 48
#; 		1 . 模擬一組, 例: 只有角度 48
#; ..........................................
def f_getIni_targetTheta():
	from pathlib import Path
	import configparser

	cfg = configparser.ConfigParser()
	cfg.read(Path(Path.cwd(), 'config.ini', encoding='utf-8'))

	multi = int(cfg['PARAMETER']['THETA_MULTI'])

	n1 = int(cfg['PARAMETER']['THETA_TARGET'])
	n2 = int(cfg['PARAMETER']['THETA_INTERVAL'])
	# print('multi:', multi, '.', 'n1: ', n1, ' . ', 'n2: ', n2)

	if multi == 1:
		nStart = int(-n1)
	else:
		nStart = int(n1)

	nEnd = int(n1) + int(n2)

	nList = []
	for i in range(nStart, nEnd, n2):
		nList.append(i)

	# print('nList: ', nList)

	return nList

def f_establish_directory():
	from pathlib import Path
	import os, datetime

	d = datetime.datetime.now().strftime('%Y%m%d')
	p = Path(Path.cwd(), 'result' + '\\' + d)
	# print('Lu-250410:', p)

	if p.is_dir() == False:
		# print('Lu-250409: establish directory.')
		os.makedirs(p)

	return p

def f_get_clock():
	import os, datetime
	t = datetime.datetime.now().strftime('%H%M%S')
	return t


def f_remove_report():
	from pathlib import Path
	import shutil, os, configparser

	cfg = configparser.ConfigParser()
	cfg.read(Path(Path.cwd(), 'config.ini', encoding='utf-8'))

	rm = int(cfg['PARAMETER']['REMOVE_OLD_REPORT'])

	if rm == 1:
		p = Path(Path.cwd(), 'result')

		if p.is_dir() == True:
			shutil.rmtree(p)


def f_speed_up():
	from pathlib import Path
	import configparser

	cfg = configparser.ConfigParser()
	cfg.read(Path(Path.cwd(), 'config.ini', encoding='utf-8'))

	speedup = int(cfg['PARAMETER']['SPEED_UP'])
	return speedup