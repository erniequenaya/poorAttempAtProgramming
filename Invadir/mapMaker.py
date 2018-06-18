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

###	PARA DISTRIBUCION INICIAL DE ZONAS POR JUGADOR	###
zonaPlayers=[]
cant=2
tempzonas=zonas
#mzplayers=totalZonas/cant
mzplayers=5

###	PARA DISTRIBUCION INICIAL DE DADOS POR ZONA	###
#cada jugador empieza con dados igual al triple de sus zonas
#dados x zona
dicePZ=[]
dicePZ=list(range(totalZonas))
print("dicePZ ",dicePZ)

for i in range(cant):
	zonaPlayers.append([])
#dados x jugador . los cuales corresponden a 15 por jugador
	dicePP=mzplayers*3
	for j in range(mzplayers):
		zonaPlayers[i].append([])
		random.shuffle(tempzonas)
		zonaPlayers[i][j].append(0)
		zonaPlayers[i][j]=tempzonas[0]
		tempzonas=tempzonas[1:]
#inicia la asignacion de dados x zona y x jugador
		if(dicePP>8):
			dicePZ[zonaPlayers[i][j]]=random.randint(1,5)
		elif(dicePP>0 and j!=mzplayers-1):
			dicePZ[zonaPlayers[i][j]]=random.randint(1,dicePP)
		else:
			dicePZ[zonaPlayers[i][j]]=dicePP
		dicePP=dicePP-dicePZ[zonaPlayers[i][j]]
		print("la zona ",zonaPlayers[i][j]," tiene ",dicePZ[zonaPlayers[i][j]], " dados y pertenece a player ",i)
	print("el jugador ",i," qedo con ",zonaPlayers[i])

###TERMINA LA ASIGNACION DE ZONAS Y DADOS POR ZONA INICIAL###


# atackar
# 1) Seleccionar Tu Zona
# 2) Seleccionar vecino para atackar siempre y cuando no sea su zona
# 3) Opcion de Finalizar Turno
# Player -> zona -> vecinos -> tirar dados->  fin player repartir dados y cambiar de player o volver a selc zona

fin =1
for i in range (cant ):
	while fin==1 :
		print ("Player ",i,"zonas disponibles",zonaPlayers[i])
		ZonaSelec= int (input ("Elegir tu Zona para atackar") ) # temporal
		for j in range (totalZonas):
			if (j == ZonaSelec) :
				print ("tiene vecinos a " , vecinos[j])
				temp=int (input( ("Atackar o cambiar zona (1/0) ")))
				if (temp==1):
					vecinoAtackar = int (input ("Seleccione vecino "))
					fin=0
				elif (temp==0):
					fin=1
print ("mi Zona ",ZonaSelec, "atacka ", vecinoAtackar)


###	DISTRIBUCION DE DADOS AL FINAL DEL TURNO	###
#ESTE PROCESO DEBE ENCADENARSE A ATACAR Y EJECUTARSE CADA VEZ QUE EL PLAYER DECIDA TERMINAR SU TURNO

#ES DECIR INMEDIATAMENTE DESPUES DE QUE fin=0

#verificar el total de zonas del jugador
#este numero se transformara en cantidad de dados a repartir al final del turno
#los dados se repartiran al azar por las zonas del jugador
#el control es cedido a la CPU o a un jugador respectivamente
i=0
reward=len(zonaPlayers[i])		### darle un multiplo a reward aumenta la cantidad a recompensar
for W in range(reward):
	dicePZ[random.choice(zonaPlayers[i])]+=1
print(dicePZ)



