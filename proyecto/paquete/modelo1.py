# En modelo1.py

def registrar_producto():
    producto = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad en stock: "))
    return {"producto": producto, "precio": precio, "cantidad": cantidad}
