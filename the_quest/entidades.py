import pygame as pg
from pygame.sprite import Sprite
from . import ALTO, ANCHO, FPS
import random

class Nave(Sprite):
    disfraces = ["nave1.png", "nave2.png", "nave3.png", "nave4.png", "nave5.png"]
    def __init__(self, **kwargs): # **kwargs = Al instanciar, hay que meterle los pares clave/valor que me interesen = posicionamiento (x,y)
        self.imagenes = [] # Imagen animada
        for fichero in self.disfraces:
            self.imagenes.append(pg.image.load(f"resources/images/{fichero}"))
        self.imagen_activa = 0

        self.tiempo_transcurrido = 0
        self.tiempo_cambio_animacion = 1000 // FPS * 8

        self.image = self.imagenes[self.imagen_activa]
        self.rect = self.image.get_rect(**kwargs) # **kwargs permite clave-valor(posicion rect, valor) para posicionar el rect al instanciar Nave

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


