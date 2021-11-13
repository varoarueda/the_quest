import pygame as pg
from pygame.constants import KEYDOWN
from . import FPS, ANCHO, ALTO, LIMITE_TIEMPO_ANIMACION_CAMBIO_NIVEL, VELOCIDAD_NAVE, VELOCIDAD_PLANETA, game, CENTRO_PANTALLA, DURACION_EXPLOSION, TIEMPO_DURACION_NIVEL, NIVEL, sonido
from .entidades import EstadoAsteroide, EstadoExplosion, EstadoPlaneta, EstadoPlayer, Nave, Asteroide, Marcadores, Marcador_derecha, Explosion, Planeta
import random
from enum import Enum

class Escena():
    def __init__(self, pantalla): # le paso la pantalla donde se va acrear la escena
        self.pantalla = pantalla
        self.velocidad = pg.time.Clock()

    def bucle_principal(self):
        pass

class Portada(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla) # Hereda de class Escena
        self.background = pg.image.load("resources/images/bg_portada.png").convert()
        self.logo = pg.image.load("resources/images/logo.png")
        fuente = pg.font.Font("resources/fonts/nasalization-rg.otf", 55)
        self.callToAction = fuente.render("Pulsa <SCP> para CONTINUAR", True, (255, 255, 255))
        self.anchoTexto = self.callToAction.get_width()

    def bucle_principal(self, si_pierdes, usuario):
        print("soy portada")
        si_pierdes = 1
        game_over = False
        while not game_over:
            for evento in pg.event.get(): # Recupero eventos
                if evento.type == pg.QUIT:
                    exit()
                
                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_SPACE:
                        game_over = True
                    if evento.key == pg.K_ESCAPE:
                        game_over = True



            self.pantalla.blit(self.background, (0,0))
            self.pantalla.blit(self.logo, (230, 250))
            self.pantalla.blit(self.callToAction, ((ANCHO-self.anchoTexto)//2, 650)) # Obtener tamaño texto y centrado

            pg.display.flip()

        return si_pierdes, usuario

class Game_over(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla) 
        self.background = pg.image.load("resources/images/bg_gameover.png")
        fuente = pg.font.Font("resources/fonts/nasalization-rg.otf", 60)
        self.texto = fuente.render("Pulsa <SPC> para JUGAR otra vez", True, (255, 255, 255))
        self.anchoTexto = self.texto.get_width()

    def bucle_principal(self, si_pierdes, usuario):
        print("soy game_over")
        si_pierdes = 1
        game_over = False
        while not game_over:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    exit()

                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_SPACE:
                        game_over = True
                        

            self.pantalla.blit(self.background, (0, 0))
            self.pantalla.blit(self.texto, ((ANCHO - self.anchoTexto)//2, 650))

            pg.display.flip()

        return si_pierdes, usuario



class Instrucciones(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)
        self.background = pg.image.load("resources/images/bg_instrucciones.jpg").convert()
        fuente = pg.font.Font("resources/fonts/nasalization-rg.otf", 55)
        self.texto = fuente.render("Pulsa <SCP> para CONTINUAR", True, (255, 255, 255))
        self.anchoTexto = self.texto.get_width()

    def bucle_principal(self, si_pierdes, usuario):
        print("soy instrucciones")
        si_pierdes = 1
        game_over = False
        while not game_over:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    exit()

                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_SPACE:
                        game_over = True
                    if evento.key == pg.K_ESCAPE:
                        game_over = True


            self.pantalla.blit(self.background, (0, 0))
            self.pantalla.blit(self.texto, ((ANCHO-self.anchoTexto)//2 , 550))

            pg.display.flip()

        return si_pierdes, usuario

class Usuario(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla) 
        self.background = pg.image.load("resources/images/bg_records.png")
        
        fuente = pg.font.Font("resources/fonts/nasalization-rg.otf", 70)
        self.texto = fuente.render("Introduce tu Usuario", True, (255, 255, 255))
        self.anchoTexto = self.texto.get_width()

        fuente2 = pg.font.Font("resources/fonts/nasalization-rg.otf", 45)
        self.texto2 = fuente2.render("Pulsa <SPC> para empezar la PARTIDA", True, (255, 255, 255))
        self.anchoTexto2 = self.texto2.get_width()

        self.fuente_usuario = pg.font.Font("resources/fonts/nasalization-rg.otf", 90)


    def bucle_principal(self, si_pierdes, usuario):
        usuario = ''
        si_pierdes = 1
        game_over = False
        while not game_over:
            
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    exit()

                if evento.type == pg.KEYDOWN:

                    if evento.key == pg.K_SPACE:
                        game_over = True

                    elif evento.key == pg.K_BACKSPACE:
                        if usuario != '':
                            usuario = usuario[:-1]

                    elif len(usuario) < 3:
                        usuario += evento.unicode.upper()
                    self.texto_usuario = self.fuente_usuario.render(usuario, True, (255, 255, 255))
                    self.anchoTexto_usuario = self.texto_usuario.get_width()

            self.pantalla.blit(self.background, (0, 0))
            self.pantalla.blit(self.texto, ((ANCHO-self.anchoTexto)//2 , 100))
            self.pantalla.blit(self.texto2, ((ANCHO-self.anchoTexto2)//2 , 600))
            if usuario != '':
                self.pantalla.blit(self.texto_usuario, ((ANCHO-self.anchoTexto_usuario)//2 , 350))

            pg.display.flip()
        print("USUARIO = ", usuario)

        return si_pierdes, usuario


class Partida(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)

        # FONDO ----------------------------------------------------------------------------------------------------------------
        self.background = pg.image.load("resources/images/bg_partida2.jpg").convert()
        self.x = 0 # Para animar background

        # TEXTO_WIN ----------------------------------------------------------------------------------------------------------------
        fuente = pg.font.Font("resources/fonts/nasalization-rg.otf", 120)
        self.texto = fuente.render("YOU WIN", True, (255, 255, 255))
        self.anchoTexto = self.texto.get_width()

        # NIVEL --------------------------------------------------------------------------------------------------------------
        # self.nivel = 1

        # CONTADORES
        self.temporizador_nivel = 0

        # NAVE ----------------------------------------------------------------------------------------------------------------
        self.player = Nave(EstadoPlayer.NAVEGANDO, midleft=(0, ALTO//2)) # posicionamiento viene del **kwargs (init clase Nave)

        #PLANETA --------------------------------------------------------------------------------------------------------------
        self.lista_planetas = []
        for disfraz in range(4):
            self.lista_planetas.append(Planeta(EstadoPlaneta.ESCONDETE, disfraz +1, midleft=(ANCHO-20, ALTO//2)))

        # EXPLOSION ------------------------------------------------------------------------------------------------------------
        self.explosion = Explosion(0, 0, EstadoExplosion.OFF, 0)

        # MARCADORES ------------------------------------------------------------------------------------------------------------
        self.letrero_vidas = Marcadores(20, 20, "nasalization-rg.otf", 24, (255,255,255))
        self.cuenta_vidas = Marcadores(120, 20, "nasalization-rg.otf", 24, (255,255,255))

        self.letrero_puntos = Marcadores(ANCHO - 130, 20, "nasalization-rg.otf", 24, (255,255,255))
        self.cuenta_puntos = Marcador_derecha(ANCHO - 140, 20, "nasalization-rg.otf", 24, (255,255,255))

        self.letrero_nivel =  Marcadores(ANCHO //2 - 240, 20, "nasalization-rg.otf", 24, (255,255,255))
        self.cuenta_nivel = Marcadores(ANCHO // 2 -150, 20, "nasalization-rg.otf", 24, (255,255,255))

        self.letrero_tiempo = Marcadores(ANCHO//2 + 90 , 20, "nasalization-rg.otf", 24, (255,255,255))
        self.tiempo = Marcadores(ANCHO//2 + 200 , 20, "nasalization-rg.otf", 24, (255,255,255))

        # GRUPOS -----------------------------------------------------------------------------------------------------------------
        self.grupo_asteroides = pg.sprite.Group()
        self.grupo_marcadores = pg.sprite.Group()
        self.grupo_explosion = pg.sprite.Group()
        self.grupo_planeta = pg.sprite.Group()

        self.grupo_marcadores.add(self.letrero_vidas, self.cuenta_vidas, self.letrero_puntos, self.cuenta_puntos, self.letrero_nivel, self.cuenta_nivel, self.letrero_tiempo, self.tiempo)
        self.grupo_explosion.add(self.explosion)

        # SONIDOS ------------------------------------------------------------------------------------------------------------
        self.explosion_fx = self.carga_sonido("explosion")
        
    def carga_sonido(self, fx, volumen=1):
        _fx = pg.mixer.Sound(sonido(fx))
        _fx.set_volume(volumen)
        return _fx 


    def reset(self):
        self.player.reset()
        self.cuenta_atras = TIEMPO_DURACION_NIVEL
        self.explosion.contador = DURACION_EXPLOSION
        self.temporizador_nivel = 0
        self.puntos = 0
        self.vidas = 3
        self.nivel = NIVEL
        self.paso_nivel(self.nivel)


    def paso_nivel(self, nivel):
        self.lista_planetas[nivel].reset()
        
        # ASTEROIDES ------------------------------------------------------------------------------------------------------------
        self.grupo_asteroides.empty()
        self.asteroides = []
        self.grupo_asteroides = pg.sprite.Group()

        if nivel == 0:
            for i in range(5):
                self.asteroide = Asteroide(self.nivel, center=(random.randrange(ANCHO+50, ANCHO+500) , random.randrange(40, ALTO-40)))
                self.asteroides.append(self.asteroide)
        else:
            for i in range(nivel * 5):
                self.asteroide = Asteroide(self.nivel, center=(random.randrange(ANCHO+50, ANCHO+500*self.nivel) , random.randrange(40, ALTO-40)))
                self.asteroides.append(self.asteroide)

        self.grupo_asteroides.add(self.asteroides)


    def bucle_principal(self, si_pierdes, usuario): ########################################################################################################
        print("soy partida")
        self.reset()
        si_pierdes = 2
        game_over = False
        while not game_over:

            dt = self.velocidad.tick(FPS) # Reloj General
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    exit()

                if evento.type == pg.KEYDOWN:   
                    if evento.key == pg.K_ESCAPE:
                        game_over = True

                    
            # MARCADORES ----------------------------------------------------------------------------------------------------------------
            self.letrero_vidas.texto = "VIDAS"
            self.cuenta_vidas.texto = self.vidas

            self.letrero_puntos.texto = "PUNTOS"
            self.cuenta_puntos.texto = self.puntos

            self.letrero_nivel.texto = "NIVEL"
            self.cuenta_nivel.texto = self.nivel

            self.letrero_tiempo.texto = "TIEMPO"
            if self.nivel != None:
                self.tiempo.texto = int(self.cuenta_atras)

            # CUENTA ATRAS
            if self.nivel != None:
                self.cuenta_atras -= 1.5 /100
                if self.cuenta_atras <= 0:
                    self.cuenta_atras = 0

            # SINCRONIZA POSICION NAVE Y EXPLOSION ---------------------------------------------------------------------------------------------------------------
            posicion_explosion = self.player.rect.center
            self.explosion.rect.center = posicion_explosion

            # LOGICA JUEGO
            if self.cuenta_atras > 0:
                colision = pg.sprite.spritecollide(self.player, self.grupo_asteroides, True)
                if colision and self.explosion.colision:
                    self.vidas -= 1
                    self.explosion.colision = False
                    self.explosion.estado = EstadoExplosion.ON
                    self.explosion_fx.play()

            if self.explosion.estado == EstadoExplosion.ON:
                self.explosion.contador -= 1
                if self.explosion.contador < 0:
                    self.explosion.estado = EstadoExplosion.OFF
                    self.explosion.colision = True
                    self.player.estado = EstadoPlayer.NAVEGANDO
                    if self.vidas == 0:
                        game_over = True
                    elif self.vidas == 1:
                        self.explosion.contador = DURACION_EXPLOSION *2
                    else:
                        self.explosion.contador = DURACION_EXPLOSION

            if self.cuenta_atras == 0:
                self.temporizador_nivel += 1
                self.player.estado = EstadoPlayer.ATERRIZANDO
                self.lista_planetas[self.nivel].estado = EstadoPlaneta.MUESTRATE

                if self.temporizador_nivel == LIMITE_TIEMPO_ANIMACION_CAMBIO_NIVEL:
                    self.nivel += 1
                    self.paso_nivel(self.nivel)
                    self.cuenta_atras = TIEMPO_DURACION_NIVEL
                    self.temporizador_nivel = 0
                    self.player.estado = EstadoPlayer.NAVEGANDO
                    
                elif self.temporizador_nivel > 1000:
                    self.lista_planetas[self.nivel].estado = EstadoPlaneta.ESCONDETE
                    self.player.estado = EstadoPlayer.DESPEGANDO

            if self.nivel == 3 and self.cuenta_atras == 0:
                self.player.estado = EstadoPlayer.ATERRIZANDO
                self.lista_planetas[self.nivel].estado = EstadoPlaneta.FIN
                if self.temporizador_nivel > 1500:
                    si_pierdes = 1
                    game_over = True
                    self.reset()

            # UPDATES -------------------------------------------------------------------------------------------------------------------
            self.grupo_marcadores.update()
            self.player.update(dt)
            self.grupo_asteroides.update(self.puntos)
            self.grupo_explosion.update(dt)
            self.lista_planetas[self.nivel].update()

            # PUNTUACION ----------------------------------------------------------------------------------------------------------------
            if self.player.estado == EstadoPlayer.NAVEGANDO:
                for self.asteroide in self.grupo_asteroides:
                    if self.asteroide.rect.right < 3:
                        self.puntos += 1
            
            # RENDERIZADO ------------------------------------------------------------------------------------------------------------
            x_relativa = self.x % self.background.get_rect().width
            self.pantalla.blit(self.background, (x_relativa - self.background.get_rect().width , 0))
            if x_relativa < ANCHO:
                self.pantalla.blit(self.background, (x_relativa, 0))
            self.x -= 0.3 # Velocidad movimiento background
            
            self.grupo_asteroides.draw(self.pantalla)
            self.grupo_explosion.draw(self.pantalla)
            self.lista_planetas[self.nivel].draw(self.pantalla)
            if self.explosion.estado == EstadoExplosion.OFF and self.vidas != 0:
                self.player.draw(self.pantalla)

            self.grupo_marcadores.draw(self.pantalla)

            if self.nivel == 3 and self.temporizador_nivel > 1100:
                self.pantalla.blit(self.texto, ((ANCHO - self.anchoTexto)//2, 500))

            pg.display.flip()
        
        return si_pierdes, usuario


class Records(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla) 
        self.background = pg.image.load("resources/images/bg_records.png")
        fuente = pg.font.Font("resources/fonts/nasalization-rg.otf", 50)
        fuente2 = pg.font.Font("resources/fonts/nasalization-rg.otf", 80)
        fuente3 = pg.font.Font("resources/fonts/nasalization-rg.otf", 30)
        fuente4 = pg.font.Font("resources/fonts/nasalization-rg.otf", 50)

        self.texto = fuente.render("PULSA <SPC> PARA VOLVER AL INICIO", True, (255, 255, 255))
        self.anchoTexto = self.texto.get_width()

        
        self.texto1 = fuente2.render("RECORDS", True, (255, 255, 255))
        self.anchoTexto1 = self.texto1.get_width()

        self.texto_records1 = fuente3.render("1er CLASIFICADO - XXX PTOS", True, (255, 255, 255))
        self.anchoTextoRecords1 = self.texto_records1.get_width()

        self.texto_records2 = fuente3.render("2º CLASIFICADO - XXX PTOS", True, (255, 255, 255))
        self.anchoTextoRecords2 = self.texto_records2.get_width()

        self.texto_records3 = fuente3.render("3er CLASIFICADO - XXX PTOS", True, (255, 255, 255))
        self.anchoTextoRecords3 = self.texto_records3.get_width()



    def bucle_principal(self, si_pierdes, usuario):
        print("soy records")
        si_pierdes = 2
        game_over = False
        while not game_over:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    exit()

                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_SPACE:
                        game_over = True

            self.pantalla.blit(self.background, (0, 0))

            self.pantalla.blit(self.texto, ((ANCHO - self.anchoTexto)//2, 650))
            self.pantalla.blit(self.texto1, ((ANCHO - self.anchoTexto1)//2, 100))

            self.pantalla.blit(self.texto_records1, ((ANCHO - self.anchoTextoRecords1)//2, 300))
            self.pantalla.blit(self.texto_records2, ((ANCHO - self.anchoTextoRecords2)//2, 350))
            self.pantalla.blit(self.texto_records3, ((ANCHO - self.anchoTextoRecords3)//2, 400))

            pg.display.flip()

        return si_pierdes, usuario
