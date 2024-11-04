from coordenadas import *

def test_calcular_distancia(c1,c2):
    print(f"La distancia entre las coordenadas es de {calcular_distancia(c1,c2)}")

def test_calcular_media_coordenadas(coordenadas):
    print("La media de todas las coordenadas es:", calcular_media_coordenadas(coordenadas))

if __name__ == "__main__":
    lista_coordenadas =[
        Coordenadas(1.0, 2.0),
        Coordenadas(2.3, 4,2),
        Coordenadas(3.5, 6.4)
    ]
    
    test_calcular_distancia(Coordenadas(1.0, 2.0), Coordenadas(2.3, 4,2))
    test_calcular_media_coordenadas(lista_coordenadas)
'''    
def test_calcular_distancia(c1, c2):
    print("Probando calcular_distancia")
    distancia = calcular_distancia(c1, c2)
    print(f"La distancia entre {c1} y {c2} es {distancia}")
 
def test_calcular_media_coordenadas(lista_coordenadas):
    print("Probando calcular_media_coordenadas")
    media = calcular_media_coordenadas(lista_coordenadas)
    print(f"La media de la lista de coordednas es {media}")
 
if __name__ == "__main__":
    lista_coordenadas = [
        Coordenadas(1.0, 2.5), 
        Coordenadas(0.1, 5.0),
        Coordenadas(2.2, 3.5),
        Coordenadas(9.4, 5.0),
    ]
    test_calcular_distancia(lista_coordenadas[0], lista_coordenadas[1])
    test_calcular_media_coordenadas(lista_coordenadas)
'''