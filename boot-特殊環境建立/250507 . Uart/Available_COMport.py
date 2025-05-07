import serial.tools.list_ports

coms=serial.tools.list_ports.comports()
for a in coms:
	print(a)
