
import time 
arreglo = [7, 50 , 0, 5, 9, 2]
x = 7

inicio = time.time()

for i in range (0, len(arreglo)):
    if x == arreglo[i]:
        print('El elemento está en la lista, en la posicion: ',i)
    else:
        print('El elemento no está en la lista')

fin = time.time()    

tiempo_ejecutado = fin - inicio  # Calcula el tiempo transcurrido
print("Tiempo de ejecución:", tiempo_ejecutado)