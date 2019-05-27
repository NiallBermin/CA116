#!/usr/bin/env python

n = input()

i = 0
while i < n:
    if i % 2:
        print(i * - 1)
    else:
        print(i)
    i += 1
