import os
os.system("cls")
#desarrolle el programa que permite comvertir una cantidad dada en metros a su equivalente en centimetros, pulgadas, pies y yardas.
metros = int( input("Ingrese la cantidad de metros : "))

centimetros = metros * 100
pulgadas = centimetros / 2.54
pies = pulgadas / 12
yardas = pies / 3

print( f"Centímetros : {centimetros:.2f}")
print( f"Pulgadas : {pulgadas:.2f}")
print( f"Pies : {pies:.2f}")
print( f"yardas : {yardas:.2f}")