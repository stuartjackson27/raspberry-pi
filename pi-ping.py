import os
import sys
import RPi.GPIO as GPIO
import time
from datetime import datetime

#IP = '192.168.1.254' #ping router gatway IP address
IP = '8.8.8.8' #ping google DNS server 

GPIO.setwarnings(False) # stops errer message due to pins in old state may need to look at a cleaner way  to do this
GPIO.setmode(GPIO.BCM) # set board mode to Broadcom
GPIO.setup(21, GPIO.OUT) # set up pin 17

while True:
  response = os.system("ping -c 1 {}" .format(IP))
  if response == 0:
    print ('internet is up!')
    GPIO.output(21, 0) # turn off pin 21 LED
    time.sleep(0.5) # sleep for 1/2 a second
  else:
    now = datetime.now()  # sets now with current data and time to that the logs can be time stamped
    f= open("/var/www/html/ping_log.html","a+")  # open a file called ping_log.log in apend mode 
    f.write(str(now))    # write the curent time to the ping_log file
    f.write("  internet is down<br>\n") # print internet is down text to the log file
    f.close()   # close the file
    print ('internet is down!')
    GPIO.output(21, 1) # turn on pin 21 LED
    time.sleep(0.5) # sleep for 1/2 a second