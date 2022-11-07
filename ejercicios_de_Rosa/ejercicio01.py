import os
os.system("cls")
#desarrolle el programa que determine el porcentaje de varones y mujeres que hay en un salon
mujeres = float(input("ingresa la cantidad de mujeres: "))
hombres = float(input("ingresa la cantidad de hombres: "))

total_estudiantes = mujeres + hombres
porcentajemujeres = mujeres * 100 // total_estudiantes
porcentajehombres = hombres * 100 // total_estudiantes

print( f" total de estudiantes :  {total_estudiantes:.2f}")
print( f" porcentaje de mujeres en un salón de clases  :  {porcentajemujeres:.2f} %")
print( f" porcentaje de varones del salón de clases  : {porcentajehombres:.2f} %")