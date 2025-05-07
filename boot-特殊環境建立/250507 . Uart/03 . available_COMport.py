import serial.tools.list_ports

coms=serial.tools.list_ports.comports()
for a in coms:
	print(a)

# 輸出
COM3 - USB Serial Port (COM3)
[Finished in 153ms]
