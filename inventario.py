#Solicitar el nombre del producto
nombre = input("Ingrese el nombre del producto ")
#solicitar la cantidad del producto
cantidad = int(input("Ingrese la cantidad "))
#Validamos la informacion con el ciclo while 
while cantidad <=0:
    #si el numero es menor o igual a 0 entonces se activa el ciclo sino deja ingresar la cantidad
    print("Error, La cantidad no puede ser menor a 0")
    cantidad = int(input("Ingrese la cantidad "))
#Validamos el precio con el ciclo while 
precio = float(input("Ingrese el precio: "))
while precio <=0:
    print("Error, el precio debe ser mayor a 0")
    precio = float(input("Ingrese el precio: "))
#con la variable costo sacamos el precio total del prodcuto multiplicandolo por la cantidad
costo_total = (precio*cantidad)
#imprimimos todos los datos, el nombre , la cantidad , precio y su costo total
print(f"Producto: {nombre} | cantidad: {cantidad} | precio unitario:{precio} | Costo total calculado: {costo_total}")

#Este programa esta diseñado para llevar registro de un producto.

    

