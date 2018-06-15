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
for i in range(totalZonas):
	print(zonas[i], "tiene de vecinos a: ",vecinos[i])

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

# atackar
# 1) Seleccionar Tu Zona
# 2) Seleccionar vecino para atackar siempre y cuando no sea su zona
# 3) Opcion de Finalizar Turno
# Player -> zona -> vecinos -> tirar dados->  fin player repartir dados y cambiar de player o volver a selc zona
NuevaZonas=[]
fin =1
ZonaSelc= 0
zonatemp=0
while (fin == 1):

	for i in range (cant ):			# recordar que si gana sumar mazplayers obtenidas

		print ("Player",i,"zonas disponibles",zonaPlayers[i])
		ZonaSelec= input ("Elegir tu Zona para atackar")  # temporal
		print ("vecinos ", vecinos[ZonaSelc])
		for j in range (totalZonas):
			print ("Zona")
