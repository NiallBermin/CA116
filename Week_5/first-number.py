#!/usr/bin/env python

n = raw_input()
i = 0
while i < len(n) and not (n[i] >= "0" and n[i] <= "9"):
    i = i + 1
j = i
while j < len(n) and (n[j] >= "0" and n[j] <= "9"):
    j = j + 1
if i < len(n):
    print n[i:j], i
