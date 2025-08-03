costo_objeto1 = 0
costo_objeto2 = 0
costo_objeto3 = 0
# Defino las variables para el costo de los objetos
print("Ingrese el costo del primer objeto:")
costo_objeto1 = float(input())
# Pido el costo del primer objeto
print("Ingrese el costo del segundo objeto:")
costo_objeto2 = float(input())
# Pido el costo del segundo objeto
print("Ingrese el costo del tercer objeto:")
costo_objeto3 = float(input())
# Pido el costo del tercer objeto
costo_total = costo_objeto1 + costo_objeto2 + costo_objeto3
print("El costo total de los objetos comprados es:", round(costo_total, 2), "monedas")
# Muestro el costo total redondeado a dos decimales