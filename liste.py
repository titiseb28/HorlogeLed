#!/usr/bin/env python

FILE = 'liste.txt'
 
#creation de la liste
liste = []
for ligne in open(FILE):
    liste.append(ligne.split('\t'))
 
print liste[1][2]



print len(liste)
#print liste[:]
