#!/usr/bin/env python

nterms = input()
nterms = int(nterms)
n1 = 0
n2 = 1

if nterms == 1:
    print(n1)
else:
    while n1 < nterms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
