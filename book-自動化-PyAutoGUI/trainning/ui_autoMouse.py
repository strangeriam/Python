
import tkinter as tk
from tkinter import ttk

import sys, time, datetime

programSize = '600x400'

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

import pyautogui
screenWidth = pyautogui.size()[0]
screenHeight = pyautogui.size()[1]
screenSize = screenWidth, 'x', screenHeight
print(screenSize)

root = tk.Tk()
root.geometry( programSize )

# ==================================================
frame_1 = ttk.Frame(root)
frame_2 = ttk.Frame(root)
frame_3 = ttk.Frame(root)
frame_4 = ttk.Frame(root)

frame_1.pack(side="left", fill="both", expand=True)
frame_2.pack(side="left", fill="both", expand=True)
frame_3.pack(side="left", fill="both", expand=True)
frame_4.pack(side="left", fill="both", expand=True)

lbl_1 = ttk.Label(frame_1, text='FRAME 1')
lbl_2 = ttk.Label(frame_2, text='FRAME 2')
lbl_3 = ttk.Label(frame_3, text='FRAME 3')
lbl_4 = ttk.Label(frame_4, text='FRAME 4')

# lbl_1.pack(side='top')
# lbl_2.pack(side='top')
# lbl_3.pack(side='top')
# lbl_4.pack(side='top')

# FRAME 1 =======================
frame1_1top = ttk.Frame(frame_1)
frame1_1top.pack(side='top', ipadx=10, ipady=30)

frame1_1middle = ttk.Frame(frame_1)
frame1_1middle.pack(side='top', ipadx=10, ipady=30)

frame1_1bottom = ttk.Frame(frame_1)
frame1_1bottom.pack(side='top', ipadx=10, ipady=10)

lbl_title1 = ttk.Label(frame1_1top, text='- INFORMATION -')
lbl_title2 = ttk.Label(frame1_1middle, text='- MOUSE POSITION -')
lbl_title3 = ttk.Label(frame1_1bottom, text='- GO -')
lbl_title1.pack(side='top')
lbl_title2.pack(side='top')
# lbl_title3.pack(side='top')

# Information =======================
frame1_resolution = ttk.Frame(frame1_1top)
frame1_uisize = ttk.Frame(frame1_1top)
frame1_resolution.pack(side='top')
frame1_uisize.pack(side='top')

lbl_info1a = ttk.Label(frame1_resolution, text='Screen Resolution: ')
lbl_info2b = ttk.Label(frame1_resolution, text=screenSize)
lbl_info1a.pack(side='left', ipadx=5, ipady=5)
lbl_info2b.pack(side='right')

lbl_info2a = ttk.Label(frame1_uisize, text='Program UI Size: ')
lbl_info1b = ttk.Label(frame1_uisize, text=programSize)
lbl_info2a.pack(side='left', ipadx=5, ipady=5)
lbl_info1b.pack(side='right')

# Mouse position X =======================
frame_1x = ttk.Frame(frame1_1middle)
frame_1x.pack(side="top", fill="both", expand=True)

var_position_x = tk.StringVar()
lbl_mouse_x = tk.Label(frame_1x, text='X: ')
lbl_mouse_x.pack(side="left", ipadx=5, ipady=5)

entry_mouse_x = ttk.Entry(frame_1x, width=15, textvariable=var_position_x)
entry_mouse_x.pack(side="left")
entry_mouse_x.focus()

# Mouse position Y =======================
frame_1y = ttk.Frame(frame1_1middle)
frame_1y.pack(side="top", fill="both", expand=True)

var_position_y = tk.StringVar()
lbl_mouse_y = tk.Label(frame_1y, text='Y: ')
lbl_mouse_y.pack(side="left", ipadx=10, ipady=10)

entry_mouse_y = ttk.Entry(frame_1y, width=15, textvariable=var_position_y)
entry_mouse_y.pack(side="left")
entry_mouse_y.focus()

# Summit =======================
frame_1btn = ttk.Frame(frame1_1bottom)
frame_1btn.pack(side="top", fill="both", expand=True)

btn_summit = ttk.Button(frame1_1bottom, text="GO")
btn_summit.pack(side='top', fill='both', expand=True)

# frame_3 : =======================
btn_Normal = ttk.Button(frame_3, text="normal", command=f_normal)
btn_Active = ttk.Button(frame_3, text="active", command=f_active)

btn_Normal.pack(side="top", fill="both", expand=True)
btn_Active.pack(side="top", fill="both", expand=True)

# frame_4 : =======================
btn_Exit = ttk.Button(frame_4, text="exit", command=f_exit)
btn_Exit.pack(side="top", fill="both", expand=True)

# ==================================================
root.mainloop()
