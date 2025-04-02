
import tkinter as tk
from tkinter import ttk

import time

from common import f_normal
from common import f_trytrylu
from common import f_exit
from common import f_mouse_move
from common import f_read_screen_size
from common import f_readini_ui_size

from common import f_readini_flow1_x
from common import f_readini_flow2_x
from common import f_readini_flow3_x

from common import f_readini_flow1_y
from common import f_readini_flow2_y
from common import f_readini_flow3_y

from common import f_color

screenSize = f_read_screen_size()
programSize = f_readini_ui_size()

flow1_x = int(f_readini_flow1_x())
flow2_x = int(f_readini_flow2_x())
flow3_x = int(f_readini_flow3_x())

flow1_y = int(f_readini_flow1_y())
flow2_y = int(f_readini_flow2_y())
flow3_y = int(f_readini_flow3_y())

# print('flow1_x: ', flow1_x)
# print('flow1_y: ', flow1_y)

version = 'v250402'
program_title = 'AUTO UI Control . by Lu', version

def f_mouse_move_click(x, y):
	import pyautogui, datetime
	from common import f_timeNow

	varX = int(x)
	varY = int(y)

	nowTime = f_timeNow()
	print('click summit X & Y .. ', varX, ':', varY, ':', nowTime)

	pyautogui.click(varX, varY, button='left', duration=0.25)
	print('read position .. ', pyautogui.position())

def f_mouse_summit_1():
	x = var_flow1_x.get()
	y = var_flow1_y.get()

	if len(x) == 0:
		print('x1: Empty')
		return

	if len(y) == 0:
		print('y1: Empty')
		return

	print('x1:y1 ', x, ':', y)
	f_mouse_move_click(x, y)

def f_mouse_summit_2():
	x = var_flow2_x.get()
	y = var_flow2_y.get()

	if len(x) == 0:
		print('x2: Empty')
		return

	if len(y) == 0:
		print('y2: Empty')
		return

	print('x2:y2 ', x, ':', y)
	f_mouse_move_click(x, y)

def f_mouse_summit_3():
	x = var_flow3_x.get()
	y = var_flow3_y.get()

	if len(x) == 0:
		print('x3: Empty')
		return

	if len(y) == 0:
		print('y3: Empty')
		return

	print('x3:y3 ', x, ':', y)
	f_mouse_move_click(x, y)

def f_mouse_go():
	x1 = var_flow1_x.get()
	y1 = var_flow1_y.get()

	if len(x1) == 0:
		print('x1: Empty')
		return

	if len(y1) == 0:
		print('y1: Empty')
		return

	print('x1:y1 ', x1, ':', y1)
	f_mouse_move_click(x1, y1)

	time.sleep(2)
	x2 = var_flow2_x.get()
	y2 = var_flow2_y.get()

	if len(x2) == 0:
		print('x2: Empty')
		return

	if len(y2) == 0:
		print('y2: Empty')
		return

	print('x2:y2 ', x2, ':', y2)
	f_mouse_move_click(x2, y2)

	time.sleep(2)
	x3 = var_flow3_x.get()
	y3 = var_flow3_y.get()

	if len(x3) == 0:
		print('x3: Empty')
		return

	if len(y3) == 0:
		print('y3: Empty')
		return

	print('x3:y3 ', x3, ':', y3)
	f_mouse_move_click(x3, y3)

# Clear flow 1 Entry
# 刪除開頭與結尾索引之間的 (全部) 內容
def f_clear_flow1x_entry(event):
    entry_flow1_x.delete(0, tk.END)

def f_clear_flow1y_entry(event):
    entry_flow1_y.delete(0, tk.END)

def f_clear_flow2x_entry(event):
    entry_flow2_x.delete(0, tk.END)

def f_clear_flow2y_entry(event):
    entry_flow2_y.delete(0, tk.END)

def f_clear_flow3x_entry(event):
    entry_flow3_x.delete(0, tk.END)

def f_clear_flow3y_entry(event):
    entry_flow3_y.delete(0, tk.END)


