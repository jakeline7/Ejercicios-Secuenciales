#Dado un número que expresa el tiempo en segundos
#desarrolle el programa que exprese dicho tiempo como la cantidad de
#días, horas, minutos y segundos contenidos en ese número.

segundos= int(input("Escriba la cantidad de segundos: "))

dias = segundos // (24*60*60)
segundos = segundos % (24*60*60)
horas = segundos // (60*60)
segundos = segundos % (60*60)
minutos = segundos // 60
segundos = segundos % 60

print("Días: {} - Horas: {} - Minutos: {} - Segundos: {}".format(dias, horas, minutos, segundos))
