#1 Precios frutas

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200 
precios_frutas['Manzana'] = 1500 
precios_frutas['Pera'] = 2300

#2 Actualizar precios

precios_frutas['Naranja'] = 1330
precios_frutas['Manzana'] = 1500 
precios_frutas['Melon]'] = 2800

print(precios_frutas)

#3 

lista_frutas = list(precios_frutas.keys())

print(lista_frutas)

#4 numeros telefonicos

agenda_telefonos = {}
num_contactos = 5 

for i in range(num_contactos):
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    numero = input(f"Ingrese el número de {nombre}: ")
    agenda_telefonos[nombre] = numero

nombre_consulta = input("\nIngrese el nombre a consultar: ")

if nombre_consulta in agenda_telefonos:
    numero_asociado = agenda_telefonos[nombre_consulta]
    print(f"El número de {nombre_consulta} es: {numero_asociado}")
else:
    print(f"Contacto '{nombre_consulta}' no encontrado en la agenda.")

#5 frase

frase = input("Ingrese una frase: ").lower()
palabras = frase.split()

palabras_unicas = set(palabras)

recuento_palabras = {}
for palabra in palabras:
    recuento_palabras[palabra] = recuento_palabras.get(palabra, 0) + 1

print(f"Palabras únicas (Set): {palabras_unicas}")
print(f"Recuento (Diccionario): {recuento_palabras}")

#6 tupla de 3 notas

alumnos_notas = {}
num_alumnos = 3

for i in range(num_alumnos):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    
    try:
        nota1 = float(input("Ingrese Nota 1: "))
        nota2 = float(input("Ingrese Nota 2: "))
        nota3 = float(input("Ingrese Nota 3: "))
        
        alumnos_notas[nombre] = (nota1, nota2, nota3)
    except ValueError:
        print("Entrada inválida. Saltando este alumno.")
        continue

print("\nResultados de Promedios")
for nombre, notas in alumnos_notas.items():
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {nombre} es: {promedio:.2f}")

#7 dos set de numeros

aprobados_parcial1 = {"Ana", "Juan", "Sofía", "Luis", "Pedro"}
aprobados_parcial2 = {"Juan", "Pedro", "Martín", "Elena", "Sofía"}

aprobados_ambos = aprobados_parcial1.intersection(aprobados_parcial2)
print(f"Aprobaron AMBOS parciales: {aprobados_ambos}")

aprobados_solo_uno = aprobados_parcial1.symmetric_difference(aprobados_parcial2)
print(f"Aprobaron SOLO UNO: {aprobados_solo_uno}")

aprobados_total = aprobados_parcial1.union(aprobados_parcial2)
print(f"Total que aprobaron AL MENOS UNO: {aprobados_total}")


#8 productos stok

stock_productos = {"lapiz": 100, "cuaderno": 50, "goma": 20}

while True:
    print("\nOpciones")
    print("1. Consultar stock")
    print("2. Agregar/Actualizar unidades")
    print("3. Salir")
    
    opcion = input("Seleccione una opción (1/2/3): ")

    if opcion == '1':
        producto = input("Ingrese el nombre del producto: ").lower()
        cantidad = stock_productos.get(producto, "no existe")
        
        if cantidad != "no existe":
            print(f"Stock de {producto}: {cantidad} unidades.")
        else:
            print(f"El producto '{producto}' no se encuentra en stock.")
    
    elif opcion == '2':
        producto = input("Ingrese el nombre del producto: ").lower()
        
        try:
            unidades = int(input("Ingrese la cantidad de unidades a agregar: "))
            
            if producto in stock_productos:
                stock_productos[producto] += unidades
                print(f"Stock de {producto} actualizado a: {stock_productos[producto]}.")
            else:
                stock_productos[producto] = unidades
                print(f"Nuevo producto '{producto}' agregado con stock: {unidades}.")
        except ValueError:
            print("Cantidad inválida. Debe ser un número entero.")

    elif opcion == '3':
        print("\nStock final:")
        print(stock_productos)
        break
    
    else:
        print("Opción no válida. Intente de nuevo.")

#9 tuplas dia hora

agenda = {
    ("lunes", "10:00"): "Reunión de equipo",
    ("martes", "15:00"): "Clase de inglés",
    ("miércoles", "09:00"): "Entrega de proyecto",
    ("viernes", "14:30"): "Entrenamiento deportivo"
}

dia_consulta = input("Ingrese el día (ej. lunes): ").lower()
hora_consulta = input("Ingrese la hora (ej. 10:00): ")

clave_consulta = (dia_consulta, hora_consulta)

if clave_consulta in agenda:
    evento = agenda[clave_consulta]
    print(f"\nActividad para el {dia_consulta} a las {hora_consulta}: {evento}")
else:
    print(f"\nNo hay actividad programada para el {dia_consulta} a las {hora_consulta}.")

#10 paises y capitales

paises_capitales = {
    "Argentina": "Buenos Aires", 
    "Chile": "Santiago",
    "España": "Madrid",
    "Perú": "Lima"
}

print(f"Original (País: Capital): {paises_capitales}")

capitales_paises = {
    capital: pais 
    for pais, capital in paises_capitales.items()
}

print(f"Invertido (Capital: País): {capitales_paises}")
