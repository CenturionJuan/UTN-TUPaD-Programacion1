#Actividad de cierre unidad 1 - Estructuras Secuenciales
#Alumno: Centurion Bartlett Juan Rodolfo

#Actividades:
# 1)
print("Hola Mundo!")

# 2)
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

# 3)
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# 4)
radio = float(input("Ingrese el radio del círculo: "))
area = 3.1416 * radio ** 2
perimetro = 2 * 3.1416 * radio
print(f"Área: {area}")
print(f"Perímetro: {perimetro}")

# 5)
segundos = int(input("Ingrese una cantidad de segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas} horas")

# 6)
num = int(input("Ingrese un número: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# 7)
a = int(input("Ingrese el primer número (distinto de 0): "))
b = int(input("Ingrese el segundo número (distinto de 0): "))
print(f"Suma: {a + b}")
print(f"Resta: {a - b}")
print(f"Multiplicación: {a * b}")
print(f"División: {a / b}")

# 8)
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso / (altura ** 2)
print(f"Su IMC es: {imc}")

# 9)
celsius = float(input("Ingrese la temperatura en °C: "))
fahrenheit = (9 / 5) * celsius + 32
print(f"{celsius} °C equivalen a {fahrenheit} °F")

# 10)
n1 = float(input("Ingrese el primer número: "))
n2 = float(input("Ingrese el segundo número: "))
n3 = float(input("Ingrese el tercer número: "))
promedio = (n1 + n2 + n3) / 3
print(f"El promedio es: {promedio}")
