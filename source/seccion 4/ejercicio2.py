horas = 0
minutos = 0
segundos = 0
#defino las variables para el tiempo jugado
print("ingrese las horas jugadas:")
horas = int(input())
#pido las horas jugadas
print("ingrese los minutos jugados:")
minutos = int(input())
#pido los minutos jugados
print("ingrese los segundos jugados:")
segundos = int(input())
#pido los segundos jugados
tiempoTotal = horas * 3600 + minutos * 60 + segundos
print("El tiempo total jugado en segundos es:", tiempoTotal)
#calculo el tiempo total en segundos