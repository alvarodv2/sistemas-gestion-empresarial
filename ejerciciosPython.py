
# Exercice 1 -----
def verificarNumero(n):
    if n == 0:
        print(f"El número 22 no es primo, repite")
        return True
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return False
        print(f"El número 22 no es primo, repite")
        return True

while True:
    n = int(input("Ingrese un número: "))
    if verificarNumero(n):
        break
        

# Exercice2 -----
def divisionControlada(a,b):

    try:
        d = a/b
        # Si escribiesemos int(d), nos saldría el número entero de la división.
        # Si escribimos simplemente return d, nos devuelve el número real. 
        return d
    except ZeroDivisionError:
        return 0
    
a = int(input("Ingrese el dividendo: "))
b = int(input("Ingrese el divisor: "))
resultado = divisionControlada(a,b)
print(f"El resultado de la división es: {resultado}")


# Exercice 3 -----
def listaDeCadenas():

    nuevaCadena = ["Mbappe", "Vini", "Bellingham", "Haaland", "C.Ronaldo"]

    longitud = [len(cadena) for cadena in nuevaCadena]

    print(longitud)

# Llamada a la funcion
listaDeCadenas()

# Exercice 4 -----   
def binaryToDecimal(binary_str):

    decimal = int(binary_str, 2)
    return decimal

def decimalToBinary(decimal_num):

    binary_str = bin(decimal_num)[2:]  
    return binary_str

def binaryFunction():
    cadenaTexto = "100101010001"
    
    # Convertimos la cadena binaria a decimal
    decimal = binaryToDecimal(cadenaTexto)
    print(f"Decimal: {decimal}")
    
    # Convertimos el decimal de vuelta a binario
    binary_str = decimalToBinary(decimal)
    print(f"Binario: {binary_str}")

# Llamada a la funcion
binaryFunction()

# Exercice 5 -----
def transformasCadena():

    texto = "Hola Mundo"

    #Convertimos la cadena en una lista
    lista = texto.split()

    #Invertimos el orden de la lista
    listaAlReves = lista[::-1]

    # Invertirmos cada palabra
    listaAlReves = [palabra[::-1] for palabra in listaAlReves]

    # Juntamos el resultado de las palabras invertidas en una cadena
    resultado = ' '.join(listaAlReves)

    print(resultado)

# Llamada a la funcion
transformasCadena()


# Exercice 6 -----
def dosListas():
    
    lista1 = [1,2,3,4,5]
    lista2 = [6,7,8,9,10]

    if len(lista1) != len(lista2):
        raise ValueError("Las listas no tienen la misma longitud")
    else:
        lista_mayores = list(map(lambda x, y: max(x, y), lista1, lista2))
        print(lista_mayores)

# Llamada a la funcion
dosListas()


# Exercice 7 {Sin resolver por dudas/falta de timepo de entrega} -----


# DICCIONARIOS Excersice 7 -----
def gestionDeFruteria():

    # Diccionario para almacenar los productos de la tienda
    diccionarioFruteria = {}  

    # Diccionario para almacenar los productos de la cesta
    cestaDeLaCompra = {}  

    while True:
        print("\n---- Frutería ----")
        print("1. Añadir artículo a la frutería")
        print("2. Mostrar tienda (ver todos los artículos y precios)")
        print("3. Crear una nueva cesta de la compra")
        print("4. Añadir artículo a la cesta")
        print("5. Calcular el total de la cesta")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre de la fruta: ").strip()
            if nombre.lower() == 'salir':
                print("Cancelando la operacion...")
                break
            try:
                precio = float(input(f"Ingrese el precio por kilo de {nombre}: "))
                diccionarioFruteria[nombre] = precio
                print(f"Artículo añadido: {nombre} - Precio por kilo: {precio}")
            except ValueError:
                print("Por favor, ingrese un precio valido.")

        elif opcion == "2":
            if diccionarioFruteria:
                print("\n--- Articulos en tienda ---")
                for fruta, precio in diccionarioFruteria.items():
                    print(f"Fruta: {fruta}, Precio por kilo: {precio}")
            else:
                print("La tienda no tiene articulos aun.")

        elif opcion == "3":
            cestaDeLaCompra.clear()  
            print("Se ha creado una nueva cesta de la compra (vacia).")

        elif opcion == "4":
            if not diccionarioFruteria:
                print("No hay articulos en la tienda para añadir a la cesta.")
                continue

            fruta = input("Ingrese el nombre de la fruta que desea añadir a la cesta: ").strip()
            if fruta in diccionarioFruteria:
                try:
                    cantidad = float(input(f"Ingrese la cantidad de kilos de {fruta}: "))
                    precio = diccionarioFruteria[fruta]
                    total_por_fruta = cantidad * precio
                    if fruta in cestaDeLaCompra:
                        cestaDeLaCompra[fruta] += total_por_fruta  
                    else:
                        cestaDeLaCompra[fruta] = total_por_fruta
                    print(f"Se ha añadido {cantidad} kilos de {fruta} por un total de {total_por_fruta:.2f} a la cesta.")
                except ValueError:
                    print("Por favor, ingrese una cantidad valida.")
            else:
                print(f"{fruta} no esta disponible en la tienda.")

        elif opcion == "5":
            if not cestaDeLaCompra:
                print("La cesta esta vacia. Añada articulos primero.")
            else:
                print("\n--- Cesta de la compra ---")
                total = 0
                for fruta, subtotal in cestaDeLaCompra.items():
                    print(f"{fruta}: {subtotal:.2f}€")
                    total += subtotal
                print(f"\nTotal de la cesta: {total:.2f}€")

        elif opcion == "6":
            print("Saliendo del programa...")
            break

        # Opcion no valida
        else:
            print("Opcion no valida!")

# Llamada a la funcion
gestionDeFruteria()


# DICCIONARIOS Excersice 8 -----
def diccionarioIdiomas():

    diccionario = {}

    while True:
        print("\n---- Diccionario Español-Ingles ----")
        print("1. Añadir palabras al diccionario")
        print("2. Traducir frase")
        print("3. Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            entrada = input("Ingrese las palabras en formato 'Español:Ingles' separadas por los dos puntos: ")
            pares = entrada.split(',')
            for par in pares:
                espanol, ingles = par.split(':')
                diccionario[espanol.strip()] = ingles.strip()
            print("Palabra añadida al diccionario.")

        elif opcion == "2":
            frase = input("Ingrese una frase en español: ")
            palabras = frase.split()
            traduccion = []
            for palabra in palabras:
                if palabra in diccionario:
                    traduccion.append(diccionario[palabra])
                else:
                    traduccion.append(palabra)
            print("Frase traducida:", ' '.join(traduccion))

        elif opcion == "3":
            print("Saliendo del programa...")
            break

        else:
            print("Opcion no valida!")

# Llamada a la funcion
diccionarioIdiomas()


