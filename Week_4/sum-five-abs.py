#!/usr/bin/env python

m = 0
i = 0
while i < 5:
    n = input()
    if n <= 0:
        n = -n
    m = m + n
    i = i + 1
print m