root = tk.Tk()
root.resizable(False, False)  			;# Fixed UI size
root.title(program_title) 				;# UI Title text
root.geometry( programSize )			;# Define UI size

# ==================================================
f1_info = ttk.Frame(root)
f2_plan = ttk.Frame(root)
f3_nor_act = ttk.Frame(root)
f4_exit = ttk.Frame(root)

f1_info.pack(side="left", fill="both", expand=True)
f2_plan.pack(side="left", fill="both", expand=True)
f3_nor_act.pack(side="left", fill="both", expand=True)
f4_exit.pack(side="left", fill="both", expand=True)

lbl_1 = ttk.Label(f1_info, text='f1_info')
lbl_2 = ttk.Label(f2_plan, text='f2_plan')
lbl_3 = ttk.Label(f3_nor_act, text='f3_nor_act')
lbl_4 = ttk.Label(f4_exit, text='f4_exit')

# lbl_1.pack(side='top')
# lbl_2.pack(side='top')
# lbl_3.pack(side='top')
# lbl_4.pack(side='top')

# f1_info =======================
f1_top = ttk.Frame(f1_info)
f1_top.pack(side='top', ipadx=10, ipady=30)

f1_mid = ttk.Frame(f1_info)
f1_mid.pack(side='top', ipadx=10, ipady=30)

f1_btm = ttk.Frame(f1_info)
f1_btm.pack(side='top', ipadx=10, ipady=10)

lbl_title1 = ttk.Label(f1_top, text='- INFORMATION -')
lbl_title1.pack(side='top')

# Information =======================
f1_resolution = ttk.Frame(f1_top)
f1_uisize = ttk.Frame(f1_top)
f1_resolution.pack(side='top')
f1_uisize.pack(side='top')

lbl_info1a = ttk.Label(f1_resolution, text='Screen Resolution: ').pack(side='left', ipadx=5, ipady=5)
lbl_info2b = ttk.Label(f1_resolution, text=screenSize).pack(side='right')

lbl_info2a = ttk.Label(f1_uisize, text='Program UI Size: ').pack(side='left', ipadx=5, ipady=5)
lbl_info1b = ttk.Label(f1_uisize, text=programSize).pack(side='right')

# frame 2 . label . Mouse Plan =======================
lbl_mousePlan = ttk.Label(f2_plan, text='- Mouse Plan -')
lbl_mousePlan.pack(side='top')

# ================================================
# frame 2 . frame . flow 1 =======================
f2_fflow1 = ttk.Frame(f2_plan)
f2_fflow1.pack(side='top')

lbl_fflow1 = ttk.Label(f2_fflow1, text='flow 1, X : Y ')
lbl_fflow1.pack(side='left')

var_flow1_x = tk.StringVar()

# state=tk.NORMAL (預設: NORMAL 可用. DISABLED 不可用. )

entry_flow1_x = tk.Entry(f2_fflow1, textvariable=var_flow1_x, fg=f_color(1), bg=f_color(8), font=('Algerian','12','bold'), width=5, state=tk.NORMAL)
entry_flow1_x.insert(0, flow1_x)
entry_flow1_x.bind('<Button-1>', f_clear_flow1x_entry)
entry_flow1_x.pack(side="left")
entry_flow1_x.focus()

lbl_fflow1_colon = ttk.Label(f2_fflow1, text=' : ')
lbl_fflow1_colon.pack(side='left')

var_flow1_y = tk.StringVar()

# entry_flow1_y = ttk.Entry(f2_fflow1, width=5, textvariable=var_flow1_y)
entry_flow1_y = tk.Entry(f2_fflow1, textvariable=var_flow1_y, fg=f_color(1), bg=f_color(8), font=('Algerian','12','bold'), width=5, state=tk.NORMAL)
entry_flow1_y.insert(0, flow1_y)
entry_flow1_y.bind('<Button-1>', f_clear_flow1y_entry)
entry_flow1_y.pack(side="left")
entry_flow1_y.focus()

