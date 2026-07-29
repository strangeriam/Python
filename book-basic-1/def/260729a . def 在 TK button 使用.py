
def _f_apc_power(a_b):
	print('Hello', a_b)

btn_apc_a_on = tk.Button(item_frame, text="APC A ON", command=_f_apc_power("B"), state=tk.NORMAL)
# 以上, 如果直接使用 command=_f_apc_power("B"),
# 則 TK 一開啟, 在還沒按下 Button 前, 就會立即執行.

# 必須改成以下,
# --> command=lambda: _f_apc_power("B")
# 按下 Button 後, 才會執行 _f_apc_power("B") .
btn_apc_a_on = tk.Button(item_frame, text="APC A ON", command=lambda: _f_apc_power("B"), state=tk.NORMAL)
btn_apc_a_on.pack(side=tk.LEFT)

輸出:
Hello B
