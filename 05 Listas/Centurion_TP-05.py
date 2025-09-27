#Practico 5: Listas

#Alumno: Centurion Bartlett Juan Rodolfo


#1) Lista de notas de 10 estudiantes
notas = [7.5, 8.0, 6.5, 9.0, 10, 5.5, 7.0, 8.5, 9.5, 6.0]

print("Notas:", notas)

promedio = sum(notas) / len(notas)

print("Promedio:", promedio)

print("Nota más alta:", max(notas))
print("Nota más baja:", min(notas))


#2) Lista de productos
productos = []

for i in range(5):
    productos.append(input(f"Ingrese producto {i+1}: "))

    print("Productos ordenados:", sorted(productos))

eliminar = input("¿Qué producto desea eliminar? ")

if eliminar in productos:
    productos.remove(eliminar)

print("Lista actualizada", productos)


#3) Lista de 15 números aleatorios
import random

numeros = [random.randint(1, 100) for _ in range(15)]
pares = [n for n in numeros if n % 2 == 0]
impares = [n for n in numeros if n % 2 != 0]

print("Numeros:", numeros)
print("Pares:", pares, "Cantidad:", len(pares))
print("Impares:", impares, "Cantidad:", len(impares))

#4) Lista sin elementos repetidos
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]

datos_sin_repetidos = list(set(datos))

print("Original:", datos)
print("Sin repetidos:", datos_sin_repetidos)


#5) Lista de estudiantes presentes
estudiantes = ["Ana", "Pedro" , "María", "Lucas" , "Sofía", "Juan", "Gabriel", "Martín"]
accion = input("¿Desea agregar o eliminar un estudiante? (agregar/eliminar): ").lower()

if accion == "agregar":
    nuevo = input("Ingrese el mombre del estudiante: ")
    estudiantes.append(nuevo)
elif accion == "eliminar":
    eliminar = input("Ingrese el nombre del estudiante que desea eliminar: ")
    if eliminar in estudiantes:
        estudiantes.remove(eliminar)

print("Lista final de estudiantes: ", estudiantes)


#6) Lista con 7 números a rotar
numeros = [1, 2, 3, 4, 5, 6, 7]

ultima = numeros.pop()

numeros.insert(0, ultima)

print("Lista rotada", numeros)


#7) Matriz 7x2
temperaturas = [
    [12, 26],
    [11, 29],
    [14, 27],
    [10, 20],
    [13, 22],
    [11, 22],
    [14, 30]
]

minimas = [t[0] for t in temperaturas]
maximas = [t[1] for t in temperaturas]

print("Proimedio mínimas:", sum(minimas)/len(minimas))
print("Promedio máximas:", sum(maximas)/len(maximas))

amplitud = [maximas[i] - minimas[i] for i in range(7)]
dia_mayor_amplitud = amplitud.index(max(amplitud)) + 1

print("Dia com mayor amplitud térmica:", dia_mayor_amplitud)


#8)Matiz 5x3
notas = [
    [6, 7, 8],
    [6, 8, 9],
    [7, 7, 9],
    [9, 8, 9],
    [8, 8, 9],
]

for i, estudiante in enumerate(notas, start=1):
    print(f"Promedio estudiante {i}:", sum(estudiante)/len(estudiante))

for j in range(3):
    materia = [notas[i][j] for i in range(5)]
    print(f"Promedio materia {j+1}:", sum(materia)/len(materia))


#9) Tablero de Ta-Te-Ti
tablero = [["-" for _ in range(3)] for _ in range(3)]

for turno in range(5):
    fila = int(input("Fila (0-2): "))
    columna = int(input("Columna (0-2): "))
    jugador = "X" if turno % 2 == 0 else "O"
    if tablero[fila][columna] == "-":
        tablero[fila][columna] = jugador
    
    for fila_tab in tablero:
        print(fila_tab)


#10) Ventas de tienda
ventas = [
    [8, 10, 12, 10, 11, 5, 7],
    [5, 6, 5, 10, 15, 8, 9],
    [15, 14, 13, 12, 11, 10, 9],
    [8, 9, 10, 11, 12, 13, 14]
]

for i, producto in enumerate(ventas, start=1):
    print(f"Total de producto {i}:", sum(producto))

totales_dia = [sum(ventas[j][i] for j in range(4)) for i in range(7)]
print("Dia con mayores ventas:", totales_dia.index(max(totales_dia)) + 1)

totales_prod = [sum(p) for p in ventas]
print("Producto mas vendido:", totales_prod.index(max(totales_prod)) + 1)