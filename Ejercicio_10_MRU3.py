# -------------------------------------------------------------------------
#
# 11/03/2024
# Versión: 1.0
# Autor: Daniel José Iriarte Vargas
#
# Programa que calcula la aceleración o desaceleración
#
# -------------------------------------------------------------------------

# Captura de Datos

velocidadInicial = float(input("Por favor introduzca la Velocidad Inicial en km/h: "))
velocidadFinal = float(input("Por favor introduzca la Velocidad Final en km/h: "))
tiempo = int(input("Por favor introduzca el Tiempo en segundos: "))

# Procesos

velocidadIMS = (velocidadInicial * 1000) / 3600
velocidadFMS = (velocidadFinal * 1000) / 3600
aceleracion = (velocidadFMS - velocidadIMS) / tiempo

# Salidas / Mostrar Resultados

print(f"'La distancia recorrida es de {round(aceleracion , 2)} m/seg2'")