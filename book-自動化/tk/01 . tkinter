import tkinter as tk

root = tk.Tk()
root.geometry("600x400")

rectangle_1 = tk.Label(root, text="Rectangle 1", bg="green", fg="white")
rectangle_1.pack(ipadx=10, ipady=10)

rectangle_2 = tk.Label(root, text="Rectangle 2", bg="red", fg="white")
rectangle_2.pack(ipadx=10,ipady=10)

root.mainloop()

其他功能

. 塞滿 x 軸
;#  =======
rectangle_1.pack(ipadx=10, ipady=10, fill="x")

. 強制 y 軸填滿
;#  ===========
rectangle_1.pack(ipadx=10, ipady=10, fill="y", expand=True)

. 強制填滿 xy 軸
;#  ============
rectangle_1.pack(ipadx=10, ipady=10, fill="both", expand=True)

. 不指定 xy 軸, 空間填滿
;#  ===================
rectangle_1.pack(ipadx=10, ipady=10, expand=True)

. Using expand on both rectangles.
;#  ===============================
rectangle_1.pack(ipadx=10, ipady=10, fill="both", expand=True)
rectangle_2.pack(ipadx=10, ipady=10, expand=True)

. side left
;#  ========
rectangle_1.pack(side="left", ipadx=10, ipady=10, fill="both")
rectangle_2.pack(ipadx=10, ipady=10, fill="both")

. 有定義 side=”left” 優先
;#  =====================
rectangle_1.pack(side="left", ipadx=10, ipady=10, fill="both", expand=True)
rectangle_2.pack(ipadx=10, ipady=10, fill="both", expand=True)

. 3 個物件的占比 expansion priority
;#  ===============================
rectangle_1 = tk.Label(root, text="Rectangle 1", bg="green", fg="white")
rectangle_1.pack(side="left", ipadx=10, ipady=10, fill="both", expand=True)

rectangle_2 = tk.Label(root, text="Rectangle 2", bg="red", fg="white")
rectangle_2.pack(side="top", ipadx=10, ipady=10, fill="both", expand=True)

rectangle_3 = tk.Label(root, text="Rectangle 3", bg="black", fg="white")
rectangle_3.pack(side="left", ipadx=10, ipady=10, fill="both", expand=True)

. expansion priority
;#  =========================================================
rectangle_3.pack(side="left", ipadx=10, ipady=10, fill="both")



