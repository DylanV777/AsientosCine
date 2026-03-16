# #Sala de cine

filas = 8
columnas = 10

sala = []

for f in range(1, filas + 1):
    fila = []
    for c in range(columnas):
        fila.append("O")  
    sala.append(fila)


print("        PANTALLA")
print("   ===================")


print("   ", end="")
for c in range(1, columnas+1):
    print(c, end=" ")
print()

for f in range(filas):
    print(f+1, end="  ")  
    for c in range(columnas):
        print(sala[f][c], end=" ")
    print()

opcion = "si"
print()
while opcion == "si":
    fila = int(input("Ingrese la fila"))
    columna = int(input("Ingrese la columna"))

    if sala[fila-1][columna-1] == "O":
        sala[fila-1][columna-1] = "X"
        print()
        print("Asiento reservado con exito")
        print()
    else:
        print()
        print("Asiento ocupado, elija uno disponible")
        print()

    print("  ", end="")
    for c in range(1, columnas + 1):
        print(c, end=" ")
    print()
    
    for f in range (1, filas + 1):
        print(f, end = " ")
        for c in range(columnas):
            print(sala[f-1][c], end = " ")
        print()

    opcion = input("¿Desea reservar otro asiento? si/no")

