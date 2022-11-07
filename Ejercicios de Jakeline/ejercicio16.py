#El cálculo del pago mensual de un empleado de una empresa se efectúa de la siguiente manera:
#el sueldo básico se calcula sobre la base del número total de horas trabajadas basado en una tarifa horaria, 
#al sueldo básico, se le aplica una bonificación del 20% obteniéndose el sueldo bruto;
#al sueldo bruto, se le aplica un descuento del 10% obteniéndose el sueldo neto.
#Desarolle el programa que muestre el sueldo básico, bruto y neto de un trabajador.

horas= int(input("Ingrese la cantidad de horas trabajadas: "))
tarifaporhora= 40

basico= horas*tarifaporhora
bonificacion= (basico*20)/100
bruto= basico + bonificacion
descuento= (bruto*10)/100
neto= bruto - descuento

print("Sueldo básico: ", basico)
print("Sueldo bruto: ", bruto)
print("Sueldo neto: ", neto)