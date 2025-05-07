import serial
ser = serial.Serial("COM3", 115200)

ser
#輸出:
Serial<id=0x157a0c6b280, open=True>(port='COM3', baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=None, xonxoff=False, rtscts=False, dsrdtr=False)

ser.close()
#輸出:
Serial<id=0x157a0c6b280, open=False>(port='COM3', baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=None, xonxoff=False, rtscts=False, dsrdtr=False)




import serial
print('A')
try:
	ser = serial.Serial("com3", 115200)
	print('B')
except serial.SerialException:
	serial.Serial("com3", 115200).close()
	ser = serial.Serial("com3",115200)
	print('C')
print('done')
