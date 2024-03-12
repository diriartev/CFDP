# -------------------------------------------------------------------------
#
# 11/03/2024
# Versión: 1.0
# Autor: Daniel José Iriarte Vargas
#
# Programa que lee 3 números y descubre si uno de ellos es la
# suma de los otros 2 
#
# -------------------------------------------------------------------------

# Captura de Datos

num1 = int(input("Por favor introduzca el primer número: "))
num2 = int(input("Por favor introduzca el segundo número: "))
num3 = int(input("Por favor introduzca el tercer número: "))

# Procesos y salidas

if num1 == num2 + num3:
    print(f"El número {num1} es la suma de los otros 2 números ({num2} y {num3})")
elif num2 == num1 + num3:
    print(f"El número {num2} es la suma de los otros 2 números ({num1} y {num3})")
elif num3 == num1 + num2:
    print(f"El número {num3} es la suma de los otros 2 números ({num1} y {num2})")