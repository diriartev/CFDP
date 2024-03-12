# -------------------------------------------------------------------------
#
# 11/03/2024
# Versión: 1.0
# Autor: Daniel José Iriarte Vargas
#
# Programa que calcula un número factorial
#
# -------------------------------------------------------------------------

# Definir Variables

factorial = 1

# Captura de Datos

num = int(input("Por favor introduzca el número al que desea hallarle el factorial: "))

# Procesos

for conCic in range(1 , num + 1):
    factorial = int(factorial * conCic)

# Salidas / Mostrar Resultados
    
print(f"El número factorial de {num} es {factorial}")