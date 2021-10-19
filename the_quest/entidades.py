import pygame as pg
from pygame.sprite import Sprite
from . import ALTO, ANCHO, FPS
import random

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

        self.image = self.imagenes[self.imagen_activa]
        self.rect = self.image.get_rect(**kwargs) # **kwargs permite clave-valor(posicion rect, valor) para posicionar el rect al instanciar Nave
        self.estado = estado

    def update(self, dt):
        if pg.key.get_pressed()[pg.K_UP]:
            self.rect.y -= 5
        if pg.key.get_pressed()[pg.K_DOWN]:
            self.rect.y += 5

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

        return self.rect.center
    '''
    def explota(self, dt):
        animacion = ["explosion01.png", "explosion02.png", "explosion03.png", "explosion04.png", "explosion05.png", "explosion06.png", "explosion07.png", "explosion08.png"]
        self.imagenes = []
        for fichero in animacion:
            self.imagenes.append(pg.image.load(f"resources/images/explosion/{fichero}"))
        self.imagen_activa = 0
        self.image = self.imagenes[self.imagen_activa]

    def reset_estado(self, dt):
        self.estado = True

    def reset_nave(self, dt):
        disfraces = ["nave1.png", "nave2.png", "nave3.png", "nave4.png", "nave5.png"]
        self.imagenes = []
        for fichero in disfraces:
            self.imagenes.append(pg.image.load(f"resources/images/{fichero}"))
        self.imagen_activa = 0
        self.image = self.imagenes[self.imagen_activa]
    ''' 


class Explosion(Sprite):
    disfraces = ["explosion01.png", "explosion02.png", "explosion03.png", "explosion04.png", "explosion05.png", "explosion06.png", "explosion07.png","explosion08.png"]
    def __init__(self, x, y, estado):
        super().__init__()
        self.x = x
        self.y = y
        self.imagenes = []
        for fichero in self.disfraces:
            self.imagenes.append(pg.image.load(f"resources/images/explosion/{fichero}"))
        
        self.imagen_activa = 0
        self.tiempo_transcurrido = 0
        self.tiempo_cambio_animacion = 1000 // FPS * 8 # Multiplicador velocidad animación

        self.image = self.imagenes[self.imagen_activa]
        self.rect = self.image.get_rect(x=self.x, y=self.y)

        self.estado = False

    def update(self, dt):
        self.tiempo_transcurrido += dt
        if self.tiempo_transcurrido >= self.tiempo_cambio_animacion:
            self.imagen_activa += 1
            if self.imagen_activa >= len(self.imagenes):
                self.imagen_activa = 0
            self.tiempo_transcurrido = 0

            self.image = self.imagenes[self.imagen_activa]





class Asteroide(Sprite):
    disfraces = ["asteroide1.png", "asteroide2.png", "asteroide3.png", "asteroide4.png", "asteroide5.png", "asteroide6.png", "asteroide7.png", "asteroide8.png"]
    def __init__(self, **kwargs):
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
        self.velocidad_x = random.randrange(5, 8)
        
    


    def update(self, dt):
        self.rect.x -= self.velocidad_x
        if self.rect.right < 0:
            self.rect.center = (random.randrange(ANCHO+50, ANCHO+100), random.randrange(40, ALTO-40))
            self.velocidad_x = random.randrange(7, 9)





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

    def update(self, dt):
        self.image = self.fuente.render(self._texto, True, self.color)
        self.rect = self.image.get_rect(x=self.x, y=self.y) 

    @property
    def texto(self):
        return self._texto
    
    @texto.setter
    def texto(self, valor):
        self._texto = str(valor)





