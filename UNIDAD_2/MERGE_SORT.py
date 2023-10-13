#Dividir el arreglo en mitades 
def merge_sort(arreglo):
    #Caso Base
    #verificar que el arreglo tiene un  solo elemento el arreglo
    if len(arreglo) <= 1:
        return arreglo
    #DIVIDIR
    #Obtener la mitad
    mitad = len(arreglo)//2 #doble diagonal = rendondear el resultado
    izq = arreglo[:mitad] #desde el inicio del arrgelo HASTA la mitad
    der = arreglo[mitad:] #desde la mitad HASTA el final
    #CONQUISTAR
    #llamada recursiva
    izq = merge_sort(izq)
    der = merge_sort(der)

    #COMBINAR
    #funsionar las soluciones recur
    return merge(izq, der)

def merge(izq, der):
    ordenado = []
    i_izq, i_der = 0, 0
    #Ciclo para comparar los elementos
    while i_izq < len(izq) and i_der < len(der):
        if izq[i_izq] < der[i_der]:
            ordenado.append(izq[i_izq]) #añadir al final del arreglo 
            i_izq += 1   
        else:
            ordenado.append(der[i_der])
            i_der += 1 #se el suma un 1 adicional 
            #agregar todos los elementos restantes,si existen
    ordenado.extend(izq[i_izq:]) #hace mas grande una lista pegando la otra
    ordenado.extend(der[i_der:])
    return ordenado
 #metodo para ejecutar el programa       
if __name__ ==  '__main__':
    arreglo = [4, 2, 3, 1, 5, 7, 6, 8, 9]
    print('Arreglo desrdenado: ', arreglo)
    ordenado = merge_sort(arreglo)
    print('Arreglo Ordenado: ',ordenado)