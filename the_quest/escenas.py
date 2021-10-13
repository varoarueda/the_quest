import pygame as pg
from pygame.constants import KEYDOWN
from . import FPS, ANCHO, ALTO
from .entidades import Nave, Asteroide
import random

class Escena():
    def __init__(self, pantalla): # le paso la pantalla donde se va acrear la escena
        self.pantalla = pantalla
        self.reloj = pg.time.Clock()

    def bucle_principal(self):
        pass

class Portada(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla) # Hereda de class Escena
        self.background = pg.image.load("resources/images/bg_portada.png").convert()
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
        self.background = pg.image.load("resources/images/bg_instrucciones.jpg").convert()
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

        # FONDO
        self.background = pg.image.load("resources/images/bg_partida2.jpg").convert()
        self.x = 0 # Para animar background

        #GRUPO
        self.todos = pg.sprite.Group()
        
        # NAVE
        self.player = Nave(midleft=(ANCHO-1200, ALTO//2)) # posicionamiento viene del **kwargs (init clase Nave)

        # self.vidas = 3

        # ASTEROIDES
        self.asteroides = pg.sprite.Group()
        for i in range(10):
            asteroide = Asteroide(center=(random.randrange(ANCHO+50, ANCHO+500), random.randrange(40, ALTO-40)))
            self.todos.add(asteroide)

        self.todos.add(self.asteroides, self.player)



    def bucle_principal(self):
        print("soy partida")
        game_over = False
        while not game_over:
            dt = self.reloj.tick(FPS) # Reloj General
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    exit()

            # UPDATES
            #self.player.update(dt)
            #for i in range(10):
                #self.asteroides[i].update(dt)
            self.todos.update(dt)

            # BLITS
            x_relativa = self.x % self.background.get_rect().width
            self.pantalla.blit(self.background, (x_relativa - self.background.get_rect().width , 0))
            if x_relativa < ANCHO:
                self.pantalla.blit(self.background, (x_relativa, 0))
            self.x -= 0.3 # Velocidad movimiento background
            
            #self.pantalla.blit(self.player.image, self.player.rect) # Haye que pasar la image (surface) y el rect (rectagulo) del Sprite de Nave

            #for asteroide in self.asteroides:
                #self.pantalla.blit(asteroide.image, asteroide.rect)
            self.todos.draw(self.pantalla)
            


            pg.display.flip()




class Records(Escena):
    pass
