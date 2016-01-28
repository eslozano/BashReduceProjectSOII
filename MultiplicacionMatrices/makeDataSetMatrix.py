#!/usr/bin/env python

# File: makeDataSetMatrix.py
#Author: Lozano J. Estefania
#Description: This file was used to create files of differents size
#to test the advantages of bashreduce. 
#Return: n lines with two matrix (first:[2,3],second:[3,2]) separate by a ","
#When execute save in a file

import numpy as np
import re
import random

#m=[[0,0],[0,0]]
for x in range(0, 2000000):
	#y=np.random.random((2, 2))
	#z=np.random.random((2, 2))
	#m=np.add(m,np.add(x, y))
	#print (str(y[0][0])+" "+
	print (str(random.random())+" "+str(random.random())+" "+str(random.random())+" "+str(random.random())+" "+str(random.random())+" "+str(random.random())+","+str(random.random())+" "+str(random.random())+" "+str(random.random())+" "+str(random.random())+" "+str(random.random())+" "+str(random.random()))

