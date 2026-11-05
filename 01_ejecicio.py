dia = ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo")


def leer_ventas(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(
                int(input(f"Ingrese la venta del producto {i + 1} el {dia[j]}: "))
            )
        matriz.append(fila)
    return matriz


def leer_precio(filas):
    precios = []
    for fila in range(filas):
        precios.append(int(input(f"Ingrese precio del producto {fila + 1}: ")))
    return precios


def ingresos_semanal_productos(ventas, precios):
    filas = len(ventas)
    columnas = len(ventas[0])
    lista_total = []
    for i in range(filas):
        suma = 0
        for j in range(columnas):
            suma += ventas[i][j] * precios[i]
        lista_total.append(suma)
    return lista_total


def ingreso_total_diarios(ventas, precios):
    filas = len(ventas)
    columnas = len(ventas[0])
    lista_dias = []
    for i in range(columnas):
        suma = 0
        for j in range(filas):
            suma += ventas[j][i] * precios[j]
        lista_dias.append(suma)
    return lista_dias


lista_precios = leer_precio(5)
matriz_ventas = leer_ventas(5, 7)

total_semanal = ingresos_semanal_productos(matriz_ventas, lista_precios)
max_total = max(total_semanal)
producto_max = total_semanal.index(max_total) + 1
print(
    f"El producto {producto_max} es el que más ingresos genera en la semana con ${max_total:,}"
)

total_diario = ingreso_total_diarios(matriz_ventas, lista_precios)
max_diario = max(total_diario)
dia_max = dia[total_diario.index(max_diario)]
print(f"El día con mayores ingresos es el {dia_max} con ${max_diario:,}")
