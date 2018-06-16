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
#seleccion de vecinos
maxVecinos=8
vecinos=[]
for i in range(totalZonas):
	vecinos.append([])
	for j in range(maxVecinos):
		vecinos[i].append([])
		flag=random.randint(1,10)
		vecinos[i][j]=0
		if(flag<7):
			vecinos[i][j]=random.randint(1,totalZonas)
for i in range(totalZonas):
	print(zonas[i], "tiene de vecinos a: ",vecinos[i])

#hasta este punto el mapa es creado

###distribucion de zonas####
zonaPlayers=[]
cant=2
tempzonas=zonas
print("tempzonas ",tempzonas)
print(zonas)
#mzplayers=totalZonas/cant
mzplayers=5
zonaPlayers=[]

###para dist inicial
#cada jugador empieza con dados igual al triple de sus zonas
#dados x zona
dicePZ=[]
dicePZ=list(range(totalZonas))
print("dicePZ ",dicePZ)
#distribucion de dados x zona


for i in range(cant):
	zonaPlayers.append([])
#dados x jugador
	dicePP=mzplayers*3
	for j in range(mzplayers):
		zonaPlayers[i].append([])
		random.shuffle(tempzonas)
		zonaPlayers[i][j].append(0)
		zonaPlayers[i][j]=tempzonas[0]
		tempzonas=tempzonas[1:]
#inicia la asignacion de dados x zona y x jugador
#		temp=random.randint(1,dicePP)
		if(dicePP>8):
			dicePZ[zonaPlayers[i][j]]=random.randint(1,5)
		elif(dicePP>0 and j!=mzplayers):
			dicePZ[zonaPlayers[i][j]]=random.randint(1,dicePP)
		else:
			dicePZ[zonaPlayers[i][j]]=dicePP
		dicePP=dicePP-dicePZ[zonaPlayers[i][j]]
		print("la zona ",zonaPlayers[i][j]," tiene ",dicePZ[zonaPlayers[i][j]], " dados y pertenece a player ",i)
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
