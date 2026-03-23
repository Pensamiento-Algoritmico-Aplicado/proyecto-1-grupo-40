import sys
import csv
from typing import List, Dict, Set, Tuple

# Definimos Variables iniciales como Tareas, Recursos y los resultados

class Tarea:
    def __init__(self, id_t: str, duracion: int, categoria: str):
        self.id = id_t
        self.duracion = duracion
        self.categoria = categoria

class Recurso:
    def __init__(self, id_r: str, categoria_enlazada: Set[str]):
        self.id = id_r
        self.categoria = categoria_enlazada
        self.tiempo_disponible = 0

class Resultados:
    def __init__(self, tarea_id: str, recurso_id: str, inicio: int, fin: int):
        self.tarea_id = tarea_id
        self.recurso_id = recurso_id
        self.inicio = inicio
        self.fin = fin

class Base:
    def __init__(self, tareas: List[Tarea], recursos: List[Recurso]):
        self.tareas = tareas
        self.recursos = recursos
        self.cronograma: List[Resultados] = []

    # Definimos la variable que ordena las tareas en orden de duracion descendiente (O*n*ln(n))
    def ejecutar_lpt(self) -> None:
        tareas_ordenadas = sorted(self.tareas, key=lambda t: t.duracion, reverse=True)
        for tarea in tareas_ordenadas:
            compatibles = [r for r in self.recursos if tarea.categoria in r.categoria]

            recurso_elegido = min(compatibles, key=lambda r: r.tiempo_disponible)

            inicio = recurso_elegido.tiempo_disponible

            fin = inicio + tarea.duracion

            self.cronograma.append(Resultados(tarea.id, recurso_elegido.id, inicio, fin ))

            recurso_elegido.tiempo_disponible = fin

    def guardar_output(self) -> None:
        # Realiza la salida del archivo de forma output.txt con formato CSV
        with open('output.txt', 'w', encoding='utf-8', newline='') as f:
            escritor = csv.writer(f)
            for a in self.cronograma:
                escritor.writerow([a.tarea_id, a.recurso_id, a.inicio, a.fin])

# Definimos variables para leer y cargar "tareas.txt" y "recursos.txt"

def cargar_datos() -> Tuple[List[Tarea], List[Recurso]]:
    tareas: List[Tarea] = []
    recursos: List[Recurso] = []
    with open('tareas.txt', 'r', encoding='utf-8') as f:
        lector = csv.reader(f)
        for fila in lector:
            if fila:
                tareas.append(Tarea(fila[0].strip(), int(fila[1].strip()), fila[2].strip()))
    
    with open('recursos.txt', 'r', encoding='utf-8') as f:
        lector = csv.reader(f)
        for fila in lector:
            if fila:
                enlace = set(c.strip() for c in fila[1:])
                recursos.append(Recurso(fila[0].strip(), enlace))
    
    return tareas, recursos

# Ejecutar algoritmo y mostrar resultados

def main() -> None:
    if len(sys.argv) < 2:
        print("Uso: python main.py <makespan_objetivo>")
        return
    
    objetivo = float(sys.argv[1])

    lista_tareas, lista_recursos = cargar_datos()
    motor = Base(lista_tareas, lista_recursos)
    motor.ejecutar_lpt()
    motor.guardar_output()

    mk_final = max(a.fin for a in motor.cronograma)
    print(f"Makespan Obtenido: {mk_final} (Objetivo: {objetivo})")

if __name__ == "__main__":
    main()








    

