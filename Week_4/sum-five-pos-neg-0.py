#!/usr/bin/env python

b = 0
m = 0
n = input()
while n != 0:
    if n <= 0:
        b = b + n
    else:
        m = m + n
    n = input()
print b, m
