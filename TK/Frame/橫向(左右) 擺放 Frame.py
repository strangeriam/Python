import tkinter as tk

class GO:
	def __init__(self, root):
		self.root = root
		self.root.title("trytryLu")
		self.root.geometry('600x500')

		self._f_ui()

	def _f_ui(self):
		frameL = tk.Frame(self.root, bg="lightblue", width=300, height=500)
		frameL.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

		self.frameL_Up1 = tk.Frame(frameL)
		self.frameL_Up1.pack()

		self.lbl_L_A = tk.Label(self.frameL_Up1, text='Frame Left')
		self.lbl_L_A.pack()


		frameR = tk.Frame(self.root, bg="lightgreen", width=300, height=500)
		frameR.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

		self.frameR_Up1 = tk.Frame(frameR)
		self.frameR_Up1.pack()

		self.lbl_R_A = tk.Label(self.frameR_Up1, text='Frame Right')
		self.lbl_R_A.pack()



if __name__ == "__main__":
	root = tk.Tk()
	app = GO(root)
	root.mainloop()
