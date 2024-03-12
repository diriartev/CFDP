# -------------------------------------------------------------------------
#
# 11/03/2024
# Versión: 1.0
# Autor: Daniel José Iriarte Vargas
#
# Programa que calcula el salario y los impuestos de un trabajador 
# en función de las horas trabajadas
#
# -------------------------------------------------------------------------

# Captura de Datos

nombre = input("Por favor introduzca su nombre: ")
horas = int(input("Por favor introduzca el número de horas trabajadas: "))
precioHora = int(input("Por favor introduzca el precio o valor de la hora de trabajo (En USD): "))

# Procesos 

salarioBruto = float(horas * precioHora) 
impuestos = float(salarioBruto * 0.20)
salarioNeto = float(salarioBruto - impuestos)

# Salidas / Mostrar Resultados

print(f"Hola {nombre}, su salario bruto es de {salarioBruto} USD, sus impuestos son de {impuestos} USD y por ende su salario neto es de {salarioNeto} USD")