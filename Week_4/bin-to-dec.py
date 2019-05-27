#!/usr/bin/env python

s = raw_input()
i = 0
v = 0
while i < len(s):
    if s[len(s) - i - 1] == "1":
        v = v + 2 ** i
    i = i + 1
print v
