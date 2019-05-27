#!/usr/bin/env python

b = 0
m = 0
i = 0
while i < 5:
    n = input()
    if n <= 0:
        b = b + n
    else:
        m = m + n
    i = i + 1
print b, m
