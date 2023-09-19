import time

def burbuja(arr):
    n = len(arr)
    start_time = time.time()
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    end_time = time.time()
    print(f"Tiempo de ejecución del Método Burbuja: {end_time - start_time:.6f} segundos")
    print("Lista ordenada usando Método Burbuja:", arr)

def burbujaOpt(arr):
    n = len(arr)
    start_time = time.time()
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    end_time = time.time()
    print(f"Tiempo de ejecución del Método Burbuja Optimizada: {end_time - start_time:.6f} segundos")
    print("Lista ordenada usando Método Burbuja Optimizada:", arr)

def main():
    print("Seleccione el método de ordenamiento:")
    print("1. Método Burbuja")
    print("2. Método Burbuja Optimizada")
    choice = int(input("eliga la opción "))

    if choice not in [1, 2]:
        print("Selección no válida. Por favor, elija 1 o 2.")
        return

    n = int(input("Ingrese el tamaño de la lista: "))
    arr = []
    for i in range(n):
        element = int(input(f"Ingrese el elemento {i+1}: "))
        arr.append(element)

    if choice == 1:
        burbuja(arr)
    else:
        burbujaOpt(arr)

if __name__ == "__main__":
    main()

