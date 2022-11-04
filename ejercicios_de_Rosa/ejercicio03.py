import os
os.system("cls")
#desarrolle el programa que determine la longitud total recorrida en metros y en yardas

    
t1_km = float(input("ingrese la longitud en km del tramo 1: "))
t2_pies = float(input("ingrese la longitud en pies del tramo 2: "))
t3_millas = float(input("ingrese la longitud en millass del tramo 3: "))


    
t1_m = t1_km * 1000
t2_m = t2_pies / 3.281
t3_m = t3_millas * 1609

    
totalmetros = t1_m + t2_m + t3_m
totalyardas = totalmetros * 1.094


print( f"Longitud total en metros:  {totalmetros:.2f} m")
print( f"Longitud total en yardas:  {totalyardas:.2f}  yd")