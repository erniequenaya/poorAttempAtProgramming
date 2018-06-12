#!/usr/bin/python3

#logica del creador de mapas
#solo existen 2 tipos de datos: zonas y vecinos
#las zonas pueden tener hasta 8 vecinos
#la cantidad de vecinos sera definido al azar para c/zona

import random
totalZonas=40
zonas=[]
for i in range(totalZonas):
	zonas.append("zona "+str(i))
#seleccion de vecinos
maxVecinos=8
vecinos=[]
for i in range(totalZonas):
	vecinos.append([])
	for j in range(maxVecinos):
		vecinos[i].append([])
		vecinos[i][j].append(random.randint(1,totalZonas))
print(vecinos)
for i in range(totalZonas):
	print("zona ",zonas[i], "tiene de vecinos a: ",vecinos[i])
print(totalZonas)
