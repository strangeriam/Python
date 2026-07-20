import tkinter as tk

root = tk.Tk()
root.title('SendTX')
root.geometry('200x100')

def ui():
	lbl_com = tk.Label(text='com:', width=10)
	lbl_com.pack(side=tk.LEFT)


ui()

root.mainloop()
