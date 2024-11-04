from centros import *

def test_leer_centros(datos):
    print("Mostrando el primero:", datos[0], sep = "\n")
    print("Mostrando el último:",datos[-1], sep = "\n")
    
def test_calcular_total_camas_centros_accesibles(datos):
    print(f"El número de camas total en los centros accesibles es de {calcular_total_camas_centros_accesibles(datos)}")

if __name__ == '__main__':
    datos = leer_centros('data/centrosSanitarios.csv')
    test_leer_centros(datos)
    test_calcular_total_camas_centros_accesibles(datos)