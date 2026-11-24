# PROBLEMA 3: CONTROL DE INVENTARIO

# 1. Crear la matriz de inventario.
# Cada ariculo contiene: codigo, nombre, stock actual, stock minimo.

inventario = [
    ["A001", "Teclado", 8, 15],
    ["A002", "Mouse", 20, 10],
    ["A003", "Monitor", 3, 8],
    ["A004", "Impresora", 5, 12],
    ["A005", "Disco Duro SSD", 10, 18]
]

# 2. Funcion para calcular la cantidad a solicitar.

def calcular_cantidad_pedido(stock_actual, stock_minimo):

    if stock_actual < stock_minimo:
        cantidad = stock_minimo - stock_actual
    else:
        cantidad = 0

    return cantidad

# 3. Recorrer la matriz y mostar los resultados.

print("=====CONTROL DE INVENTARIO=====")
print("LISTA DE ARTICULOS Y CANTIDADES A SOLICITAR")
print("=================================")

for articulo in inventario:

    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    cantidad_pedido = calcular_cantidad_pedido(stock_actual, stock_minimo)

    print(nombre, ":", cantidad_pedido, "unidades a solicitar. ")

print("=================================")
print("Proceso finalizado.") 