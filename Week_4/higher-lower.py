#!/usr/bin/env python

n = input()
i = 0
while i < 5:
    m = input()
    if m > n:
        print "higher"
    elif n > m:
        print "lower"
    elif n == m:
        print "equal"
    n = m
    i = i + 1
