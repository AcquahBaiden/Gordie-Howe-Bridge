#!/usr/bin/python
import threading
import time
import sys
import os
from datetime import datetime
sys.path.insert(0, '/home/pi/Gordie-Howe-Bridge/lib/Met-One-Aerocet-531s-serial/')
from aerocet531s import Aerocet531s



aeroObject1 = Aerocet531s(38400,'/dev/ttyUSB0')



#Start serial connection to device
aeroObject1.open()
if aeroObject1 is None:
    print "Couldn't assign object"

results = aeroObject1.command('SS')

print "Status says: %s" % results
    

#aeroObject2 = Aerocet531s(38400,'/dev/ttyUSB0',1)

#sTART SERIAL CONNECTION TO DEVICE
if aeroObject1.activate_comm_mode() is None:
    print "Couldn't open com"

#"SS" command erturns the serial number
results = aeroObject1.command("D2018-07-11")

#Get the current status of the unit
stat = aeroObject1.start_sampling()
if stat is not None:
    print "Sampling started"
    
aeroObject1.close()