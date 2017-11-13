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

serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=4, block_orientation=-90)

#metttre le fichier liste.txt en liste
FILE = 'liste.txt'
 
#creation de la liste
liste = []
for ligne in open(FILE):
    liste.append(ligne.split('\t'))


i = 0
ii =0

while i < 10:
	print i

        #ont recup la Date
        date = datetime.datetime.now()
        date2 = date.strftime('%d %m')
        
	#ont recup l'heure
        heure = time.strftime("%H:%M")
        

        for message in liste:
				
		type = liste[ii][1]

		if type == "TXT":
			message = liste[ii][2]

		if type == "URL":
			URL = liste[ii][2]
			f = urllib2.urlopen(URL)
		        message = f.read()
        		f.close()

		if type == "SH":
			sh = liste[ii][0]
			
			if sh == "heure":
				message = heure
			if sh == "date":
				message = date2

		with canvas(device) as draw:
                	legacy.text(draw, (0, 0), message, fill="white", font=proportional(CP437_FONT))

        	time.sleep(5)
		ii=ii+1


        i = i+1
	ii = 0
