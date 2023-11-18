# En modelo2.py

def realizar_venta(producto_info, cantidad_vendida):
    producto_info["cantidad"] -= cantidad_vendida
    monto_total = producto_info["precio"] * cantidad_vendida
    return monto_total
