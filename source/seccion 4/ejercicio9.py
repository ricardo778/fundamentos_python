tiempo_total = 0
tiempo_transcurrido = 0
# Defino las variables para el tiempo
print("Ingrese el tiempo total de la misión en horas:")
tiempo_total = float(input())
# Pido el tiempo total de la misión
print("Ingrese el tiempo transcurrido en horas:")
tiempo_transcurrido = float(input())
# Pido el tiempo transcurrido
tiempo_restante = tiempo_total - tiempo_transcurrido
print("El tiempo restante para completar la misión es:", round(tiempo_restante, 2), "horas")
# Muestro el tiempo restante redondeado a dos decimales