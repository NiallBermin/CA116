#!/usr/bin/env python

a = input()
b = input()

while b != 0:
    new_a = b
    b = a - (b * (a // b))
    a = new_a
print(a)
