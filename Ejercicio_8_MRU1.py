# -------------------------------------------------------------------------
#
# 11/03/2024
# Versión: 1.0
# Autor: Daniel José Iriarte Vargas
#
# Programa que calcula la aceleración y el promedio
# constante de una partícula 
#
# -------------------------------------------------------------------------

# Captura de Datos

velocidadInicial = float(input("Por favor introduce la Velocidad Inicial de la particula en m/seg: "))
velocidadFinal = float(input("Por favor introduce la Velocidad Final de la particula en m/seg: "))
tiempoInicial = int(input("Por favor introduce el Tiempo Inicial de la particula en seg: "))
tiempoFinal = int(input("Por favor introduce el Tiempo Final de la particula en seg: "))

# Procesos 

aceleracionPromedio = float((velocidadFinal - velocidadInicial) / (tiempoFinal - tiempoInicial))
tiempo = int((tiempoFinal - tiempoInicial))
aceleracionConstante = float((velocidadFinal - velocidadInicial) / tiempo)

# Salidas / mostrar Resultados

print(f"La Aceleracion Promedio de la particula es: {round(aceleracionPromedio,2)} m/seg2")
print(f"La Aceleracion Constante de la particula es: {round(aceleracionConstante,2)} m/seg2")