import pygame as pg
from pygame.constants import KEYDOWN
from . import FPS, ANCHO

class Escena():
    def __init__(self, pantalla): # le paso la pantalla donde se va acrear la escena
        self.pantalla = pantalla
        self.reloj = pg.time.Clock()

    def bucle_principal(self):
        pass

class Portada(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla) # Hereda de class Escena
        self.background = pg.image.load("resources/images/bg_portada.png")
        self.logo = pg.image.load("resources/images/logo.png")
        fuente = pg.font.Font("resources/fonts/nasalization-rg.otf", 40)
        self.callToAction = fuente.render("Pulsa <SCP> para continuar", True, (255, 255, 255))
        self.anchoTexto = self.callToAction.get_width()

    def bucle_principal(self):
        print("soy partida")
        game_over = False
        while not game_over:
            for evento in pg.event.get(): # Recupero eventos
                if evento.type == pg.QUIT:
                    exit()
                
                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_SPACE:
                        game_over = True


            #self.pantalla.fill((19, 41, 81))
            self.pantalla.blit(self.background, (0,0))
            self.pantalla.blit(self.logo, (230, 250))
            self.pantalla.blit(self.callToAction, ((ANCHO-self.anchoTexto)//2, 550)) # Obtener tamaño texto y centrado

            pg.display.flip()



class Instrucciones(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)
        self.background = pg.image.load("resources/images/bg_instrucciones.jpg")
        fuente = pg.font.Font("resources/fonts/nasalization-rg.otf", 60)
        self.texto = fuente.render("Pulsa <SCP> para JUGAR", True, (255, 255, 255))
        self.anchoTexto = self.texto.get_width()

    def bucle_principal(self):
        print("soy instrucciones")
        game_over = False
        while not game_over:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    exit()

                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_SPACE:
                        game_over = True

            self.pantalla.blit(self.background, (0, 0))
            self.pantalla.blit(self.texto, ((ANCHO-self.anchoTexto)//2 , 650))

            pg.display.flip()



class Partida(Escena):
    pass

class Records(Escena):
    pass
