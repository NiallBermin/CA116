#!/usr/bin/env python

n = input()

if n == 11 or n == 12 or n == 13:
    print('th')
elif int(str(n)[-1]) == 1:
    print('st')
elif int(str(n)[-1]) == 2:
    print('nd')
elif int(str(n)[-1]) == 3:
    print('rd')
else:
    print('th')
