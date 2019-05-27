#!/usr/bin/env python

n = input()
y = input()

i = 0
while i < n:
    if y % 2 == 0:
        print y
        y = y / 2
    elif y % 2 != 0:
        print y
        y = y * 3 + 1
    i = i + 1
