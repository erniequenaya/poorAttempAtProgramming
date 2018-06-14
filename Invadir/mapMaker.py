#!/usr/bin/python3

#logica del creador de mapas
#solo existen 2 tipos de datos: zonas y vecinos
#las zonas pueden tener hasta 8 vecinos
#la cantidad de vecinos sera definido al azar para c/zona
#se agrego la variable "flag" la cual evita que todas las zonas tengan 8 vecinos si o si

import random
totalZonas=10
zonas=[]
zonas=list(range(totalZonas))
print (zonas)
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
#for i in range(totalZonas):
#	print(zonas[i], "tiene de vecinos a: ",vecinos[i])

#hasta este punto el mapa es creado

###distribucion de zonas
zonaPlayers=[]
cant=2
tempzonas=zonas
#mzplayers=totalZonas/cant
mzplayers=5
zonaPlayers=[]
print(mzplayers)
for i in range(cant):
	zonaPlayers.append([])
	for j in range(mzplayers):
		zonaPlayers[i].append([])
		random.shuffle(tempzonas)
#		print("lista actual: ",tempzonas)
		zonaPlayers[i][j].append(tempzonas[0])
		tempzonas=tempzonas[1:]
	print("el jugador ",i," qedo con ",zonaPlayers[i])





