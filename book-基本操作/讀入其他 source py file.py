
# common.py (跟 main.py 在同一層)
import sys, time, datetime

def f_timeNow():
	dt = datetime.datetime.now()
	return dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second

def f_normal():
	nowTime = f_timeNow()
	print('click normal .. ', nowTime)

def f_active():
	nowTime = f_timeNow()
	print("click active .. ", nowTime)

def f_exit():
	nowTime = f_timeNow()
	print("click exit .. ", nowTime)
	time.sleep(1)
	sys.exit()


# main.py
import sys, time, datetime, pyautogui

from common import f_timeNow
from common import f_normal
from common import f_active
from common import f_exit

programSize = '600x400'

screenWidth = pyautogui.size()[0]
screenHeight = pyautogui.size()[1]
screenSize = screenWidth, 'x', screenHeight
print(screenSize)

root = tk.Tk()
root.geometry( programSize )

....
