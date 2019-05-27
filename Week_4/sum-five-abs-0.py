#!/usr/bin/env python

m = 0
n = input()
while n != 0:
    if n <= 0:
        n = -n
    m = m + n
    n = input()
print m
