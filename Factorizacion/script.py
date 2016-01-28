#!/usr/bin/env python

import sys

def cuadrado(n):
        return n * n

for line in sys.stdin:
       if line != '\n':
          num = int(line)
          cuad = cuadrado(num)

