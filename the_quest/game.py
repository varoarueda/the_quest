import pygame as pg
from the_quest import ALTO, ANCHO
from the_quest.escenas import Instrucciones, Portada

pg.init()

class Game():
    def __init__(self):
        pantalla = pg.display.set_mode((ANCHO, ALTO)) # esta pantalla hay que pasarsela a cada una de las escenas
        self.escenas = [Portada(pantalla), Instrucciones(pantalla)]

    def launch(self):
        i = 0
        while True:
            self.escenas[i].bucle_principal()
            i += 1
            if i == len(self.escenas):
                i = 0
    
        


