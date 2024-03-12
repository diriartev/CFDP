# -------------------------------------------------------------------------
#
# 11/03/2024
# Versión: 1.0
# Autor: Daniel José Iriarte Vargas
#
# Programa que calcula el desplazamiento de un ciclista
#
# -------------------------------------------------------------------------

# Captura de Datos

velocidadInicial = float(input("Por favor introduzca la Velocidad Inicial en km/h: "))
tiempoInicial = int(input("Por favor introduzca el Tiempo Inicial en segundos: "))
tiempoFinal = int(input("Por favor introduzca el Tiempo Final en segundos: "))
aceleracion = float(input("Por favor introduzca la Aceleracion en m/seg2: "))

# Procesos

velocidadMS = float((velocidadInicial * 1000) / 3600)
distancia =  float((velocidadMS * (tiempoFinal - tiempoInicial)) + ((1 / 2) * aceleracion * ((tiempoFinal - tiempoInicial) ** 2)))

# Salidas / Mostrar Resultados

print(f"El desplazamiento (distancia recorrida) del ciclista es de {round(distancia , 2)} metros")