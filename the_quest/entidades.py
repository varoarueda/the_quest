import pygame as pg
from pygame import surface
from pygame.sprite import Sprite
from . import ALTO, ALTO_NAVE, ANCHO, ANCHO_NAVE, FPS, VELOCIDAD_PLANETA, CENTRO_PANTALLA, VELOCIDAD_NAVE
import random
from enum import Enum


class EstadoPlayer(Enum):
    NAVEGANDO = 0
    EXPLOTANDO = 1
    ATERRIZANDO = 2
    DESPEGANDO = 3
    
class Nave(Sprite):
    disfraces = ["nave1.png", "nave2.png", "nave3.png", "nave4.png", "nave5.png"]
    def __init__(self, estado, **kwargs): # **kwargs = Al instanciar, hay que meterle los pares clave/valor que me interesen = posicionamiento (x,y)
        super().__init__()
        self.imagenes = [] # Imagen animada
        for fichero in self.disfraces:
            self.imagenes.append(pg.image.load(f"resources/images/{fichero}"))

        self.imagen_activa = 0
        self.tiempo_transcurrido = 0
        self.tiempo_cambio_animacion = 1000 // FPS * 8 # Multiplicador velocidad animación

        self.velocidad_x = VELOCIDAD_NAVE
        self.velocidad_y = VELOCIDAD_NAVE

        self.image = self.imagenes[self.imagen_activa]
        self.rect = self.image.get_rect(**kwargs) # **kwargs permite clave-valor(posicion rect, valor) para posicionar el rect al instanciar Nave

        self.nivel = 0
        self.rotate = 0
        self.flip_y = 0
        self.flip_x = 0
        self.estado = EstadoPlayer.NAVEGANDO
        self.posicion_inicial = kwargs


    def update(self, dt):
        if self.estado == EstadoPlayer.NAVEGANDO:
            if pg.key.get_pressed()[pg.K_UP]:
                self.rect.y -= VELOCIDAD_NAVE
            if pg.key.get_pressed()[pg.K_DOWN]:
                self.rect.y += VELOCIDAD_NAVE

            if self.rect.bottom >= ALTO: 
                self.rect.bottom = ALTO
            if self.rect.top <= 0: 
                self.rect.top = 0 

            self.tiempo_transcurrido += dt # Velocidad animacion
            if self.tiempo_transcurrido >= self.tiempo_cambio_animacion:
                self.imagen_activa += 1 #Animacion disfraz
                if self.imagen_activa >= len(self.imagenes):
                    self.imagen_activa = 0
                self.tiempo_transcurrido = 0
                self.image = self.imagenes[self.imagen_activa]
            return self.rect.midleft
        

        if self.estado == EstadoPlayer.ATERRIZANDO:

            # MOVIMIENTO
            if self.rect.y < (ALTO//2):
                self.rect.y += 1
            elif self.rect.y > (ALTO//2):
                self.rect.y -= 1

            if self.rect.x < (ANCHO - (ANCHO//3)):
                self.rect.x += 1

            # ROTACION
            if self.rect.x > (ANCHO//2):
                if self.rotate > -180:
                    self.rotate -= 1
                    self.flip_y = 180

            # ESCALADO
            if self.rect.x == 800:
                if self.rect.w > 0:
                    self.rect.w -= 3
                if self.rect.h > 0:
                    self.rect.h -= 1

            # ANIMACION DISFRAZ
            self.tiempo_transcurrido += dt # Velocidad animacion
            if self.tiempo_transcurrido >= self.tiempo_cambio_animacion:
                self.imagen_activa += 1 #Animacion disfraz
                if self.imagen_activa >= len(self.imagenes):
                    self.imagen_activa = 0
                self.tiempo_transcurrido = 0
                self.image = self.imagenes[self.imagen_activa]
            return self.rect.midleft

        if self.estado == EstadoPlayer.DESPEGANDO:
            # ESCALADO
            if self.rect.x <= 800:
                self.rect.w += 3
                if self.rect.w > ANCHO_NAVE:
                    self.rect.w = ANCHO_NAVE
                self.rect.h += 1
                if self.rect.h > ALTO_NAVE:
                    self.rect.h = ALTO_NAVE

            # MOVIMIENTO
            if self.rect.x > 0:
                self.rotate = 0
                self.flip_x = 0
                self.flip_y = 0
                self.rect.x -= 1
                self.nivel += 1

            # ANIMACION DISFRAZ
            self.tiempo_transcurrido += dt # Velocidad animacion
            if self.tiempo_transcurrido >= self.tiempo_cambio_animacion:
                self.imagen_activa += 1 #Animacion disfraz
                if self.imagen_activa >= len(self.imagenes):
                    self.imagen_activa = 0
                self.tiempo_transcurrido = 0
                self.image = self.imagenes[self.imagen_activa]
            return self.rect.midleft

    def reset(self):
        self.rect = self.image.get_rect(**self.posicion_inicial)
        self.rotate = 0
        self.flip_y = 0 
        self.flip_x = 0 
        self.estado = EstadoPlayer.NAVEGANDO


    def draw(self, pantalla):
        image = pg.transform.rotate(self.image, self.rotate)
        image = pg.transform.flip(image, self.flip_x, self.flip_y)
        image = pg.transform.scale(image, (self.rect.w , self.rect.h))
        pantalla.blit(image, self.rect)


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class EstadoExplosion(Enum):
    ON = 1
    OFF = 2

class Explosion(Sprite):
    disfraces = ["explosion01.png", "explosion02.png", "explosion03.png", "explosion04.png", "explosion05.png", "explosion06.png", "explosion07.png","explosion08.png"]
    def __init__(self, x, y, estado, contador):
        super().__init__()
        self.x = x
        self.y = y
        self.imagenes = []
        for fichero in self.disfraces:
            self.imagenes.append(pg.image.load(f"resources/images/explosion/{fichero}"))
        
        self.imagen_activa = 0
        self.tiempo_transcurrido = 0
        self.tiempo_cambio_animacion = 1000 // FPS * 10 # Multiplicador velocidad animación

        self.image = self.imagenes[self.imagen_activa]
        self.rect = self.image.get_rect(x=self.x, y=self.y)

        self.estado = EstadoExplosion.OFF
        self.contador = 0
        self.colision = True        

    def update(self, dt):
        if self.estado == EstadoExplosion.ON:
            self.tiempo_transcurrido += dt
            if self.tiempo_transcurrido >= self.tiempo_cambio_animacion:
                self.imagen_activa += 1
                if self.imagen_activa >= len(self.imagenes):
                    self.imagen_activa = 0
                self.tiempo_transcurrido = 0
                self.image = self.imagenes[self.imagen_activa]

        if self.estado == EstadoExplosion.OFF:
            self.image = pg.image.load("resources/images/vacio.png")

    def play(self):
        if self.estado == EstadoExplosion.ON:
            pg.mixer.music.play(0)



#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class EstadoAsteroide(Enum):
    ON = 1
    OFF= 2

class Asteroide(Sprite):
    disfraces = ["asteroide1.png", "asteroide2.png", "asteroide3.png", "asteroide4.png", "asteroide5.png", "asteroide6.png", "asteroide7.png", "asteroide8.png"]
    def __init__(self, velocidad, **kwargs):
        super().__init__()
        self.imagen_aleatoria = random.randrange(7)
        if self.imagen_aleatoria == 0:
            self.image = pg.image.load(f"resources/images/{self.disfraces[0]}")
        if self.imagen_aleatoria == 1:
            self.image = pg.image.load(f"resources/images/{self.disfraces[1]}")
        if self.imagen_aleatoria == 2:
            self.image = pg.image.load(f"resources/images/{self.disfraces[2]}")
        if self.imagen_aleatoria == 3:
            self.image = pg.image.load(f"resources/images/{self.disfraces[3]}")
        if self.imagen_aleatoria == 4:
            self.image = pg.image.load(f"resources/images/{self.disfraces[4]}")
        if self.imagen_aleatoria == 5:
            self.image = pg.image.load(f"resources/images/{self.disfraces[5]}")
        if self.imagen_aleatoria == 6:
            self.image = pg.image.load(f"resources/images/{self.disfraces[6]}")
        if self.imagen_aleatoria == 7:
            self.image = pg.image.load(f"resources/images/{self.disfraces[7]}")
        self.rect = self.image.get_rect(**kwargs)
        self.velocidad_x = random.randrange(3, velocidad + 5)
        self.estado = EstadoAsteroide.ON
        self.contador = 0
        self.puntos = 1


    def update(self, puntos):
        self.rect.x -= self.velocidad_x
        if self.rect.right < 0:
            puntos += self.puntos
            self.rect.center = (random.randrange(ANCHO+50, ANCHO+100), random.randrange(40, ALTO-40))
            self.velocidad_x = random.randrange(3, 5)


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class EstadoPlaneta(Enum):
    MUESTRATE = 1
    ESCONDETE = 2
    FIN = 3

class Planeta(Sprite):
    def __init__(self, estado, disfraz,**kwargs):
        super().__init__()
        self.image = pg.image.load(f"resources/images/planeta{disfraz}.png").convert_alpha()
        self.rect = self.image.get_rect(**kwargs)
        self.velocidad_x = VELOCIDAD_PLANETA
        self.estado = estado
        self.posicion_inicial = kwargs
    
    def update(self):
        if self.estado == EstadoPlaneta.MUESTRATE:
            self.rect.x -= VELOCIDAD_PLANETA
            if self.rect.midleft <= CENTRO_PANTALLA:
                self.rect.midleft = CENTRO_PANTALLA

        if self.estado == EstadoPlaneta.ESCONDETE:
            self.rect.x += VELOCIDAD_PLANETA
            if self.rect.midleft >= (ANCHO - 10, ALTO//2):
                self.rect.midleft = (ANCHO - 10, ALTO//2)

        if self.estado == EstadoPlaneta.FIN:
            self.rect.x -= VELOCIDAD_PLANETA
            if self.rect.center <= CENTRO_PANTALLA:
                self.rect.center = CENTRO_PANTALLA

    def reset(self):
        self.rect = self.image.get_rect(**self.posicion_inicial)
        self.estado = EstadoPlaneta.ESCONDETE


    def draw(self, pantalla):
        pantalla.blit(self.image, self.rect)


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


class Marcadores(Sprite):
    def __init__(self, x, y, fichero_letra, size, color):
        super().__init__()
        self._texto = ""
        self.x = x
        self.y = y
        self.color = color
        self.fuente = pg.font.Font(f"resources/fonts/{fichero_letra}", size)
        self.image = self.fuente.render(self._texto, True, self.color)
        self.rect = self.image.get_rect(x=self.x, y=self.y) 


    def update(self):
        self.image = self.fuente.render(self._texto, True, self.color)
        self.rect = self.image.get_rect(x=self.x, y=self.y) 

    @property
    def texto(self):
        return self._texto
    
    @texto.setter
    def texto(self, valor):
        self._texto = str(valor)


class Marcador_derecha(Marcadores):
    def update(self):
        super().update()
        self.rect = self.image.get_rect(right = self.x, y=self.y)











