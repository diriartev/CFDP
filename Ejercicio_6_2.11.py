# -------------------------------------------------------------------------
#
# 11/03/2024
# Versión: 1.0
# Autor: Daniel José Iriarte Vargas
#
# Programa que calcula y visuliza la longitud de la circunferencia
# y el área de un círculo de radio dado
#
# -------------------------------------------------------------------------

# Importar Librerias

import math

# Captura de Datos

radio = float(input("Por favor introduzca el radio del círculo: "))

# Procesos

circunferencia = float(2 * math.pi * radio)
area = float(math.pi * (radio ** 2))

# Salidas / Mostrar resultados

print(f"La circunferencia del cículo es {round(circunferencia,2)} y el área es {round(area,2)}")