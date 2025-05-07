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

# 輸出:
A 0 : b'ping 192.168.2.1\r\n'
B 1 : b'PING 192.168.2.1 (192.168.2.1): 56 data bytes\r\n'
B 2 : b'64 bytes from 192.168.2.1: seq=1 ttl=64 time=0.150 ms\r\n'
B 3 : b'64 bytes from 192.168.2.1: seq=2 ttl=64 time=0.123 ms\r\n'
C 3 : close com
[Finished in 2.3s]
