#!/usr/bin/env python

n = input()

if n == 2:
    print('prime')
elif n == 3:
    print('prime')
elif n % 2 == 0:
    print('not prime')
elif n % 3 == 0:
    print('not prime')
elif n == 1:
    print('not prime')
else:
    print('prime')
