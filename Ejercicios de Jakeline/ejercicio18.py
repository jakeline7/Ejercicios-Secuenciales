#En una tienda han puesto en oferta la venta de todos sus artículos por cambio de estación
#ofreciendo un 15% + 15% de descuento.
#El primer 15% se aplica al importe de la compra,
#mientras que el segundo 15% se aplica al importe que resulta de 
#restar el importe de la compra menos el primer descuento.
#Dada la cantidad de unidades adquiridas de un mismo tipo de artículo por parte de un cliente y el precio unitario del artículo.
#Desarrolle el programa que determine el importe de la compra, el descuento y el importe a pagar.

precio_articulo= int(input("Ingrese el precio unitario del artículo: "))
cantidad_articulo= int(input("Ingrese la cantidad total del artículo: "))
importe_compra= precio_articulo * cantidad_articulo

descuento1= (importe_compra*15)/100
importe_nuevo= importe_compra - descuento1
descuento2= (importe_nuevo*15)/100
descuento_total= descuento1 + descuento2

importe_pago= importe_compra - descuento_total

print("Importe total de compra: ", importe_compra)
print("Descuento total: ", descuento_total)
print("Importe a pagar: ", importe_pago )