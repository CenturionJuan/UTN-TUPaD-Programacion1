#Practico 4: Estructuras Repetitivas

#Alumno: Centurión Bartlett Juan Rodolfo

#1) Números del 0 al 100
for i in range(101):
    print(i)

#2) Cantidad de dígitos
numero = int(input("Ingrese un número entero: "))
contador = 0

for digito in str(abs(numero)): #Convierto a string para contar dígitos
    contador += 1

print(f"Cantidad de dígitos: {contador}")

#3) Suma de dos valores sin contar los mismos
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

suma = sum(range(min(a,b)+1, max(a,b))) #Rango excluyendo extremos

print(f"Suma de los números entre {a} y {b} (excluyendo extremos): {suma}")

#4) Suma secuencial hasta el 0
total = 0
while True:
    n = int(input("Ingrese un número (0 para terminar)"))
    if n == 0:
        break
    total += n
print(f"Suma acumulada: {total}")

#5) Juego de adivinar un número
import random

numero_secreto = random.randint(0, 9)
intentos = 0

while True:
    intento = int(input("Adivine el número entre 0 y 9: "))
    intentos += 1
    if intento == numero_secreto:
        print(f"Correcto. Intentos necesarios: {intentos}")
        break

#6) Numeros pares entre 0 y 100
for i in range(100, -1, -2):
    print(i)

#7) Suma de números hasta n
n = int(input("Ingrese un número entero positivo: "))

suma = sum(range(n+1))

print(f"Suma de todos los números enteros de 0 a {n}: {suma}")

#8) Contador de pares, impares, positivos y negativos
pares = impares = positivos = negativos = 0

for _ in range(100):
    num = int(input("Ingrese un número entero: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1

print(f"Pares: {pares}, Impares: {impares}, Positivos: {positivos}, Negativos: {negativos}")

#9) Calcular media de 100 números
suma_total = 0

for _ in range(100):
    num = int(input("Ingrese un número entero: "))
    suma_total += num

media = suma_total / 100

print(f"Media de los 100 números: {media}")

#10) Invertir dígitos de un número
numero = input("Ingrese un número entero: ")
numero_invertido = numero[::-1] 

print(f"Número invertido: {numero_invertido}")