import math

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
