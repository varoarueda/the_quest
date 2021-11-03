import pygame as pg
from the_quest import ALTO, ANCHO, ESCENA, musica
from the_quest.escenas import Game_over, Instrucciones, Usuario, Partida, Portada, Records


class Game():
    pg.init()
    pg.mixer.pre_init(44100, -16, 2, 512)
    pg.mixer.init()
    def __init__(self):
        pantalla = pg.display.set_mode((ANCHO, ALTO)) # esta pantalla hay que pasarsela a cada una de las escenas
        self.escenas = [Portada(pantalla), Instrucciones(pantalla), Usuario(pantalla), Partida(pantalla), Records(pantalla), Game_over(pantalla)]

    def launch(self):
        i = ESCENA
        si_pierdes = 1
        self.carga_musica(0)
        while True:
            si_pierdes = self.escenas[i].bucle_principal(si_pierdes)
            i += si_pierdes
            if i >= len(self.escenas):
                i = 0
    

    def carga_musica(self, indice):
        pg.mixer.music.load(musica(indice))
        pg.mixer.music.set_volume(0.1)
        pg.mixer.music.play(-1)









