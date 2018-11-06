import serial
from pynmea2 import pynmea2

# tty = input("Name of the serial device\n(e.g.: '/dev/ttyUSB0'): ")
# print(tty)

# /dev/tty.usbserial-DN05A5FC

ser = serial.Serial(port="/dev/tty.usbserial-DN05A5FC",
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

print(ser.name)

while 1:
    data =ser.readline()
    # print(data)
    decodedData = data.decode("utf-8")
    if decodedData[:1] == "$":
        parsedData = pynmea2.parse(decodedData)
        print(parsedData)