# En modelo3.py

ventas = []

def registrar_venta(venta_info):
    ventas.append(venta_info)

def resumen_ventas():
    total_ventas = sum(venta["monto"] for venta in ventas)
    total_productos_vendidos = sum(venta["cantidad"] for venta in ventas)
    return f"Total de ventas: ${total_ventas:.2f}\nTotal de productos vendidos: {total_productos_vendidos}"
