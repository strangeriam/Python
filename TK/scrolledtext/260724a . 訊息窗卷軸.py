import tkinter as tk
from tkinter import scrolledtext, messagebox

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


		# --- Event Log Area ---
		frameR = tk.Frame(self.root, bg="lightgreen", width=300, height=500)
		frameR.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

		tk.Label(frameR, text="Event Log:").pack(anchor=tk.W, padx=10)
		self.log_area = scrolledtext.ScrolledText(frameR, width=80, height=15, state=tk.DISABLED)
		self.log_area.pack(padx=10, pady=5)


if __name__ == "__main__":
	root = tk.Tk()
	app = GO(root)
	root.mainloop()
