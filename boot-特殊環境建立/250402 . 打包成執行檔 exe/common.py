import sys, time, datetime

def f_timeNow():
	dt = datetime.datetime.now()
	return dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second

def f_normal():
	nowTime = f_timeNow()
	print('click normal .. ', nowTime)

def f_trytrylu():
	nowTime = f_timeNow()
	print("click trytryLu .. ", nowTime)

def f_exit():
	nowTime = f_timeNow()
	print("click exit .. ", nowTime)
	time.sleep(1)
	sys.exit()

def f_mouse_move():
	import pyautogui

	nowTime = f_timeNow()
	print("click summit .. ", nowTime)

	pyautogui.click(1000, 1000, button='left', duration=0.25, clicks=2, interval=1)
	print('read position .. ', pyautogui.position())

def f_read_screen_size():
	import pyautogui

	screenWidth = pyautogui.size()[0]
	screenHeight = pyautogui.size()[1]
	screenSize = screenWidth, 'x', screenHeight

	return screenSize

def f_readini_flow1_x():
	import configparser

	config = configparser.ConfigParser()
	config.read('MainConfig.ini', encoding='utf-8')
	x = config['MOUSE']['flow_1_x']
	return x

def f_readini_flow2_x():
	import configparser

	config = configparser.ConfigParser()
	config.read('MainConfig.ini', encoding='utf-8')
	x = config['MOUSE']['flow_2_x']
	return x

def f_readini_flow3_x():
	import configparser

	config = configparser.ConfigParser()
	config.read('MainConfig.ini', encoding='utf-8')
	x = config['MOUSE']['flow_3_x']
	return x

def f_readini_flow1_y():
	import configparser

	config = configparser.ConfigParser()
	config.read('MainConfig.ini', encoding='utf-8')
	y = config['MOUSE']['flow_1_y']
	return y

def f_readini_flow2_y():
	import configparser

	config = configparser.ConfigParser()
	config.read('MainConfig.ini', encoding='utf-8')
	y = config['MOUSE']['flow_2_y']
	return y

def f_readini_flow3_y():
	import configparser

	config = configparser.ConfigParser()
	config.read('MainConfig.ini', encoding='utf-8')
	y = config['MOUSE']['flow_3_y']
	return y

def f_readini_ui_size():
	import configparser

	config = configparser.ConfigParser()
	config.read('MainConfig.ini', encoding='utf-8')
	ui_size = config['UI']['ui_size']
	return ui_size

def f_color(value):
    color01 = '#545454' # Gray deep1
    color02 = '#E6E6E6'
    color03 = '#CCCCCC'
    color04 = '#000000'
    color05 = '#33CC33'
    color06 = '#DD5555'
    color07 = '#F26521' # Origin
    color08 = '#C4DF9B' # Green
    color09 = '#F5989D' # Red
    color10 = '#F0F0F0' # Gray 灰黑色

    if value == 1:
    	color = color01
    elif value == 2:
    	color = color02
    elif value == 3:
    	color = color03
    elif value == 4:
    	color = color04
    elif value == 5:
    	color = color05
    elif value == 6:
    	color = color06
    elif value == 7:
    	color = color07
    elif value == 8:
    	color = color08
    elif value == 9:
    	color = color09
    elif value == 10:
    	color = color10
    else:
    	color == null

    return color

