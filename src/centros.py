from collections import namedtuple
import csv
from coordenadas import *

CentroSanitario = namedtuple('CentroSanitario', 'nombre, localidad, coordenadas, estado, num_camas, acceso_minusvalidos, tiene_uci')

def leer_centros(ruta):
    '''
    recibe la ruta de un fichero CSV codificado en UTF-8, y devuelve 
    una lista de tuplas de tipo 
    CentroSanitario(str, str, Coordenadas(float, float), str, int, bool, bool) 
    conteniendo todos los datos almacenados en el fichero.
    '''
    with open(ruta, encoding = 'utf-8') as f: 
        lector = csv.reader(f, delimiter = ";")
        next(lector)
        
        res = []
        
        for nombre, localidad, latitud , longitud, estado, num_camas, acceso_minusvalidos, tiene_uci in lector:
            latitud = float(latitud)
            longitud = float(longitud)
            coordenadas = Coordenadas(latitud, longitud)
            
            num_camas = int(num_camas)
            acceso_minusvalidos = acceso_minusvalidos.strip() == "true"
            tiene_uci = tiene_uci.strip() == "true"
            #elimina los posibles espacios
            
            tupla = CentroSanitario(nombre, localidad, coordenadas, estado, num_camas, acceso_minusvalidos, tiene_uci)
            res.append(tupla)
        return res
            
    
    
def calcular_total_camas_centros_accesibles(centros):
    '''
    recibe una lista de tuplas de tipo CentroSanitario y produce 
    como salida un entero correspondiente al número total de camas 
    de los centros sanitarios accesibles para discapacitados.
    '''
    camas_centros_accesibles = 0
    for c in centros:
        if c.acceso_minusvalidos:
            camas_centros_accesibles += c.num_camas
    return camas_centros_accesibles
            

def obtener_centros_con_uci_cercanos_a(centros, coordenadas, umbral_distancia):
    '''
    recibe una lista de tuplas de tipo CentroSanitario; 
    una tupla de tipo Coordenadas, que representa un punto; 
    y un float, que representa un umbral de distancia. 
    Produce como salida una lista de tuplas (str, str, Coordenadas(float, float)) 
    con el nombre, del centro, la localidad y las coordenadas 
    de los centros con uci situados a una distancia de las coordenadas
    dadas como parámetro menor o igual que el umbral dado.
    '''
    res = []
    for c in centros:
        if c.uci and coordenadas.calcular_distacia():
    
    

def generar_mapa():
    pass