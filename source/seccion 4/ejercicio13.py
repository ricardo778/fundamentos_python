misionesTotales = 0
misionesCompletadas = 0
# Defino las variables para el tiempo total de juego
print("Ingrese el número total de misiones:")
misionesTotales = int(input())
print("Ingrese el número de misiones completadas:")
misionesCompletadas = int(input())
porcentaje_completado = (misionesCompletadas / misionesTotales) * 100
# Calculo el porcentaje de misiones completadas
print("El porcentaje de misiones completadas es:", round(porcentaje_completado, 2), "%")
# Muestro el porcentaje de misiones completadas redondeado a dos decimales