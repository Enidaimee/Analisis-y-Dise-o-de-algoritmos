import heapq
import time

class Graph:
    def __init__(self):
        self.vertices = {} #almacenar los vértices y sus aristas con pesos
    
    def add_vertex(self, vertex):
        self.vertices[vertex] = {}  #Inicializamos las aristas del vértice
    
    def add_edge(self, start, end, weight):
        self.vertices[start][end] = weight #Añadimos una arista con su peso al vértice de inicio

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph.vertices}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph.vertices[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# grafo de ejemplo
grafo = Graph()
vertices = ['A', 'B', 'C', 'D', 'E']
for v in vertices:
    grafo.add_vertex(v)

aristas = [('A', 'B', 5), ('A', 'C', 3), ('B', 'D', 3), ('C', 'D', 1), ('D', 'E', 7)]
for arista in aristas:
    grafo.add_edge(*arista)

# medir el tiempo de ejecución
def measure_execution_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time

# Encontrar caminos mínimos desde un vértice de inicio dado
start_vertex = 'A'
resultado, tiempo_ejecucion = measure_execution_time(dijkstra, grafo, start_vertex)

# Imprimir resultados
print(f"Caminos mínimos desde {start_vertex}: {resultado}")
print(f"Tiempo de ejecución: {tiempo_ejecucion} segundos")
