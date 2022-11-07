#Juan, Rosa y Daniel aportan cantidades de dinero para formar un capital.
#Juan y Rosa aportan en dólares y Daniel, en soles.
#Desarrolle el programa que determine el capital total en dólares 
#y qué pocentaje de dicho capital aporta cada uno.
#Dólares = S/3.00 nuevos soles

juan= int(input("Ingrese cantidad de aportes de Juan: "))
rosa= int(input("Ingrese cantidad de aportes de Rosa: "))
daniel= int(input("Ingrese cantidad de aportes de Daniel: "))

daniel= daniel / 3
total= juan + rosa + daniel

porcentaje1= (juan / total)*100
porcentaje2= (rosa / total)*100
porcentaje3= (daniel / total)*100

print("Cantidad de aportes total: ", total, " dólares")
print("Porcentaje de aportes de Juan: {} % - Rosa: {} % - Daniel: {} %" .format(porcentaje1, porcentaje2, porcentaje3))

