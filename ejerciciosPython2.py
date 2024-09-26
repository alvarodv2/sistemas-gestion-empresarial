
# Exercice 1 -----------------------
class Fraccion:
    def __init__(self, num, den, imprimir=True):
        self.numerador = num
        self.denominador = den

        if self.denominador == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")
        
        # Si uno de los dos es negativo, signo = -1, si no es 1.
        self.signo = -1 if (self.numerador < 0) ^ (self.denominador < 0) else 1
        self.numerador = abs(self.numerador)
        self.denominador = abs(self.denominador)
        
        # Solo mostramos el + o - si imprimir es True.
        if imprimir:
            if self.signo == -1:
                print("Símbolo: -")
            else:
                print("Símbolo: +")

        # Simplificar fraccion.
        for i in range(2, self.denominador):
            if self.numerador % i == 0 and self.denominador % i == 0:
                self.numerador = self.numerador // i
                self.denominador = self.denominador // i

        # Solo mostrar la fracción simplificada si imprimir es True.
        if imprimir:
            print(f"Fracción simplificada: {self.numerador}/{self.denominador}")
    
    def sumar(self, otra_fraccion):
        # Calcular nuevo numerador y denominador sin imprimir nada.
        nuevo_numerador = self.numerador * otra_fraccion.denominador + otra_fraccion.numerador * self.denominador
        nuevo_denominador = self.denominador * otra_fraccion.denominador
        
        # Creamos una nueva fraccion que sera el resultado de la suma.
        # Aquí pasamos imprimir=False para que no se imprima el simbolo y la fraccion simplificada.
        resultado = Fraccion(nuevo_numerador, nuevo_denominador, imprimir=False)
        return resultado
    
    def compararFracciones(self, otra_fraccion):
    # Multiplicamos de forma cruzada para comparar los numeradores
        nuevo_numerador_self = self.numerador * otra_fraccion.denominador
        nuevo_numerador_otra = otra_fraccion.numerador * self.denominador

        # Comparamos los numeradores cruzados
        if nuevo_numerador_self == nuevo_numerador_otra:
            return "Las fracciones son iguales."
        elif nuevo_numerador_self > nuevo_numerador_otra:
            return "La primera fraccion es mayor."
        else:
            return "La segunda fraccion es mayor."
    

    def __repr__(self):
        return str(self.numerador) + '/' + str(self.denominador)

    def __eq__(self, fraccionb):
        return (self.numerador == fraccionb.numerador and
                self.denominador == fraccionb.denominador)


# Imprimimos
x = Fraccion(6, 30)  
y = Fraccion(4, 10)  

# Realizamos la suma sin que se impriman los detalles del resultado de la nueva fraccion
resultado_suma = x.sumar(y)

# Mostramos el resultado de suma
print(f"Resultado de la suma: {resultado_suma}")

# Mostramos el resultado de la comparacion de fracciones
resultadoComparar = x.compararFracciones(y)
print(resultadoComparar)


