#!/usr/bin/env python

FILE = 'liste.txt'
 
with open(FILE, 'r') as f:
    lines = [line.strip('\n') for line in f.readlines()]
 
liste = [[line] for line in lines]

for Mliste in liste:
    print Mliste

print len(liste)

print liste[:]
