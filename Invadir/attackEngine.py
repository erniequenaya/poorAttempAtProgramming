
#Logica para atacar zonas
#tipo de datos : dados y sonas

import random

totalZonas=10
zonas=[]
for i in range(totalZonas):
	zonas.append("zona "+str(i+1))
#seleccion de vecinos
maxVecinos=3
vecinos=[]

for i in range(totalZonas):
	vecinos.append([])
	for j in range(maxVecinos):
		vecinos[i].append([])
		flag=random.randint(1,10)
		# envita la cantidad sea siempre 8
		if(flag<7):
			vecinos[i][j].append(random.randint(1,totalZonas))

for i in range(totalZonas):
	print(zonas[i], "tiene de vecinos a: ",vecinos[i])

#Mi Zona
# son 2 players que corresponde la mitad de zonas
# 1)  buscar si la la zona le pertenece a alguien
# 2) si pertenece  entonces  crear una nueva  temp  y volver a buscar

zonaPlayers=[]
mzplayers= 5     # maxima zonas por jugador


                                 
for i in range(totalZonas):
        zonaPlayers.append([])
        for j in range(mzplayers):
                zonaPlayers[i].append([])                                
                zonaPlayers[i][j].append(random.randint(1,totalZonas))                                          
                k=j
                while (k != -1 ):
                        if (zonaPlayers[i][j]==zonaPlayerz[i][k]):
                                tempzona = random.randint (1,totalZonas)
                                zonaPlayer[i][j]=tempzona
                        k -=1
                                                        
                                 
print (zonaPlayers)

for i in range (2):
        for j in range(mzplayers):
                print ("jugador ",i+1 , "tiene zona a ", zonaPlayers[i][j])

#player = random.randint(1,totalZonas)
#print("Sam carry",zonas[player], "tiene de vecinos a :" , vecinos [player] )
