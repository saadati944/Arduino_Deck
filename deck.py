import serial
import profile

# load default profile
dpr=open('.\\defprofile','r')
defprof=dpr.readline()
lines=profile.load('.\\profiles\\'+defprof)
print('loaded profile :',defprof)
dpr.close()

#use user defined port if avaliable else get port name from user.
if 'port' in lines:
    port=lines['port']
else:
    port=input('enter port name : ')

sr=serial.Serial(port,9600)

while True:
    print(sr.read())
