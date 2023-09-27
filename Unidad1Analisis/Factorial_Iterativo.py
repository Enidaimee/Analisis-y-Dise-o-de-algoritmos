def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

n = int(input("Ingrese un número para calcular su factorial: "))

resultado = factorial(n)
print("El factorial de {} es: {}".format(n, resultado))
