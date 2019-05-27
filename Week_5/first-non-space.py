#!/usr/bin/env python

n = raw_input()
i = 0
s = n.split()

while i < len(n):
    if n[i] != " ":
        print i
        i = len(n)
    if i == len(n) - 1:
        print -1
    i = i + 1
