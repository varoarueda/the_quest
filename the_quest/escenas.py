import pygame as pg
from . import FPS

class Escena():
    def __init__(self, pantalla): # le paso la pantalla donde se va acrear la escena
        self.pantalla = pantalla
        self.reloj = pg.time.Clock()

    def bucle_principal(self):
        pass

class Portada(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)
        self.background = pg.image.load("resources/images/bg_portada.png")
        self.logo = pg.image.load("resources/images/logo.png")

    def bucle_principal(self):
        game_over = False
        while not game_over:
            for evento in pg.event.get(): # Recupero eventos
                if evento.type == pg.QUIT:
                    game_over = True
            self.pantalla.fill((19, 41, 81))

            self.pantalla.blit(self.background, (0,0))
            self.pantalla.blit(self.logo, (230, 250))

            pg.display.flip()



class Partida(Escena):
    pass

class Records(Escena):
    pass
