#1 Hola mundo
def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()

#2 Saludar Usuario
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

nombre_usuario = input("Por favor, ingresa tu nombre: ")

saludo = saludar_usuario(nombre_usuario)
print(saludo)


#3 Informacion Personal

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
residencia = input("Ingresa tu residencia: ")

informacion_personal(nombre, apellido, edad, residencia)

#4 Calcular circulo

import math

def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

try:
    radio = float(input("Ingresa el radio del círculo: "))
    area = calcular_area_circulo(radio)
    perimetro = calcular_perimetro_circulo(radio)

    print(f"\nResultados para un radio de {radio}:")
    print(f"Área del círculo: {area:.2f}")
    print(f"Perímetro del círculo: {perimetro:.2f}")

except ValueError:
    print("Error: Por favor, ingresa un número válido para el radio.")


#5 Funcion seg a horas

def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas

try:
    segundos = int(input("Ingresa la cantidad de segundos: "))
    horas = segundos_a_horas(segundos)

    print(f"{segundos} segundos equivalen a {horas:.4f} horas.")

except ValueError:
    print("Error: Por favor, ingresa un número entero válido para los segundos.")

#6 Funcion multiplicar

def tabla_multiplicar(numero):
    print(f"\nTabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

try:
    numero_base = int(input("Ingresa un número para ver su tabla de multiplicar: "))
    tabla_multiplicar(numero_base)

except ValueError:
    print("Error: Por favor, ingresa un número entero válido.")

#7 operaciones basicas

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    try:
        division = a / b
    except ZeroDivisionError:
        division = "Indefinido (División por cero)"
    return (suma, resta, multiplicacion, division)

try:
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    resultados = operaciones_basicas(num1, num2)

    print("\nResultados de Operaciones Básicas")
    print(f"Suma: {resultados[0]}")
    print(f"Resta: {resultados[1]}")
    print(f"Multiplicación: {resultados[2]}")
    print(f"División: {resultados[3]}")
    print("---------------------------------------")

except ValueError:
    print("Error: Por favor, ingresa números válidos.")


#8 calcular imc

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

try:
    peso_kg = float(input("Ingresa tu peso en kilogramos (kg): "))
    altura_m = float(input("Ingresa tu altura en metros (m): "))
    if altura_m <= 0:
        print("Error: La altura debe ser un valor positivo.")
    else:
        imc_resultado = calcular_imc(peso_kg, altura_m)
        print(f"\nTu Índice de Masa Corporal (IMC) es: {imc_resultado:.2f}")

except ValueError:
    print("Error: Por favor, ingresa números válidos para peso y altura.")

#9 Celsius a FFahrenheit

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

try:
    temp_celsius = float(input("Ingresa la temperatura en grados Celsius (°C): "))

    temp_fahrenheit = celsius_a_fahrenheit(temp_celsius)

    print(f"\n{temp_celsius}°C equivalen a {temp_fahrenheit:.2f}°F.")

except ValueError:
    print("Error: Por favor, ingresa un número válido para la temperatura.")


#10 Funcion calcular promedio

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

try:
    num_a = float(input("Ingresa el primer número: "))
    num_b = float(input("Ingresa el segundo número: "))
    num_c = float(input("Ingresa el tercer número: "))

    promedio_final = calcular_promedio(num_a, num_b, num_c)

    print(f"\nEl promedio de ({num_a}, {num_b}, {num_c}) es: {promedio_final:.3f}") 

except ValueError:
    print("Error: Por favor, ingresa números válidos.")