#!/usr/bin/env python

n = input()
while n != 0:
    m = input()
    if m == 0:
        n = m
    elif m < n:
        print "lower"
    elif n < m:
        print "higher"
    elif n == m:
        print "equal"
    n = m
