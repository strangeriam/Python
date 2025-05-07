# 讀到 Log 後, 顯示 Enter command or 'exit':
import serial,time
ser = serial.Serial(
	port='COM3',
	baudrate=115200,
	bytesize=serial.EIGHTBITS,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	xonxoff=False
)

line = ser.readline()

while line:
	line = ser.readline()
	print(line)
	ser.reset_input_buffer()
	# cmd = input("Enter command or 'exit':") + '\r\n'
	# if len(cmd)>0:
	# 	ser.write(cmd.encode())
	# else:
	# 	continue

# 一直讀取 Log
import serial,time
ser = serial.Serial(
	port='COM3',
	baudrate=115200,
	bytesize=serial.EIGHTBITS,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	xonxoff=False
)

line = ser.readline()

while line:
	line = ser.readline()
	print(line)
	ser.reset_input_buffer()
	# cmd = input("Enter command or 'exit':") + '\r\n'
	# if len(cmd)>0:
	# 	ser.write(cmd.encode())
	# else:
	# 	continue
