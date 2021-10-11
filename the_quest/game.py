import pygame as pg
from the_quest import ALTO, ANCHO
from the_quest.escenas import Portada

pg.init()

class Game():
    def __init__(self):
        pantalla = pg.display.set_mode((ANCHO, ALTO)) # esta pantalla hay que pasarsela a cada una de las escenas
        self.escenas = [Portada(pantalla)]

    def launch(self):
        self.escenas[0].bucle_principal()
        pg.quit()


