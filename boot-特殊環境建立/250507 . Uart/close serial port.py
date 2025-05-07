import serial
ser = serial.Serial("COM3", 115200)

ser.close()


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
