import os
os.system("cls")

gigabyte =float(input("Capacidad del disco duro en GB: "))



byte = gigabyte * 1024 * 1024 * 1024
megabyte = gigabyte * 1024
kilobyte = gigabyte * 1024 * 1024



print( f"MEGABYTES: {megabyte: .2f} MG")
print( f"KILOBYTES: {kilobyte: .2f} KG")
print( f"BYTES: {byte: .2f} B")