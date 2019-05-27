#!/usr/bin/env python

n = raw_input()
i = 0
while i < len(n) and not (n[i] >= "A" and n[i] <= "Z"):
    i = i + 1
j = i
while j < len(n) and (n[j] >= "A" and n[j] <= "Z"):
    j = j + 1
if i < len(n):
    print n[i:j], i
