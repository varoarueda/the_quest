import pygame as pg
from pygame.constants import KEYDOWN
from . import FPS, ANCHO, ALTO
from .entidades import Nave

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
        print("soy portada")
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
            self.pantalla.blit(self.callToAction, ((ANCHO-self.anchoTexto)//2, 650)) # Obtener tamaño texto y centrado

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
            self.pantalla.blit(self.texto, ((ANCHO-self.anchoTexto)//2 , 550))

            pg.display.flip()



class Partida(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)
        self.background = pg.image.load("resources/images/bg_partida2.jpg").convert()
        self.x = 0 # Para animar background
        self.player = Nave(midleft=(ANCHO-1200, ALTO//2)) # posicionamiento viene del **kwargs (init clase Nave)
        # self.vidas = 3
        

    def bucle_principal(self):
        print("soy partida")
        game_over = False
        while not game_over:
            dt = self.reloj.tick(FPS) # Reloj General
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    exit()


            self.player.update(dt)
            #Animacion fondo
            x_relativa = self.x % self.background.get_rect().width
            self.pantalla.blit(self.background, (x_relativa - self.background.get_rect().width , 0))
            if x_relativa < ANCHO:
                self.pantalla.blit(self.background, (x_relativa, 0))
            self.x -= 1 # Velocidad movimiento background
            self.pantalla.blit(self.player.image, self.player.rect) # Haye que pasar la image (surface) y el rect (rectagulo) del Sprite de Nave
            


            pg.display.flip()




class Records(Escena):
    pass
