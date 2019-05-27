#!/usr/bin/env python

n = raw_input()
i = 0
s = n.split(" ")

while i < len(n):
    if "0" <= n[i] and n[i] <= "9":
        print n[i], i
        i = len(n)
    i = i + 1
