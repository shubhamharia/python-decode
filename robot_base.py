import serial
ser = serial.Serial("COM3",9600)
while 1:
 val=b'(input("enter F To move forward or B to move backward or R to turn right or L to turn left or S to stop"))'
 if val == 'F','B','L','R':
  ser.write(val)
  print (val)
  a = ser.read()
 
 else:
  if val == 'S':
   ser.close()
  else:
   print('enter a velid number')
