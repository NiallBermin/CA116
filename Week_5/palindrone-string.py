#!/usr/bin/env python

n = raw_input()
i = 0
x = ""

while i < len(n):
    x = x + n[len(n) - 1 - i]
    i = i + 1
if x == n:
    print "palindrome"
