base = 0
multiplicador = 0
# Defino las variables para el daño
print("Ingrese el daño base")
base = float(input())
# Pido el daño base
print("Ingrese el multiplicador de daño")
multiplicador = float(input())
# Pido el multiplicador de daño
danio_total = base * multiplicador
print("El daño critico total es de:", round(danio_total, 2))
# Muestro el daño total redondeado a dos decimales