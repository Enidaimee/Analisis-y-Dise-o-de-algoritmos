##cantidad de términos de la serie de Fibonacci que deseamos generar.
def fibonacci(n):
    ##Inicialización de la secuencia de Fibonacci
    fib_sequence = [0, 1]

    if n <= 1:
        return fib_sequence[:n + 1]

    for i in range(2, n + 1):
        next_number = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_number)

    return fib_sequence

## Número de términos de la serie quese desea generar
n = int(input("Ingrese la cantidad de términos de la serie de Fibonacci que deseas generar: "))

result = fibonacci(n)
print("La serie de Fibonacci con {} términos es: {}".format(n, result))