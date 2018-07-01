import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnigs(False)
GPIO.setup(21,GPIO.OUT)

count =0
for count in range (0,3):
  print "Fan On"
  GPIO.output(21,GPIO.HIGH)
  time.sleep(4)
  
  print "Fan Off"
  GPIO.output(21,GPIO.LOW)
  time.slepp(4)
  
  
