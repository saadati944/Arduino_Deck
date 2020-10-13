import serial

sr=serial.Serial(input('enter port name : '),9600)

while True:
    print(sr.read())
