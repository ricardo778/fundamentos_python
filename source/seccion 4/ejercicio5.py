vida_ac = 0
vida_max = 0
#defino las variables para la vida del personaje
print("Ingrese la vida maxima del personaje:")
vida_max = int(input())
#pido la vida maxima del personaje
print("Ingrese la vida actual del personaje:")
vida_ac = int(input())
#pido la vida actual del personaje
vida_restante = vida_max - vida_ac
print("La vida restante del personaje es de:", vida_restante)
#calculo la vida restante del personaje