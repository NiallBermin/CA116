#!/usr/bin/env python

n = raw_input()
i = 0

while n[i] is not "+":
	i = i + 1
x = n[0:i]
k = i + 1
j = i + 1
while j < len(n):
    j = j + 1
y = n[k:j]
print int(y) + int(x)
