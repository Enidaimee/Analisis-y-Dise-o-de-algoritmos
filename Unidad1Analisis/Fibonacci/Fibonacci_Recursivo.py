def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
n=int(input("Ingresa el numero a realizar: "))

for i in range(0,n):
    print("fibonacci: " + str(i+1) + " Es: " + str(fibonacci(i)))
