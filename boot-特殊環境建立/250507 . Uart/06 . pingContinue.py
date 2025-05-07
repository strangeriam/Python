# 目的 i = 3 時, 下 Ctrl +C 離開 ping, 並且放掉 COM port. 

import serial

ser = serial.Serial(
	port='COM3',
	baudrate=115200,
	bytesize=serial.EIGHTBITS,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	xonxoff=False
)

ser.write(b'ping 192.168.2.1\r')

line = ser.readline()
print('A 0 :', line)

i = 1
while line:
	line = ser.readline()
	print('B', + i, ':', line)
	ser.reset_input_buffer()

	if i == 3:
		ser.write(bytearray(b'\x03')) # Ctrl + C 離開 ping.
		print('C', + i, ':', 'close com')
		ser.close()
		break

	i = i + 1

