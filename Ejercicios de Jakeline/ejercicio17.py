#Una institución social recibe anualmente una donación que reparte de la siguiente forma:
#25% para el centro de salud
#35% en el comedor infantil,
#25%para la escuela infantil,
#y el resto para el asilo de ancianos.
#Desarrolle el programa que muestre los montos asignados.

donacion= int(input("Ingrese el monto de la donación anual: "))

centro= (donacion*25) / 100
comedor= (donacion*35) / 100
escuela= (donacion*25) / 100
asilo= donacion - (centro + comedor + escuela)

print("Monto asignado al centro de salud: ", centro)
print("Monto asignado al comedor infantil: ", comedor)
print("Monto asignado a la escuela infantil: ", escuela)
print("Monto asignado al asilo de ancianos: ", asilo)

