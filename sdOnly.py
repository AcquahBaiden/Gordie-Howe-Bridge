#!/usr/bin/python
import threading
import sys
import serial

sys.path.insert(0, '/home/pi/Gordie-Howe-Bridge/lib/REED-SD-4023-serial/')
from sd_4023 import SD_4023

sdObject1= SD_4023('/dev/ttyUSB0')

sta = sdObject1.get_status()
print sta

opening = sdObject1.open()
if opening is None:
    print "failed to open connection"

data_stream = sdObject1.read()
print data_stream

decibels = sdObject1.read_decibel()
print decibels

sta = sdObject1.get_status()
print sta

sdObject1.close()



