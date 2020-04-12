import serial
ser = serial.Serial("COM3",9600)
while 1:
 val=int(input("enter 1 To move forward or 2 to move backward or 3 to turn right or 4 to turn left or 5 to stop"))
 if val<5:
  ser.write(val)
  print (val)
  a = ser.read()
 
 else:
  if val == 5:
   ser.close()
  else:
   print('enter a velid number')