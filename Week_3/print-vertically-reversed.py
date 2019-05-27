#!/usr/bin/env python

s = raw_input()

i = 0
while i < len(s):
    x = len(s) - i - 1
    print s[x]
    i = i + 1
