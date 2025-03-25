
from Lanzador import crear_estrella, imprimir_estrella, imprimir_galaxia, calcular_distancia, encontrar_estrella_mas_lejana

if __name__ == "__main__":
    estrella_A = crear_estrella(1, 2, 3)
    estrella_B = crear_estrella(-1, 2, 3)
    estrella_C = crear_estrella(1, -2, 3)
    
    imprimir_estrella(estrella_A, estrella_B, estrella_C)
    imprimir_galaxia(estrella_A, estrella_B, estrella_C)
    calcular_distancia(estrella_A, estrella_B, estrella_C)
    estrella_mas_lejana = encontrar_estrella_mas_lejana(estrella_A, estrella_B, estrella_C)
    print(f"La estrella más lejana es: {estrella_mas_lejana}")