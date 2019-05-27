#!/usr/bin/env python

n = raw_input()
i = 0
while i < len(n):
    if i > 0 and n[i] == n[i - 1]:
        print n[i] + n[i - 1]
        i = len(n)
    i = i + 1
