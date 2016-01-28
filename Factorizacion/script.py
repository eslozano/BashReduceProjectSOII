#!/usr/bin/env python

import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

for line in sys.stdin:
       if line != '\n':
          num = int(line)
          fact = factorial(num)
          print fact

