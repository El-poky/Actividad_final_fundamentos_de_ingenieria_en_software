def mostrar_menu():
    print("\n==============================")
    print("   BIENVENIDO A LA CALCULADORA DE ESCRITORIO")
    print("==============================")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    print("==============================")

def sumar():
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    resultado = a + b
    print(f"El resultado de la suma es: {resultado}")

def restar():
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    resultado = a - b
    print(f"El resultado de la resta es: {resultado}")

def multiplicar():
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    resultado = a * b
    print(f"El resultado de la multiplicación es: {resultado}")

def dividir():
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    
    if b == 0:
        print("Error: no se puede dividir entre cero.")
    else:
        resultado = a / b
        print(f"El resultado de la división es: {resultado}")

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1-5): ")

    if opcion == "1":
        sumar()
    elif opcion == "2":
        restar()
    elif opcion == "3":
        multiplicar()
    elif opcion == "4":
        dividir()
    elif opcion == "5":
        print("Gracias por usar la calculadora. ¡Hasta luego!")
        break
    else:
        print("Opción inválida, por favor seleccione una opción válida.")
