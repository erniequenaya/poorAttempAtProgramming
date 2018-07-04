#importacion de modulos
import pygame, sys
from pygame.locals import*

# constantes, como anchos y largo de pantalla,etc.

#clases y funciones utilizadas

#funcion principal del juego


def main():
    pygame.init()
    #La clase o funcion principal que crea o ejecuta el juego
    #la ventana y se indica el titulo
    size = widht, height = 640, 480
    screen  =   pygame.display.set_mode(size)
    pygame.display.set_caption("hitbasicgame")
    #cargamos el fondo y una imagen (se crea objetos "surface")
    fondo = pygame.image.load("fondo.jpg").convert_alpha()
    raksam = pygame.image.load("raksam.png").convert_alpha()
    #Indicamos la posicion de las "Surface" sobre la ventana
    screen.blit(fondo, (0, 0))
    screen.blit(raksam, (300, 220))
    # se muestran por pantalla
    pygame.display.flip()



    #contiene principalmente loop del juego

    #el bucle principal del juego
    while True:
        #posibles entradas del teclado y mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


if __name__ == '__main__':
    main()
