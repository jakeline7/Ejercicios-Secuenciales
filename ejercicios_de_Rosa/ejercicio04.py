import os
os.system("cls")

    
estatura_pies = float(input("ingrese  estatura en pies: "))
estatura_pulgadas = float(input("Ingrese  estatura en pulgadas: "))




pies_metros = estatura_pies * (1.0 / 3.28084)
pulgadas_metros = estatura_pulgadas * (1.0 / 39.3701)
estatura_metros = pies_metros + pulgadas_metros  


print( f"La estatura en metros sería: {estatura_metros: .2f} m")