#!/usr/bin/env python

n = input()

i = 0
while i <= n:
    if i == 0:
        print 1
        i = i + 1
    elif i % 5 == 0 and i % 3 == 0:
        print "fizz-buzz"
    elif i % 5 == 0:
        print "buzz"
    elif i % 3 == 0:
        print "fizz"
    else:
        print i
    i = i + 1
