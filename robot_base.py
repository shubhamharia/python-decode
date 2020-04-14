import serial
import time
ser = serial.Serial("COM3",9600)
while 1:
 time.sleep(2)
 val=int(input("enter 1 To move forward or 2 to move backward or 3 to turn right or 4 to turn left or 5 to stop"))
 if val<=5:
  if val ==1:
     ser.write(b'A')
  if val ==2:
   ser.write(b'B')
  if val ==3:
   ser.write(b'C')
  if val ==4:
   ser.write(b'D') 
  if val ==5:
   ser.close() 
 else:
   print('enter a valid number')
