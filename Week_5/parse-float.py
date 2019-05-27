#!/usr/bin/env python

n = raw_input()
i = 0

while i < len(n) and not (n[i] == "."):
    i = i + 1
print n[0:i]
j = i + 1
while j < len(n) and (n[j] != " " or "."):
    j = j + 1
print n[(i + 1):j]
