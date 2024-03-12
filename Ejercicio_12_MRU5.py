# -------------------------------------------------------------------------
#
# 11/03/2024
# Versión: 1.0
# Autor: Daniel José Iriarte Vargas
#
# Programa que calcula la aceleración y la distancia
# de una partícula 
#
# -------------------------------------------------------------------------

# Captura de Datos

velocidadInicial = float(input("Por favor introduce la Velocidad Inicial de la particula en km/h: "))
velocidadFinal = float(input("Por favor introduce la Velocidad Final de la particula en km/h: "))
tiempoInicial = int(input("Por favor introduce el Tiempo Inicial de la particula en horas: "))
tiempoFinal = int(input("Por favor introduce el Tiempo Final de la particula en horas: "))
tiempo = int(input("Por favor introduzca el Tiempo al que desea hallarle la Distancia en horas: "))

# Procesos

aceleracion = float((velocidadFinal - velocidadInicial) / (tiempoFinal - tiempoInicial))
distancia = float((1/2) * (velocidadFinal + velocidadInicial) * (tiempo))

# Salidas / Mostrar Resultados

print(f"La aceleración es de {round(aceleracion , 2)} km/h2")
print(f"La distancia que habra recorrido en {tiempo} horas es de {round(distancia , 2)} km")