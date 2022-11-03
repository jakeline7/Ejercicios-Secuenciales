import os
os.system("cls")


radio = float(input("Ingrese el radio del cilindro: "))
altura = float(input("Ingrese la altura del cilindro: "))

area = 2 * 3.14* radio * (radio + altura) 
volumen = 3.14* ( radio ** 2 ) * altura


print(f"Área Total: {area: .2f} metros cuadrados")
print(f"Volumen: {volumen: .2f} metros cubicos") 
