def factorial(n):
    if( n== 0):
        return 1
    else:
        return n * factorial(n-1)
n = int(input("\nIngresa el Numero: "))
print("El factorial de: " + str(n) + " Es: " + str (factorial(n)))
