import pygame as pg
from pygame.constants import KEYDOWN
from . import FPS, ANCHO, ALTO, VELOCIDAD_PLANETA, game, CENTRO_PANTALLA
from .entidades import Nave, Asteroide, Marcadores, Marcador_derecha, Explosion, Planeta
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

        # FONDO ------------------------------------------------------------------------------------------------------------
        self.background = pg.image.load("resources/images/bg_partida2.jpg").convert()
        self.x = 0 # Para animar background

        # NAVE ------------------------------------------------------------------------------------------------------------
        self.player = Nave(True, midleft=(ANCHO-1200, ALTO//2)) # posicionamiento viene del **kwargs (init clase Nave)

        #PLANETA ------------------------------------------------------------------------------------------------------------
        self.planeta = Planeta(False, 0,  midleft=(ANCHO-20, ALTO//2))


        # EXPLOSION ------------------------------------------------------------------------------------------------------------
        self.explosion = Explosion(0, 0, False, 0)

        # ASTEROIDES ------------------------------------------------------------------------------------------------------------
        self.asteroides = []
        self.grupo_asteroides = pg.sprite.Group()
        
        for i in range(8):
            self.asteroide = Asteroide(center=(random.randrange(ANCHO+50, ANCHO+500), random.randrange(40, ALTO-40)))
            self.asteroides.append(self.asteroide)

        # VIDAS ------------------------------------------------------------------------------------------------------------
        self.letras_vidas = "VIDAS"
        #self.vidas = 3
        
        # PUNTOS ------------------------------------------------------------------------------------------------------------
        self.letras_puntos = "PUNTOS"
        #self.puntos = 0

        # NIVEL ------------------------------------------------------------------------------------------------------------
        self.letras_nivel = "NIVEL"

        # MARCADORES ------------------------------------------------------------------------------------------------------------
        self.letrero_vidas = Marcadores(20, 20, "nasalization-rg.otf", 24, (255,255,255))
        self.cuenta_vidas = Marcadores(120, 20, "nasalization-rg.otf", 24, (255,255,255))

        self.letrero_puntos = Marcadores(ANCHO - 130, 20, "nasalization-rg.otf", 24, (255,255,255))
        self.cuenta_puntos = Marcador_derecha(ANCHO - 140, 20, "nasalization-rg.otf", 24, (255,255,255))

        self.letrero_nivel =  Marcadores(ANCHO //2 - 65, 20, "nasalization-rg.otf", 24, (255,255,255))
        self.cuenta_nivel = Marcadores(ANCHO // 2 + 25, 20, "nasalization-rg.otf", 24, (255,255,255))

        # GRUPOS ------------------------------------------------------------------------------------------------------------
        self.grupo_player = pg.sprite.Group()
        self.grupo_asteroides = pg.sprite.Group()
        self.grupo_marcadores = pg.sprite.Group()
        self.grupo_explosion = pg.sprite.Group()
        self.grupo_planeta = pg.sprite.Group()

        self.grupo_player.add(self.player)
        self.grupo_marcadores.add(self.letrero_vidas, self.cuenta_vidas, self.letrero_puntos, self.cuenta_puntos, self.letrero_nivel, self.cuenta_nivel)
        self.grupo_asteroides.add(self.asteroides)
        self.grupo_explosion.add(self.explosion)
        self.grupo_planeta.add(self.planeta)


    def reset(self):
        self.player.estado = True
        self.explosion.estado = False
        self.explosion.contador = 0
        self.planeta.contador = 0
        self.puntos = 0
        self.vidas = 3
        self.nivel = 0
        self.grupo_asteroides.empty()
        self.asteroides = []
        self.grupo_asteroides = pg.sprite.Group()
        self.planeta.reset(self)
        
        for i in range(8):
            self.asteroide = Asteroide(center=(random.randrange(ANCHO+50, ANCHO+500), random.randrange(40, ALTO-40)))
            self.asteroides.append(self.asteroide)
        self.grupo_asteroides.add(self.asteroides)




    def bucle_principal(self):
        print("soy partida")
        self.reset()
        while self.vidas > 0:
            print("11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111")
            dt = self.reloj.tick(FPS) # Reloj General
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    exit()

            self.letrero_vidas.texto = self.letras_vidas
            self.cuenta_vidas.texto = self.vidas

            self.letrero_puntos.texto = self.letras_puntos
            self.cuenta_puntos.texto = self.puntos

            self.letrero_nivel.texto = self.letras_nivel
            self.cuenta_nivel.texto = self.nivel
            
            # GESTION NIVELES ------------------------------------------------------------------------------------------------------------
            if self.puntos < 25:
                self.nivel = 0
            if self.puntos >= 25:
                self.nivel = 1
            if self.puntos >= 50:
                self.nivel = 2
            if self.puntos >= 75:
                self.nivel = 3

            # UPDATES ------------------------------------------------------------------------------------------------------------
            self.grupo_player.update(dt)
            self.grupo_asteroides.update(dt)
            self.grupo_marcadores.update(dt)
            self.grupo_explosion.update(dt)
            #self.grupo_planeta.update(dt)

            #COLISION ------------------------------------------------------------------------------------------------------------
            colision = pg.sprite.groupcollide(self.grupo_player, self.grupo_asteroides, False, True)
            if colision:
                self.vidas -= 1
                self.player.estado = False
            
            if self.player.estado == False:
                #self.player.kill()
                self.grupo_player.remove(self.player)

            # EXPLOSION ------------------------------------------------------------------------------------------------------------
            if self.player.estado == True:
                self.grupo_player.add(self.player)
                self.grupo_explosion.remove(self.explosion)
            else: # Nave es False
                self.grupo_explosion.add(self.explosion)
                self.explosion.estado = True
                posicion_y_explosion = self.player.rect.center
                self.explosion.rect.center = posicion_y_explosion
                self.explosion.contador += 1

            if self.explosion.contador >= 80:
                self.explosion.estado = False
                self.grupo_explosion.remove(self.explosion)

            # RESETEAR NAVE ------------------------------------------------------------------------------------------------------------
            if self.player.estado == False and self.explosion.contador >= 60:
                self.player.reset_nave(dt)
                self.grupo_player.add(self.player)
                self.player.estado = True
                self.explosion.estado = False
                self.explosion.contador = 0

            # PUNTUACION ------------------------------------------------------------------------------------------------------------
            for self.asteroide in self.grupo_asteroides:
                if self.player.estado == True:
                    if self.asteroide.rect.right < 8:
                        self.puntos += 1
            print("2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222")

            # ANIMACION FIN NIVEL ------------------------------------------------------------------------------------------------------------
            print("ESTADO PLANETA 3 = ", self.planeta.estado)
            if self.nivel != 0 and self.planeta.contador < 60:
                self.grupo_asteroides.remove(self.asteroides)
                self.planeta.muestrate(dt)
                print("33333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333")
            if self.planeta.rect.midleft == CENTRO_PANTALLA:
                self.player.aterriza(dt)
                self.planeta.contador += 1


            # ANIMACION NUEVO NIVEL ------------------------------------------------------------------------------------------------------------
            print("ESTADO PLANETA 4 = ", self.planeta.estado)
            if self.planeta.contador >= 600:
                print("44444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444")
                self.planeta.escondete(dt)
                self.player.posicionate(dt)









            
            # RENDERIZADO ------------------------------------------------------------------------------------------------------------
            x_relativa = self.x % self.background.get_rect().width
            self.pantalla.blit(self.background, (x_relativa - self.background.get_rect().width , 0))
            if x_relativa < ANCHO:
                self.pantalla.blit(self.background, (x_relativa, 0))
            self.x -= 0.3 # Velocidad movimiento background
            
            #self.pantalla.blit(self.player.image, self.player.rect) # Haye que pasar la image (surface) y el rect (rectagulo) del Sprite de Nave

            #for asteroide in self.asteroides:
                #self.pantalla.blit(asteroide.image, asteroide.rect)

            self.grupo_asteroides.draw(self.pantalla)
            self.grupo_explosion.draw(self.pantalla)
            self.grupo_planeta.draw(self.pantalla)
            self.grupo_player.draw(self.pantalla)
            self.grupo_marcadores.draw(self.pantalla)


            print("Contadpr PLANETA = " , self.planeta.contador)

            pg.display.flip()



            

class Records(Escena):
    pass
