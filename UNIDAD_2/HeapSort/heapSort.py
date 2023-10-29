import random
import time 
import matplotlib.pyplot as plt

def heapify(datos, n, i):
    mas_grande = i
    izq = 2 * i + 1
    der = 2 * i + 2
    if izq < n and datos[izq] > datos[mas_grande]:
        mas_grande = izq

    if der < n and datos[der] > datos[mas_grande]:
     mas_grande = der

    if mas_grande != i:
     datos[i], datos[mas_grande] = datos [mas_grande], datos[i]

    heapify(datos, n, mas_grande)

def heapsort(datos):
   n = len(datos)
   for i in range(n//2-1, -1, -1):
      heapify(datos, n, i) 
    

   for i in range(n-1, 0, -1):
      datos[i],datos[0] = datos[0], datos[i]
      heapify(datos, n, 0)

def medir_tiempo():
   tam = [100, 1000, 10000,100000]
   tiempos = []

   for n in tam:
      datos = [random.randint(1, 1000) for i in range(n)]
      inicio = time.time()
      heapsort(datos)
      fin = time.time()
      ejecucion = fin -inicio
      tiempos.append(ejecucion)
   return tam, tiempos


def graficar(tam, tiempos):
   plt.figure(figsize=(8, 6))
   plt.plot(tam,tiempos, marker='0')
   plt.title("compeljidad de Heapsort")
   plt.xlabel("Entrada")
   plt.ylabel("Tiempo de ejecucion")
   plt.grid(True) 



   
   plt.show()

if __name__ == '__main__':
    tam, tiempos = medir_tiempo()
    graficar(tam, tiempos)
