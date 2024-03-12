# -------------------------------------------------------------------------
#
# 11/03/2024
# Versión: 1.0
# Autor: Daniel José Iriarte Vargas
#
# Programa que lee 4 números y calcula cuál es el mayor de los 4
#
# -------------------------------------------------------------------------

# Captura de Datos

num1 = int(input("Ingrese el primer número por favor: "))
num2 = int(input("Ingrese el segundo número por favor: "))
num3 = int(input("Ingrese el tercer número por favor: "))
num4 = int(input("Ingrese el cuarto número por favor: "))

# Procesos y Salidas de Datos

if num1 > num2 and num1 > num3 and num1 > num4:
    print(f"El numero mayor es {num1}")
elif num2 > num1 and num2 > num3 and num2 > num4:
    print(f"El numero mayor es {num2}")
elif num3 > num1 and num3 > num2 and num3 > num4:
    print(f"El numero mayor es {num3}")
elif num4 > num1 and num4 > num2 and num4 > num3:
    print(f"El numero mayor es {num4}")
else:
    print("Ha habido un error, quizá puso 2 números iguales, vuelva ejecutar el programa por favor")