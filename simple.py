#!/usr/bin/env python
import time
import sys
import datetime
import urllib2

from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.led_matrix.device import max7219
from luma.core import legacy
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT

#recup variable ex heure << simple.py "$(date +'%H:%M')" >>

#for arg in sys.argv: 
 #  print arg

serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=4, block_orientation=-90)
#print("Created device")



i = 0
ii = 0
while i < 30:
	print i

        #ont recup la temperature de la salle a manger
        f = urllib2.urlopen("http://192.168.0.40/core/api/jeeApi.php?apikey=W2DfaXK7G63ZrawBFTCODepuOpHlURbRi8Ob598abQZjQwD6&type=cmd&id=385")
        tempeS = f.read()
        f.close()
        print tempeS


         #ont recup la temperature de la salle a manger
        f = urllib2.urlopen("http://192.168.0.40/core/api/jeeApi.php?apikey=W2DfaXK7G63ZrawBFTCODepuOpHlURbRi8Ob598abQZjQwD6&type=cmd&id=8")
        ext = f.read()
        f.close()
        print ext


        date = datetime.datetime.now()
        date2 = date.strftime('%d %m')
        #print date2    

        heure = time.strftime("%H:%M")
        #print time.strftime("%H:%M")

        seconde = time.strftime("%S")
        #print seconde
        #serial = spi(port=0, device=0, gpio=noop())
        #device = max7219(serial, cascaded=4, block_orientation=-90)
        #print("Created device")


        with canvas(device) as draw:
                legacy.text(draw, (0, 0), heure, fill="white", font=proportional(CP437_FONT))

        time.sleep(5)

        with canvas(device) as draw:
                legacy.text(draw, (0, 0), date2, fill="white", font=proportional(CP437_FONT))

        time.sleep(5)

        with canvas(device) as draw:
                legacy.text(draw, (0, 0), "Salle", fill="white", font=proportional(SINCLAIR_FONT))

        time.sleep(5)


        with canvas(device) as draw:
                legacy.text(draw, (0, 0), tempeS, fill="white", font=proportional(CP437_FONT))

        time.sleep(5)

        with canvas(device) as draw:
		legacy.text(draw, (5, 0), "EXT", fill="white", font=proportional(CP437_FONT))

        time.sleep(5)

        with canvas(device) as draw:
                legacy.text(draw, (0, 0), ext, fill="white", font=proportional(CP437_FONT))

        time.sleep(5)

        i = i+1

