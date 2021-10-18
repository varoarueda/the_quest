import pygame as pg
from pygame.constants import KEYDOWN
from . import FPS, ANCHO, ALTO, game
from .entidades import Nave, Asteroide, Marcadores
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

            self.pantalla.blit(self.background, (0,0))
            self.pantalla.blit(self.logo, (230, 250))
            self.pantalla.blit(self.callToAction, ((ANCHO-self.anchoTexto)//2, 650)) # Obtener tamaño texto y centrado

            pg.display.flip()

class Game_over(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla) 
        self.background = pg.image.load("resources/images/bg_gameover.png")
        fuente = pg.font.Font("resources/fonts/nasalization-rg.otf", 60)
        self.texto = fuente.render("Pulsa Y para JUGAR otra vez", True, (255, 255, 255))
        self.anchoTexto = self.texto.get_width()

    def bucle_principal(self):
        print("soy game_over")
        game_over = False
        while not game_over:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    exit()

                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_y:
                        game_over = True
                '''
                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_y:
                        game_over = self.escenas.partida.blucle_principal()
                '''
            self.pantalla.blit(self.background, (0, 0))
            self.pantalla.blit(self.texto, ((ANCHO - self.anchoTexto)//2, 650))

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

        # NAVE
        self.player = Nave(midleft=(ANCHO-1200, ALTO//2)) # posicionamiento viene del **kwargs (init clase Nave)

        # ASTEROIDES
        self.asteroides = []
        self.grupo_asteroides = pg.sprite.Group()
        
        for i in range(4):
            self.asteroide = Asteroide(center=(random.randrange(ANCHO+50, ANCHO+500), random.randrange(40, ALTO-40)))
            self.asteroides.append(self.asteroide)
        #self.grupo_asteroides.add(self.asteroides)

        # VIDAS
        self.letras_vidas = "VIDAS"
        self.vidas = 3
        
        # PUNTOS
        self.letras_puntos = "PUNTOS"
        self.puntos = 0

        # MARCADORES
        self.letrero_vidas = Marcadores(20, 20, "nasalization-rg.otf", 24, (255,255,255))
        self.cuenta_vidas = Marcadores(120, 20, "nasalization-rg.otf", 24, (255,255,255))

        self.letrero_puntos = Marcadores(ANCHO - 130, 20, "nasalization-rg.otf", 24, (255,255,255))
        self.cuenta_puntos = Marcadores(ANCHO - 180, 20, "nasalization-rg.otf", 24, (255,255,255))

        # GRUPOS
        self.grupo_player = pg.sprite.Group()
        self.grupo_asteroides = pg.sprite.Group()
        self.grupo_marcadores = pg.sprite.Group()

        self.grupo_player.add(self.player)
        self.grupo_marcadores.add(self.letrero_vidas, self.cuenta_vidas, self.letrero_puntos, self.cuenta_puntos)
        self.grupo_asteroides.add(self.asteroides)


    def bucle_principal(self):
        print("soy partida")
        game_over = False
        self.vidas = 3
        while not game_over:
            dt = self.reloj.tick(FPS) # Reloj General
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    exit()

            self.letrero_vidas.texto = self.letras_vidas
            self.cuenta_vidas.texto = self.vidas

            self.letrero_puntos.texto = self.letras_puntos
            self.cuenta_puntos.texto = self.puntos

            # UPDATES
            self.grupo_player.update(dt)
            self.grupo_asteroides.update(dt)
            self.grupo_marcadores.update(dt)

            #COLLIDE
            tocados = pg.sprite.groupcollide(self.grupo_player, self.grupo_asteroides, False, True)
            if (tocados):
                self.vidas -= 1
            if self.vidas < 1:
                game_over = True
            print(tocados)
            
            


            # BLITS
            x_relativa = self.x % self.background.get_rect().width
            self.pantalla.blit(self.background, (x_relativa - self.background.get_rect().width , 0))
            if x_relativa < ANCHO:
                self.pantalla.blit(self.background, (x_relativa, 0))
            self.x -= 0.3 # Velocidad movimiento background
            
            #self.pantalla.blit(self.player.image, self.player.rect) # Haye que pasar la image (surface) y el rect (rectagulo) del Sprite de Nave

            #for asteroide in self.asteroides:
                #self.pantalla.blit(asteroide.image, asteroide.rect)
            self.grupo_player.draw(self.pantalla)
            self.grupo_asteroides.draw(self.pantalla)
            self.grupo_marcadores.draw(self.pantalla)



            pg.display.flip()




class Records(Escena):
    pass
