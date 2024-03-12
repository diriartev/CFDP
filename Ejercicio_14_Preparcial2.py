# -------------------------------------------------------------------------
#
# 11/03/2024
# Versión: 1.0
# Autor: Daniel José Iriarte Vargas
#
# Programa que suma números naturales hasta un número escogido
#
# -------------------------------------------------------------------------

# Definir Variables

num = int()
conCic = int()
sumNum = int()

# Inicializar Variables

num = 0
conCic = 0
sumNum = 0

# Captura de Datos

while True:
    num = int(input('Por favor introduzca un número natural: '))
    if num > 0:
        break

# Procesos aritméticos
    
for conCic in range(1, num + 1):
    sumNum += conCic

# Mostrar Resultado
    
print('La suma de los números naturales hasta', num, 'es', sumNum)