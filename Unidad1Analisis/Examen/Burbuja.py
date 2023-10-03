# Lista de elementos
elementos = [5, 3, 8, 4, 6]

# Método Iterativo
def BurbujaIte(arreglo): # Define una función llamada BurbujaIte que toma una lista arreglo como argumento
    n = len(arreglo) # Calcula la longitud de la lista arreglo y almacena el resultado en la variable n
    for i in range(n - 1): #Inicia un bucle que recorre la lista desde el primer elemento hasta el penúltimo elemento. i representa la posición actual en la lista
        for j in range(n - 1 - i):#nicia otro bucle que recorre la lista desde el primer elemento hasta el último elemento no ordenado en la iteración actual. 
            if arreglo[j] > arreglo[j + 1]:#Compara el elemento actual  con el siguiente elemento
                arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j] #Realiza el intercambio de elementos si es necesario.
#llamada al metdod                
BurbujaIte(elementos)
print ('Metodo iterativo:', elementos) #imprime elementos ordenados

# Método Recursivo

def BurbujaRe(arreglo, n=None): #define funcion igual que la iterativa
    if n is None: # Si n no se proporciona como argumento, se calcula la longitud de la lista arreglo y se asigna a n
        n = len(arreglo)

    # Caso Base: Si la lista está completamente ordenada 
    intercambios_realizados = False
    for i in range(n - 1): #Inicia un bucle que recorre la lista desde el primer elemento hasta el penúltimo elemento
        if arreglo[i] > arreglo[i + 1]: #Compara el elemento actual con el siguiente elemento 
            arreglo[i], arreglo[i + 1] = arreglo[i + 1], arreglo[i] #Realiza el intercambio de elementos
            intercambios_realizados = True #se verifica si se realizaron intercambios 

    if not intercambios_realizados: #Si no se realizaron intercambios, la lista está completamente ordenada y la función retorna
        return
    # Caso General: Llamada recursiva para ordenar el resto de la lista
    BurbujaRe(arreglo, n - 1)

# Llamada al método recursivo
BurbujaRe(elementos)
print('Metodo Recursivo:', elementos)

###notación Big O= O(n^2) algoritmo cuyo tiempo de ejecución aumenta cuadráticamente con el tamaño de la entrada
