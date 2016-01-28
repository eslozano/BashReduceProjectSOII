#!/usr/bin/env python

import random

text_file = open("data4.txt", "w")
for x in range(0, 50000000):
    text_file.write(str(random.randint(1,1000)*1,)+'\n')
text_file.close()


