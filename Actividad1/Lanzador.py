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
    


def encontrar_estrella_mas_lejana(estrella_A, estrella_B, estrella_C):
    # Calcular la distancia entre las estrellas
    distancia_A_B = estrella_A.distancia(estrella_B)
    distancia_A_C = estrella_A.distancia(estrella_C)
    distancia_B_C = estrella_B.distancia(estrella_C)

    # Determinar cuál es la estrella más lejana
    if distancia_A_B > distancia_A_C and distancia_A_B > distancia_B_C:
        return estrella_A
    elif distancia_A_C > distancia_A_B and distancia_A_C > distancia_B_C:
        return estrella_A
    else:
        return estrella_C
import math

# Definición de la clase Estrella
class Estrella:
    def __init__(self, nombre, x=0, y=0, z=0):
        self.nombre = nombre
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"{self.nombre}: ({self.x}, {self.y}, {self.z})"
    
    def distancia(self, otra_estrella):
        # Calcula la distancia euclidiana en 3D
        dx = self.x - otra_estrella.x
        dy = self.y - otra_estrella.y
        dz = self.z - otra_estrella.z
        return math.sqrt(dx ** 2 + dy ** 2 + dz ** 2)

# Función para encontrar la estrella más lejana
def encontrar_estrella_mas_lejana(estrella_A, estrella_B, estrella_C):
    # Calcular la distancia entre las estrellas
    distancia_A_B = estrella_A.distancia(estrella_B)
    distancia_A_C = estrella_A.distancia(estrella_C)
    distancia_B_C = estrella_B.distancia(estrella_C)

    # Determinar cuál es la estrella más lejana
    if distancia_A_B > distancia_A_C and distancia_A_B > distancia_B_C:
        return estrella_A
    elif distancia_A_C > distancia_A_B and distancia_A_C > distancia_B_C:
        return estrella_A
    else:
        return estrella_C

# Creación de las estrellas
estrella_A = Estrella("Estrella A", 1, 2, 3)
estrella_B = Estrella("Estrella B", 4, 5, 6)
estrella_C = Estrella("Estrella C", 7, 8, 9)

# Llamar a la función para encontrar la estrella más lejana
estrella_mas_lejana = encontrar_estrella_mas_lejana(estrella_A, estrella_B, estrella_C)

# Imprimir el resultado
print(f"La estrella más lejana es: {estrella_mas_lejana}")


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