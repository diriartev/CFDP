# -------------------------------------------------------------------------
#
# 11/03/2024
# Versión: 1.0
# Autor: Daniel José Iriarte Vargas
#
# Programa que calcula el tiempo en MRU
#
# -------------------------------------------------------------------------

# Captura de Datos

velocidadInicial = float(input("Por favor introduzca la Velocidad Inicial en km/h: "))
velocidadFinal = float(input("Por favor introduzca la Velocidad Final en km/h: "))
aceleracion = float(input("Por favor introduzca la Aceleracion en m/seg2: "))

# Procesos

velocidadIMS = (velocidadInicial * 1000) / 3600
velocidadFMS = (velocidadFinal * 1000) / 3600
tiempo = (velocidadFMS - velocidadIMS) / aceleracion

# Salidas / Mostrar Resultados

print(f"El tiempo que tarda en desacelerar o acelerar es de {round(tiempo , 2)} segundos")