import sys

sys.setrecursionlimit(2000)

# 1) Factorial de un Número y su Serie

def factorial_recursivo(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursivo(n - 1)

def calcular_serie_factorial():
    try:
        num_usuario = int(input("1. Ingrese un número para calcular la serie factorial: "))
        if num_usuario < 0:
            print("Debe ser un número positivo.")
            return

        print(f"\nSerie Factorial de 1 hasta {num_usuario}:")
        for i in range(1, num_usuario + 1):
            resultado = factorial_recursivo(i)
            print(f"{i}! = {resultado}")

    except ValueError:
        print("Entrada inválida. Ingrese un número entero.")

# 2) Serie de Fibonacci

def fibonacci_recursivo(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

def mostrar_serie_fibonacci():
    try:
        limite = int(input("\n2. Ingrese la posición límite para la serie de Fibonacci: "))
        if limite < 0:
            print("Debe ingresar un número no negativo.")
            return
            
        serie = []
        for i in range(limite + 1):
            serie.append(fibonacci_recursivo(i))
            
        print(f"Serie de Fibonacci hasta la posición {limite}: {serie}")
        
    except ValueError:
        print("Entrada inválida. Ingrese un número entero.")

# 3) Potencia de un Número

def potencia_recursiva(base, exponente):
    if exponente == 0:
        return 1
    elif exponente > 0:
        return base * potencia_recursiva(base, exponente - 1)
    else:
        return 1 / potencia_recursiva(base, abs(exponente))

def probar_potencia():
    print("\n3. Cálculo de Potencia Recursiva")
    try:
        base = float(input("Ingrese la base (n): "))
        exponente = int(input("Ingrese el exponente (m): "))
        
        resultado = potencia_recursiva(base, exponente)
        print(f"Resultado de {base}^{exponente} es: {resultado}")
        
    except ValueError:
        print("Entrada inválida.")

# 4) Conversión Decimal a Binario

def decimal_a_binario_recursivo(n):
    if n == 0:
        return ""
    
    resto = n % 2
    cociente = n // 2
    
    return decimal_a_binario_recursivo(cociente) + str(resto)

def probar_binario():
    print("\n4. Decimal a Binario Recursivo")
    try:
        num = int(input("Ingrese un número decimal positivo: "))
        if num == 0:
            print("0 en binario es: 0")
        elif num < 0:
            print("Ingrese un número positivo.")
        else:
            binario = decimal_a_binario_recursivo(num)
            print(f"El número {num} en binario es: {binario}")
            
    except ValueError:
        print("Entrada inválida.")

# 5) Verificar si una Palabra es Palíndromo

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    
    if palabra[0] == palabra[-1]:
        return es_palindromo(palabra[1:-1])
    else:
        return False

def probar_palindromo():
    print("\n5. Verificación de Palíndromo Recursiva")
    palabra = input("Ingrese una palabra (sin espacios/tildes): ").lower()
    
    if es_palindromo(palabra):
        print(f"'{palabra}' es un palíndromo.")
    else:
        print(f"'{palabra}' NO es un palíndromo.")

# 6) Suma de Dígitos de un Número

def suma_digitos(n):
    if n == 0:
        return 0
    
    ultimo_digito = n % 10
    resto_del_numero = n // 10
    
    return ultimo_digito + suma_digitos(resto_del_numero)

def probar_suma_digitos():
    print("\n6. Suma de Dígitos Recursiva")
    try:
        num = int(input("Ingrese un número entero positivo (ej. 1234): "))
        if num < 0:
            print("Ingrese un número positivo.")
            return
        
        resultado = suma_digitos(num)
        print(f"La suma de los dígitos de {num} es: {resultado}")
        
    except ValueError:
        print("Entrada inválida.")

# 7) Contar Bloques de una Pirámide

def contar_bloques(n):
    if n <= 0:
        return 0
    
    return n + contar_bloques(n - 1)

def probar_contar_bloques():
    print("\n7. Contar Bloques de Pirámide Recursiva")
    try:
        num = int(input("Ingrese el número de bloques del nivel más bajo: "))
        if num < 0:
             print("El número de bloques debe ser no negativo.")
             return
        print(f"Bloques({num}) -> {contar_bloques(num)}")
        print(f"Ejemplos: Bloques(4) -> {contar_bloques(4)}")

    except ValueError:
        print("Entrada inválida.")

# 8) Contar Ocurrencias de un Dígito en un Número

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    
    ultimo_digito = numero % 10
    resto_del_numero = numero // 10
    
    coincide = 1 if ultimo_digito == digito else 0
    
    return coincide + contar_digito(resto_del_numero, digito)

def probar_contar_digito():
    print("\n8. Contar Ocurrencias de un Dígito Recursiva")
    try:
        num = int(input("Ingrese el número entero positivo (ej. 12233421): "))
        digito = int(input("Ingrese el dígito a contar (0-9): "))
        
        if num < 0 or digito < 0 or digito > 9:
            print("Entrada inválida. Asegúrese de que el dígito esté entre 0 y 9.")
            return

        if num == 0 and digito == 0:
            resultado = 1
        elif num == 0:
            resultado = 0
        else:
            resultado = contar_digito(num, digito)
            
        print(f"El dígito {digito} aparece {resultado} veces en {num}.")
        print(f"Ejemplo: contar_digito(12233421, 2) -> {contar_digito(12233421, 2)}")

    except ValueError:
        print("Entrada inválida.")


def main():
    print("INICIO PRÁCTICO 11: APLICACIÓN DE LA RECURSIVIDAD")
    
    calcular_serie_factorial()
    mostrar_serie_fibonacci()
    probar_potencia()
    probar_binario()
    probar_palindromo()
    probar_suma_digitos()
    probar_contar_bloques()
    probar_contar_digito()
    
    print("\nFIN DEL PROGRAMA")

if __name__ == "__main__":
    main()