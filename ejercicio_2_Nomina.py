# -------------------------------------------------------------------------
#
# 11/03/2024
# Versión: 1.0
# Autor: Daniel José Iriarte Vargas
#
# Programa que calcula la nómina semanal, y salario neto de empelados 
# a los que se les paga por horas
#
# -------------------------------------------------------------------------

# Captura de Datos

nombre = input("Por favor introduzca su nombre: ")
horas = int(input("Por favor introduzca el número de horas trabajadas: "))
tarifa = int(input("Por favor introduzca la tarifa o valor de la hora de trabajo (En USD): "))

# Procesos 

if horas <= 35:
    salariobruto = float(horas * tarifa)
else:
    salariobruto = float((35 * tarifa) + ((horas* 35) * 1.5 * tarifa))

if salariobruto <= 2000:
    impuestos = float(0)
elif salariobruto <= 2200:
    impuestos = float((salariobruto - 2000) * 0.20)
else:
    impuestos = float((220 * 0.20) + ((salariobruto - (2200) * 0.30)))

salarioneto = float(salariobruto - impuestos)

# Salida / Mostrar resultados

print(f"Hola {nombre}, su salario bruto es de {salariobruto} USD, sus impuestos son de {impuestos} USD y por ende su salario neto es de {salarioneto} USD")