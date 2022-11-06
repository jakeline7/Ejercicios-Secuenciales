import os
os.system("cls")

mujeres = float(input("ingresa la cantidad de mujeres: "))
hombres = float(input("ingresa la cantidad de hombres: "))

cantidadestudiantes = mujeres + hombres
operacion = mujeres * 100
porcentajemujeres = operacion // cantidadestudiantes
porcentajehombres = hombres * 100 // cantidadestudiantes

print( f"el total de estudiantes es :  {cantidadestudiantes:.2f}")
print( f"el porcentaje de mujeres en un salón de clases es :  {porcentajemujeres:.2f} %")
print( f"El porcentaje de varones del salón de clases es : {porcentajehombres:.2f} %")