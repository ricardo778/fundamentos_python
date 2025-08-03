distancia = 0
tiempo = 0
# Defino las variables para la distancia y el tiempo
print("Ingrese la distancia recorrida en kilómetros:")
distancia = float(input())
# Pido la distancia recorrida
print("Ingrese el tiempo tomado en horas:")
tiempo = float(input())
# Pido el tiempo tomado

velocidad_promedio = distancia / tiempo
# Calculo la velocidad promedio

print("La velocidad promedio del vehículo es:", round(velocidad_promedio, 2), "km/h")
# Muestro el resultado redondeado a dos decimales