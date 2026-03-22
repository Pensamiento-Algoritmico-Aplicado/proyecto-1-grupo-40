import sys
import csv
from typing import List, Dict, Set, Tuple

#Definios Variables iniciales como Tareas, Recursos y los resultados

class Tarea:
    def __init__(self, id_t: str, duracion: int, categorias: str):
        self.id = id_t
        self.duracion = duracion
        self.categoria = categoria

class Recurso:
    def __init__(self, id.r: str, categoria_enlazada: Set[str]):
        self.id = id_r
        self.categoria = categoria_enlazada
        self.tiempo_dispo = 0

class Resultados:
    def __init__(self, tarea_id: str, recurso_id: str, inicio: int, fin; int):
        self.tarea_id = tarea_id
        self:recurso_id = recurso_id
        self.inicio = inicio
        self.fin = fin


    

