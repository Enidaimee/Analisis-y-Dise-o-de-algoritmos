import time
import random
import matplotlib.pyplot as plt

def mochila_Fraccionaria(capacidad, objetos):
    objetos.sort(key=lambda x: x[0] / x[1], reverse=True)
    total_objetos = 0.0
    mochila = []
    for valor, peso in objetos:
        if capacidad >= peso:
            mochila.append((valor, peso))
            total_objetos += valor
            capacidad -= peso
        else:
            fracc = capacidad / peso
            mochila.append((valor * fracc, peso * fracc))
            total_objetos += valor * fracc
            break
    return total_objetos, mochila

# Lista para almacenar los tiempos de ejecución
tiempos_ejecucion = []

# Ejecutar la función 10 veces con diferentes conjuntos de datos
for _ in range(10):
    objetos = [(random.randint(1, 10), random.randint(1, 20)) for _ in range(100)]
    capacidad = random.randint(50, 100)

    # Medir el tiempo de ejecución de la función
    start_time = time.time()
    total_objetos, mochila = mochila_Fraccionaria(capacidad, objetos)
    end_time = time.time()

    # Calcular el tiempo de ejecución y agregarlo a la lista
    tiempo_ejecucion = end_time - start_time
    tiempos_ejecucion.append(tiempo_ejecucion)

    print(f'El total de objetos es {total_objetos} y la mochila quedó {mochila}')

# Graficar los tiempos de ejecución
plt.plot(range(1, 11), tiempos_ejecucion, marker='o', linestyle='-', color='b')
plt.xlabel('Caso')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Tiempo de ejecución de la función mochila_Fraccionaria en 10 casos diferentes')
plt.grid(True)
plt.show()
