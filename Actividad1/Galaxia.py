from Estrellas import Estrellas

class Galaxia(Estrellas):
    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y, z)
        self.estrella = []

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
    
    def __name__(self):
        return f"Galaxia: {self.x}, {self.y}, {self.z}"
    
    def agregar_estrella(self, estrella):
        self.estrella.append(estrella)
    
    
    
    
    
    
    