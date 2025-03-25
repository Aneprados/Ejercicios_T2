import math
from Estrellas import Estrella


def distancia(self, otra_estrella):
    return math.sqrt((self.x - otra_estrella.x)**2 + (self.y - otra_estrella.y)**2 + (self.z - otra_estrella.z)**2)

def galaxia(estrella):
    x, y, z = estrella.x, estrella.y, estrella.z
    if x >= 0 and y >= 0 and z >= 0:
        return "Galaxia A"
    elif x < 0 and y >= 0 and z >= 0:
        return "Galaxia B"
    else:
        return "Galaxia C"
    
def encontrar_estrella_mas_lejana(estrella):
    x, y, z = estrella.x, estrella.y, estrella.z
    distancia_origen = math.sqrt((x - 0)**2 + (y - 0)**2 + (z - 0)**2)
    return distancia_origen

def imprimir_estrella(estrella_A, estrella_B, estrella_C):
    print(f"Estrella A: {estrella_A}")
    print(f"Estrella B: {estrella_B}")
    print(f"Estrella C: {estrella_C}")

def imprimir_galaxia(estrella_A, estrella_B, estrella_C): 
    print(f"Galaxia de la estrella A: {galaxia(estrella_A)}")
    print(f"Galaxia de la estrella B: {galaxia(estrella_B)}")
    print(f"Galaxia de la estrella C: {galaxia(estrella_C)}")

def crear_estrella(x, y, z):
    estrella = Estrella(x, y, z)
    return estrella

def determinar_galaxia(estrella):
    x, y, z = estrella.x, estrella.y, estrella.z
    if x >= 0 and y >= 0 and z >= 0:
        return "Galaxia A"
    elif x < 0 and y >= 0 and z >= 0:
        return "Galaxia B"
    else:
        return "Galaxia C"
    
def calcular_distancia(estrella_A, estrella_B, estrella_C):
    distancia_A_B = estrella_A.distancia(estrella_B)
    distancia_B_C = estrella_B.distancia(estrella_C)
    print(f"Distancia entre A y B: {distancia_A_B}")
    print(f"Distancia entre B y C: {distancia_B_C}")