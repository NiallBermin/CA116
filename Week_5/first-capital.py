#!/usr/bin/env python

n = raw_input()
i = 0
s = n.split(" ")

while i < len(n):
    if "A" <= n[i] and n[i] <= "Z":
        print n[i], i
        i = len(n)
    i = i + 1
