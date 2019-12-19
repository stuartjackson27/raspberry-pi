import os
import sys
import RPi.GPIO as GPIO
import time
from datetime import datetime

#IP = '192.168.1.254'
IP = '8.8.8.8'

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) # set board mode to Broadcom
GPIO.setup(21, GPIO.OUT) # set up pin 17

while True:
  response = os.system("ping -c 1 {}" .format(IP))
  if response == 0:
    print ('internet is up!')
    GPIO.output(21, 0) # turn off pin 21
    time.sleep(0.5)
  else:
    now = datetime.now()  
    f= open("ping_log.log","a+")
    f.write(str(now))
    f.write("  internet is down\n")
    f.close()
    print ('internet is down!')
    GPIO.output(21, 1) # turn on pin 21
    time.sleep(0.5)