
def fibonacci(n):
    fib_sequence = [0, 1]

    if n <= 1:
        return fib_sequence[:n + 1]

    for i in range(2, n + 1):
        next_number = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_number)

    return fib_sequence

# Número de términos de la serie que deseas generar
n = int(input("Ingrese la cantidad de términos de la serie de Fibonacci que deseas generar: "))

if n < 0:
    print("Por favor, ingresa un número no negativo.")
else:
    result = fibonacci(n)
    print("La serie de Fibonacci con {} términos es: {}".format(n, result))

