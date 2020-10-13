import serial
import profile
import amk
import time
import os

# load default profile
dpr=open('.\\defprofile','r')
defprof=dpr.readline()
lines=profile.load('.\\profiles\\'+defprof)
print('loaded profile :',defprof)
dpr.close()

amk.setupKeyboard()
amk.setupMouse()

#use user defined port if avaliable else get port name from user.
if 'port' in lines:
    port=lines['port']
else:
    port=input('enter port name : ')

sr=serial.Serial(port,9600)

# read a character from serial port then ...
while True:
    try:
        ch=sr.read(1).decode()
        nextprof=amk.execute(lines['global'])
        nextprof=amk.execute(lines[ch])
        if nextprof!='' and os.path.exists('.\\profiles\\'+nextprof):
            lines=config.load('.\\profiles\\'+nextprof)
            print('new profile loaded :',nextprof)
            with open('.\\defprofile','w') as dp:
                dp.truncate(0)
                dp.seek(0)
                dp.write(nextprof)
                dp.flush()
    except:
        time.sleep(0.01)
    sr.flush()