import tkinter as tk

root = tk.Tk()

def _f_change_text():
	btn_txt_var.set('Going')

btn_txt_var = tk.StringVar()
btn_txt_var.set('Go')

btn_com = tk.Button(root, textvariable=btn_txt_var, command=_f_change_text, width=15)
btn_com.pack(pady=10)
btn_com.config(state=tk.NORMAL)

root.mainloop()


輸出:
執行程式後, 會出現一個 Button, 上面顯示文字 "Go".
點選 Button, 上面文字會變成 "Going".
