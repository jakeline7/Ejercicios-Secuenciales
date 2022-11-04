import os
os.system ("cls")

base = float(input("Ingrese el largo del rectángulo: "))
altura = float(input("Ingrese el ancho del rectángulo: "))


area = base * altura 
perimetro = 2 * (base + altura )


print(f"Área: {area: .2f} metros cudrados" )
print(f"Perímetro: {perimetro: .2f} metros")