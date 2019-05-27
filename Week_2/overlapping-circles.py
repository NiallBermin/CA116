#!/usr/bin/env python

x1 = input()  #circle 1
y1 = input()
r1 = input()

x2 = input()  #circle 2
y2 = input()
r2 = input()

if ((x1 - x2) ** 2) + ((y1 - y2) ** 2) >= (r1 + r2) ** 2:
    print "no"
else:
    print "yes"
