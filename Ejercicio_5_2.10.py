# -------------------------------------------------------------------------
#
# 11/03/2024
# Versión: 1.0
# Autor: Daniel José Iriarte Vargas
#
# Programa que que calcula la superficie de un triángulo
#
# -------------------------------------------------------------------------

# Captura de Datos

base = float(input("Por favor introduzca la base del triángulo: "))
altura = float(input("Por favor introduzca la altura del triángulo: "))

# Procesos

superficie = float((base * altura) / 2)

# Salidas

print(f"La superficie del triángulo que ha indicado es {superficie}")