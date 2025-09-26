# Práctico 3: Estructuras Condicionales

#Alumno: Centurion Bartlett Juan Rodolfo

#1) Mayoria de edad
edad = int(input("Ingrese su edad: ")) 
if edad > 18:
    print("Es mayor de edad") 
else:
    print("No es mayor de edad") 


#2) Nota aprobada
nota = float(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")


#3) Número par
numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

#4) Categoría por edad
edad_categoria = int(input("Ingrese su edad: "))
if edad_categoria < 12:
    print("Niño/a")
elif edad_categoria >= 12 and edad_categoria < 18:
    print("Adolescente")
elif edad_categoria >= 18 and edad_categoria < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

#5) Contraseña válida
contraseña = input("Ingrese una contraseña (8-14 caracteres): ")
longitud = len(contraseña)

if 8 <= longitud <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#6) Sesgo estadístico
import random
from statistics import mode, median, mean

#Generar lista aleatoria de 50 números entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for i in range (50)]

#Calcular parámetros estadísticos
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

print(f"Lista de números: {numeros_aleatorios}")
print(f"Moda: {moda}, Mediana: {mediana}, Media: {media}")

#Determinar el tipo de sesgo
if media > mediana > moda:
    print("Sesgo positivo (a la derecha)")
elif media < mediana < moda:
    print("sesgo negativo (a la izquierda)")
else:
    print("Sin sesgo")

#7) Frase que termina en vocal
frase = input("Ingrese una frase o palabra: ")
vocales = "aeiouAEIOU"

if frase[-1] in vocales:
    frase += "!" #Añade signo de exclamación
print(frase)


#8) Transformación del nombre
nombre = input ("Ingrese su nombre: ")
opcion = input("Ingrese 1 (mayúsculas), 2 (minúsculas) o 3 (primera letra mayúscula): ")

if opcion == "1":
    print(nombre.upper()) #Todo en mayúsculas
elif opcion == "2":
    print(nombre.lower()) #Todo en minúsculas
elif opcion == "3":
    print(nombre.title()) #Primera letra de cada palabra en mayúscula
else:
    print("Opción no válida")

#9) Clasificación de terremoto
magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif 3 <= magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif 4 <= magnitud < 5:
    print("Moderado (sentido, pero no causa daños)")
elif 5 <= magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif 6 <= magnitud < 7:
    print("Muy fuerte (puede causar daños signidicativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")

#10) Estaciones del año
dia = int(input("Ingrese el día (1-31): "))
mes = int(input("Ingrese el mes (1-12): "))
hemisferio = input("Ingrese su hemisferio (N/S): ").upper()

#Determinar estacion
if (mes == 12 and dia >= 21) or (mes in [1,2]) or (mes == 3 and dia <= 20):
    estacion = "Invierno" if hemisferio == "N" else "Verano"
elif (mes == 3 and dia >= 21) or (mes in [4,5]) or (mes == 6 and dia <= 20):
    estacion = "Primavera" if hemisferio == "N" else "Otoño"
elif (mes == 6 and dia >= 21) or (mes in [7,8]) or (mes ==9 and dia <= 20):
    estacion = "Verano" if hemisferio == "N" else "Invierno"
else:
    estacion = "Otoño" if hemisferio == "N" else "Primavera"

print(f"Estación correspondiente: {estacion}")