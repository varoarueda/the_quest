import pygame as pg
from the_quest import ALTO, ANCHO

pg.init()

class Game():
    def __init__(self):
        self.pantalla = pg.display.set_mode((ANCHO, ALTO))

    def launch(self):
        game_over = False
        while not game_over:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    game_over = True
            self.pantalla.fill((255, 255, 0))

            pg.display.flip()

        pg.quit()


