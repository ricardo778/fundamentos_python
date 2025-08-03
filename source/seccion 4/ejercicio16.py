enemigos_totales = 0    
enemigos_derrotados = 0
# Defino las variables para el número de enemigos
print("Ingrese el número total de enemigos:")
enemigos_totales = int(input())
# Pido el número total de enemigos
print("Ingrese el número de enemigos derrotados:")
enemigos_derrotados = int(input())
# Pido el número de enemigos derrotados
porcentaje_derrotados = (enemigos_derrotados / enemigos_totales) * 100
print("El porcentaje de enemigos derrotados es:", round(porcentaje_derrotados, 2), "%")
# Muestro el porcentaje de enemigos derrotados redondeado a dos decimales