# -------------------------------------------------------------------------
#
# 11/03/2024
# Versión: 1.0
# Autor: Daniel José Iriarte Vargas
#
# Programa que calcula el capital total acumulado al final de
# un periodo de tiempo específicado
#
# -------------------------------------------------------------------------

# Captura de Datos

capital = int(input("Por favor introduzca la cantidad del capital invertido (en USD): "))
tasainteres = int(input("Por favor introduzca el porcentaje de la tasa de interés (no ponga el signo %): "))
duracion = int(input("Por favor introduzca la duración de la inversión (en semanas): "))

# Procesos

rendimientosemanal = float((capital * (tasainteres / 100)) / 52)
rendimientototal = float(rendimientosemanal * duracion)
capitaltotalacumulado = float(capital + rendimientototal)

# Salida / Mostrar resultados

print(f"El capital total acumulado de la inversión después de las {duracion} semanas es de {round(capitaltotalacumulado,2)} USD")