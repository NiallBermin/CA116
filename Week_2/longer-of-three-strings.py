#!/usr/bin/env python

l1 = raw_input()
l2 = raw_input()
l3 = raw_input()

x = len(l1)
y = len(l2)
z = len(l3)

if x > y and x > z:
    print l1

elif y > x and y > z:
    print l2
else:
    print l3
