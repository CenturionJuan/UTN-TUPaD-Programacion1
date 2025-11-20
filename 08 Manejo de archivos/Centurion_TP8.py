import os

NOMBRE_ARCHIVO = "productos.txt"

def crear_archivo_inicial():
    if not os.path.exists(NOMBRE_ARCHIVO):
        with open(NOMBRE_ARCHIVO, "w") as archivo:
            archivo.write("Lapicera,120.5,30\n")
            archivo.write("Cuaderno,350.0,15\n")
            archivo.write("Regla,80.0,40\n")

def obtener_productos_en_memoria():
    productos = []
    
    try:
        with open(NOMBRE_ARCHIVO, "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                
                if len(datos) == 3:
                    nombre, precio, cantidad = datos
                    
                    producto_dict = {
                        "nombre": nombre,
                        "precio": float(precio),
                        "cantidad": int(cantidad)
                    }
                    productos.append(producto_dict)
    
    except FileNotFoundError:
        print(f"Error: El archivo '{NOMBRE_ARCHIVO}' no fue encontrado.")
        
    return productos

def guardar_productos_actualizados(lista_productos):
    print("\nGuardando Cambios")
    
    with open(NOMBRE_ARCHIVO, "w") as archivo:
        for producto in lista_productos:
            linea_a_escribir = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
            archivo.write(linea_a_escribir)
            
    print("El archivo 'productos.txt' ha sido sobrescrito.")


def mostrar_productos(lista_productos):
    print("\n2. Listado de Productos en Memoria")
    if not lista_productos:
        print("No hay productos para mostrar.")
        return
        
    for producto in lista_productos:
        print(f"Producto: {producto['nombre']} | Precio: ${producto['precio']:.2f} | Cantidad: {producto['cantidad']}")

def agregar_producto_a_lista(lista_productos):
    print("\n3. Agregar Nuevo Producto")
    
    nombre = input("Ingrese el nombre del nuevo producto: ")
    
    while True:
        try:
            precio = float(input("Ingrese el precio: "))
            cantidad = int(input("Ingrese la cantidad: "))
            break
        except ValueError:
            print("Entrada inválida. Asegúrese de ingresar números.")

    nuevo_producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    lista_productos.append(nuevo_producto)
    print(f"Producto '{nombre}' agregado a la lista en memoria.")

def buscar_producto(lista_productos):
    print("\n5. Buscar Producto por Nombre")
    
    nombre_busqueda = input("Ingrese el nombre del producto a buscar: ").strip().lower()
    encontrado = False
    
    for producto in lista_productos:
        if producto["nombre"].lower() == nombre_busqueda:
            print(f"\n¡Producto encontrado! Datos:")
            print(f"Nombre: {producto['nombre']}")
            print(f"Precio: ${producto['precio']:.2f}") 
            print(f"Cantidad: {producto['cantidad']}")
            encontrado = True
            break
            
    if not encontrado:
        print(f"\nError: Producto '{nombre_busqueda}' no encontrado.")


if __name__ == "__main__":
    
    crear_archivo_inicial() 
    
    lista_productos = obtener_productos_en_memoria()
    
    mostrar_productos(lista_productos)
    
    agregar_producto_a_lista(lista_productos)
    
    buscar_producto(lista_productos)
    
    guardar_productos_actualizados(lista_productos)
    
    mostrar_productos(obtener_productos_en_memoria())