# Summit 1 =======================
btn_summit = ttk.Button(f2_fflow1, text="1 summit", command=f_mouse_summit_1)
btn_summit.pack(side='top', fill='both', expand=True)

# ================================================
# frame 2 . frame . flow 2 =======================
f2_fflow2 = ttk.Frame(f2_plan)
f2_fflow2.pack(side='top')

lbl_fflow2 = ttk.Label(f2_fflow2, text='flow 2, X : Y ')
lbl_fflow2.pack(side='left')

var_flow2_x = tk.StringVar()
entry_flow2_x = tk.Entry(f2_fflow2, textvariable=var_flow2_x, fg=f_color(1), bg=f_color(8), font=('Algerian','12','bold'), width=5, state=tk.NORMAL)
entry_flow2_x.insert(0, flow2_x)
entry_flow2_x.bind('<Button-1>', f_clear_flow2x_entry)
entry_flow2_x.pack(side="left")
entry_flow2_x.focus()

lbl_fflow2_colon = ttk.Label(f2_fflow2, text=' : ')
lbl_fflow2_colon.pack(side='left')

var_flow2_y = tk.StringVar()

entry_flow2_y = tk.Entry(f2_fflow2, textvariable=var_flow2_y, fg=f_color(1), bg=f_color(8), font=('Algerian','12','bold'), width=5, state=tk.NORMAL)
entry_flow2_y.insert(0, flow2_y)
entry_flow2_y.bind('<Button-1>', f_clear_flow2y_entry)
entry_flow2_y.pack(side="left")
entry_flow2_y.focus()

# Summit 2 =======================
btn_summit2 = ttk.Button(f2_fflow2, text="2 summit", command=f_mouse_summit_2)
btn_summit2.pack(side='top', fill='both', expand=True)

# ================================================
# frame 2 . frame . flow 3 =======================
f2_fflow3 = ttk.Frame(f2_plan)
f2_fflow3.pack(side='top')

lbl_fflow3 = ttk.Label(f2_fflow3, text='flow 3, X : Y ')
lbl_fflow3.pack(side='left')

var_flow3_x = tk.StringVar()

entry_flow3_x = tk.Entry(f2_fflow3, textvariable=var_flow3_x, fg=f_color(1), bg=f_color(8), font=('Algerian','12','bold'), width=5, state=tk.NORMAL)
entry_flow3_x.insert(0, flow3_x)
entry_flow3_x.bind('<Button-1>', f_clear_flow3x_entry)
entry_flow3_x.pack(side="left")
entry_flow3_x.focus()

lbl_fflow3_colon = ttk.Label(f2_fflow3, text=' : ')
lbl_fflow3_colon.pack(side='left')

var_flow3_y = tk.StringVar()

entry_flow3_y = tk.Entry(f2_fflow3, textvariable=var_flow3_y, fg=f_color(1), bg=f_color(8), font=('Algerian','12','bold'), width=5, state=tk.NORMAL)
entry_flow3_y.insert(0, flow3_y)
entry_flow3_y.bind('<Button-1>', f_clear_flow3y_entry)
entry_flow3_y.pack(side="left")
entry_flow3_y.focus()

# Summit 2 =======================
btn_summit3 = ttk.Button(f2_fflow3, text="3 summit", command=f_mouse_summit_3)
btn_summit3.pack(side='top', fill='both', expand=True)


# frame 2 . frame . Button =======================
btn_go = ttk.Button(f2_plan, text='GO', command=f_mouse_go)
btn_go.pack(side='top')


# f3_nor_act : =======================
btn_Normal = ttk.Button(f3_nor_act, text="normal", command=f_normal).pack(side="top", fill="both", expand=True)
btn_Active = ttk.Button(f3_nor_act, text="trytryLu", command=f_trytrylu).pack(side="top", fill="both", expand=True)

# f4_exit : =======================
btn_Exit = ttk.Button(f4_exit, text="exit", command=f_exit).pack(side="top", fill="both", expand=True)

root.mainloop()
