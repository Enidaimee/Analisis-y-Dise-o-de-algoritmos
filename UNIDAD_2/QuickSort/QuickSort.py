import random
import time
import matplotlib.pyplot as plt

# Función Quicksort
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        for x in arr[1:]:
            if x < pivot:
                left.append(x)
            else:
                right.append(x)
        return quicksort(left) + [pivot] + quicksort(right)

# Medir el tiempo de ejecución de Quicksort
def measure_time(arr):
    start_time = time.time()
    quicksort(arr)
    end_time = time.time()
    return end_time - start_time

# Crear 100 arreglos de números aleatorios de tamaño aleatorio
test_cases = []
for _ in range(100):
    size = random.randint(1, 10000)  # Tamaño aleatorio del arreglo
    arr = [random.randint(1, 1000) for _ in range(size)]  # Números aleatorios en el arreglo
    test_cases.append(arr)

# Medir el tiempo de ejecución para cada caso de prueba y almacenar los resultados
results = []
execution_times = []  # Lista para almacenar los tiempos de ejecución
for arr in test_cases:
    time_taken = measure_time(arr)
    execution_times.append(time_taken)  # Agregar el tiempo de ejecución a la lista
    results.append((arr, quicksort(arr.copy()), time_taken))

# Ordenar los resultados por tiempo de ejecución
results.sort(key=lambda x: x[2])

# Mostrar los arreglos de los 3 casos de prueba con menor tiempo de ejecución
print("Tres casos con menor tiempo de ejecución:")
for i in range(3):
    original, ordenado, tiempo = results[i]
    print(f"Arreglo Original: {original}")
    print(f"Arreglo Ordenado: {ordenado}")
    print(f"Tiempo de Ejecución: {tiempo} segundos")
    print("------------------------")

# Mostrar los arreglos de los 3 casos de prueba con mayor tiempo de ejecución
print("Tres casos con mayor tiempo de ejecución:")
for i in range(-1, -4, -1):
    original, ordenado, tiempo = results[i]
    print(f"Arreglo Original: {original}")
    print(f"Arreglo Ordenado: {ordenado}")
    print(f"Tiempo de Ejecución: {tiempo} segundos")
    print("------------------------")

# Crear una gráfica dodne muestre los resultados de ejecucion 
plt.figure(figsize=(10, 6))
plt.plot(execution_times, marker='o', linestyle='-', color='pink')  
plt.xlabel('tamaño del arreglo(n)')
plt.ylabel('Tiempo de Ejecución (segundos)')
plt.title(' Quicksort ')
plt.grid(True)
plt.savefig('tiempo_de_ejecucion01.png')  # Guardar la gráfica como una imagen
plt.show()
