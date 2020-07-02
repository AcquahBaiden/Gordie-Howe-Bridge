#!/usr/bin/python
import threading
import time
import sys
import os
from datetime import datetime

from tentacle_pi.AM2315 import AM2315

import getdevices


local_dir = "/home/pi/Gordie-Howe-Bridge/data/"
PATH_TO_USB = os.path.join(local_dir,time.strftime("%Y-%m-%d_%H-%M-%S"))


os.makedirs(PATH_TO_USB)

timestr = PATH_TO_USB + "/debug.log"
sys.stdout = open(timestr,"a",0)


###CONSTANTS####
_DEBUGVAR_ = True
AM_FILE_NAME = PATH_TO_USB + '/output_am2315.log'


OUTPUT_LOG_HEADERS = {'am':'Date,Time,Temp(Celsius),Humidity,crc_check\r\n'}
###ENDCONSTANTS####


###GLOBALS####
SD_SUM = 0
SD_NUM_OF_READS = 0
SD_MAX = 0
###ENDGLOBALS####


print("Baiden passec section 2")


am = AM2315(0x5c,"/dev/i2c-1")

file_am = open(AM_FILE_NAME,'a',0)


if os.path.getsize(AM_FILE_NAME) == 0:
    print ("(AM): Empty output log. Writing header")
    file_am.write(OUTPUT_LOG_HEADERS['am'])
    
    
    
def main_thread():
  
    temperature, humidity, crc_check = am.sense()
    d = datetime.now()
    str_d = d.strftime('%Y-%m-%d,%H:%M:%S:%f')
    
    file_am.write("%s,%0.1f,%0.1f,%d\r\n" % (str_d,temperature,humidity,crc_check))
    
    
def main():
    current_retry_number = 0

    
    if current_retry_number == 0:
        
        file_am.write("#"*10)
       
        
        main_thread()
    else:
        print ("Could not open serial ports!")
       
        sys.exit(1)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print ("Cleaning up GPIO")
    

