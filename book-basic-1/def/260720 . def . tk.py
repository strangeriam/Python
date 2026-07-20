import tkinter as tk

root = tk.Tk()
root.title('SendTX')
root.geometry('200x100')

def ui():
	lbl_com = tk.Label(text='com:')
	lbl_com.pack()


ui()

root.mainloop()
