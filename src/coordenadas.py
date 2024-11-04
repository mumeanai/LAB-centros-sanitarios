from collections import namedtuple
import math

Coordenadas = namedtuple('Coordenadas', 'latitud, longitud')

def calcular_distancia(c1, c2):
    '''
    recibe dos coordenadas de tipo Coordenadas(float, float) 
    devuelve un float que representa la distancia euclídea 
    entre esas dos coordenadas.
    '''
    return math.sqrt((c1.latitud-c2.latitud)**2 + (c1.longitud-c2.longitud)**2)

def calcular_media_coordenadas(coordenadas):
    '''
    recibe una lista de Coordenadas(float, float) y devuelve 
    una tupla de tipo Coordenadas(float, float) cuya latitud es 
    la media de las latitudes de la lista y cuya longitud es la 
    media de las longitudes de la lista.
    '''
    contador = 0
    total_latitudes = 0
    total_longitudes = 0
    
    for c in coordenadas:
        contador +=1
        total_latitudes += c.latitud
        total_longitudes += c.longitud
    
    return Coordenadas(total_latitudes/contador, total_longitudes/contador)
