import time #libreria para el tiempo


def Suma(a,b):
    return a + b

def Resta (a,b):
    return a - b

def Mult(a,b):
    return a * b

def Div(a,b):
    if b != 0:
        return a / b
    else:
        return "¡Error! No se puede dividir por cero."

while True:
    print("\n")
    print("--------Calculadora-----------")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir")

    opcion = input ("Selecciona una opción del 1-4: ")

    if opcion == "5":
        print("Hasta luego....")
        break
    num1=float(input("Introduce el primer Número: "))
    num2=float(input("Introduce el segundo Número: "))

    inicio = time.time()  # Captura el tiempo de inicio
    res = 0
    for i in range(0,1000):
      res = res + i
    print(res)

    if opcion == "1":
        resultado= Suma(num1, num2)
    elif opcion == "2":
        resultado = Resta(num1, num2)
    elif opcion == "3":
        resultado= Mult(num1, num2)
    elif opcion == "4":
        resultado = Div(num1, num2)
    else:
        print("opcion invalida")
        continue

    fin = time.time()  # Captura el tiempo de finalización

    print("------------------------------")
    print("El resultado es:", resultado)
    print("------------------------------")
    tiempo_ejecutado = fin - inicio  # Calcula el tiempo transcurrido

    print("Tiempo de ejecución:", tiempo_ejecutado, "segundos")