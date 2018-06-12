#!/usr/bin/python3

#logica del creador de mapas
#solo existen 2 tipos de datos: zonas y vecinos
#las zonas pueden tener hasta 8 vecinos
#la cantidad de vecinos sera definido al azar para c/zona
#se agrego la variable "flag" la cual evita que todas las zonas tengan 8 vecinos si o si

import random
totalZonas=10
zonas=[]
for i in range(totalZonas):
	zonas.append("zona "+str(i+1))
#seleccion de vecinos
maxVecinos=8
vecinos=[]
for i in range(totalZonas):
	vecinos.append([])
	for j in range(maxVecinos):
		vecinos[i].append([])
		flag=random.randint(1,10)
		if(flag<7):
			vecinos[i][j].append(random.randint(1,totalZonas))
for i in range(totalZonas):
	print(zonas[i], "tiene de vecinos a: ",vecinos[i])

#hasta este punto el mapa es creado
