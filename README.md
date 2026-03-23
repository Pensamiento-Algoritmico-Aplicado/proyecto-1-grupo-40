# Proyecto 1 - "Sistema de Planificacion"
Grupo 40 - Integrantes:
- Simón Alonso Acosta Yañez
- Raimundo Jose Eduardo Piñeiro Azócar
- Tomás Alberto Sánchez Astudillo

# Descripcion
El proyecto consiste en desarrollar un sistema de planificación de tareas (scheduler), donde se deben asignar distintas tareas a un conjunto de recursos disponibles. Cada tarea tiene una duración y una categoría, y cada recurso solo puede ejecutar tareas de ciertas categorías. El objetivo es construir un cronograma válido sin solapamientos y respetando las compatibilidades que minimice el makespan, es decir, el tiempo total necesario para completar todas las tareas.

# Plan de Estrategia
El código implementa un planificador de tareas que lee datos desde archivos .txt, representa las tareas y recursos mediante clases, y utiliza una heurística LPT (Longest Processing Time) que ordena las tareas de mayor a menor duración, junto a una estrategia greedy para asignar cada tarea al recurso compatible que esté disponible más pronto, asegurando que no haya solapamientos y que se cumplan todas las restricciones. Finalmente, genera un archivo output.txt con el cronograma resultante y calcula el makespan como el tiempo en que termina la última tarea.

# Instrucciones para ejecutar
1. Crear un virtual environment: `python -m venv .venv`
2. Activar: `source .venv/bin/activate`
3. Instalar dependencias: `pip install -r requirements.txt`
4. Ejecutar: `python main.py <makespan_objetivo>`



