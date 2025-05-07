import serial

ser = serial.Serial(
	port='COM3',
	baudrate=115200,
	bytesize=serial.EIGHTBITS,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	xonxoff=False
)

# ser.write(b'date >> /tmp/try.txt && cat /tmp/try.txt\r')
ser.write(b'ping 192.168.2.1\r')

line = ser.readline()

while line:
	line = ser.readline()
	print(line)
	ser.reset_input_buffer()
