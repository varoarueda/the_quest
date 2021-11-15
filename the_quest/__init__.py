ANCHO = 1200
ALTO = 800
FPS = 60
CENTRO_PANTALLA = (600, 400)

ESCENA = 0

VELOCIDAD_PLANETA = 1
VELOCIDAD_NAVE = 5
ALTO_NAVE = 77
ANCHO_NAVE = 174

NIVEL = 0

TIEMPO_DURACION_NIVEL = 30

LIMITE_TIEMPO_ANIMACION_CAMBIO_NIVEL = 1850
DURACION_EXPLOSION = 60

def musica(cancion):
    LISTA_MUSICA = ['musica_juego'] * 6
    return f"resources/sonidos/{LISTA_MUSICA[cancion]}.ogg"


def sonido(fx):
    LISTA_SONIDOS = ['explosion']
    if fx in LISTA_SONIDOS:
        return f"resources/sonidos/{fx}.ogg"







