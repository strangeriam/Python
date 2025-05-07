import serial
import serial.tools.list_ports as port_list

ports = list(port_list.comports())
print(ports[0].device)
port = ports[0].device
baudrate = 9600
serialPort = serial.Serial(port=port, baudrate=baudrate,
                                bytesize=8, timeout=1, stopbits=serial.STOPBITS_ONE)
serialString = ""
# serialPort.write(bytes.fromhex("A551F6"))
serialPort.write(bytes.fromhex("A555FA"))

while True:
    try:
        # serialPort.reset_input_buffer()
        # serialPort.reset_output_buffer()
        # serialString = serialPort.read(10).hex()
        serialString = serialPort.read()
        print(serialString)
    except KeyboardInterrupt:
        break

serialPort.close()



import serial
ser = serial.Serial("COM3", 115200)
   
# Send character 'S' to start the program
ser.write(bytearray(b'ls','ascii'))

# Read line   
while True:
bs = ser.readline()
print(bs)



import serial

try:
  ser = serial.Serial("com3", 115200)

except serial.SerialException:
  serial.Serial("com3", 115200).close()
  ser = serial.Serial("com3",115200)


import serial

ser = serial.Serial(
    port='/COM3',
    baudrate=115200,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SEVENBITS
)

while(True):
    print(ser.readline())

ser.close()



import serial

ser = serial.Serial(
    port='COM4',\
    baudrate=115200,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=0)

print("connected to: " + ser.portstr)
count=1

while True:
    for line in ser.read():

        print(str(count) + str(': ') + chr(line) )
        count = count+1

ser.close()
