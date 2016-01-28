#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import time
import sys
import re
import random
from datetime import datetime

tiempo_total_ejecucion = datetime.now() - datetime.now()
tiempo_total_procesamiento=datetime.now() - datetime.now()
tiempo_total_parsear=datetime.now() - datetime.now()

inicio_ejecucion = datetime.now()
for line in sys.stdin:
#line="0.659749400693 0.659749400693 0.365154323247 0.695452689837 0.690667257977 0.398005891725,0.659749400693 0.659749400693 0.550727192645 0.331999051777 0.690667257977 0.398005891725"
	inicio_procesamiento = datetime.now()
	inicio_parsear = datetime.now()
	tmp=line.split(',')

	array1=tmp[0].split(' ')
	for i in range(len(array1)):		
		num=float(array1[i])
		array1[i]=num
	matriz1=np.reshape(array1, (len(array1)/2-1,len(array1)/2)) 

	array2=tmp[0].split(' ')
	for i in range(len(array2)):		
		num=float(array2[i])
		array2[i]=num
	matriz2=np.reshape(array2, (len(array2)/2,len(array2)/2-1)) 

	fin_parsear=datetime.now()
	tiempo_total_parsear=fin_parsear - inicio_parsear + tiempo_total_parsear

	np.dot(matriz1, matriz2)

	fin_procesamiento=datetime.now()
	tiempo_total_procesamiento=fin_procesamiento - inicio_procesamiento + tiempo_total_procesamiento

fin_ejecucion=datetime.now()

tiempo_total_ejecucion = fin_ejecucion - inicio_ejecucion + tiempo_total_ejecucion

print "Tiempo total de parseo: {}".format(tiempo_total_parsear)
print "Tiempo total de procesamiento: {}".format(tiempo_total_procesamiento)
print "Tiempo total de ejecución: {}".format(tiempo_total_ejecucion)
