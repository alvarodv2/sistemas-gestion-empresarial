
# Exercice 2 -----------------------
class FiguraGeometrica:

    # Metodo superficie que devuelve 0.
    def superficie(self):
        return 0  
    
class TrianguloRectangulo(FiguraGeometrica):
    def __init__(self, cateto1, cateto2):
        self.cateto1 = cateto1
        self.cateto2 = cateto2

    def hipotenusa(self):
        return (self.cateto1 ** 2 + self.cateto2 ** 2) ** 0.5

    def superficie(self):
        return (self.cateto1 * self.cateto2) / 2
        
class Rectangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def superficie(self):
        return self.base * self.altura
        
class ListaDeFiguras:
    def __init__(self):
        self.figuras = []

    def anadirTriangulo(self, cateto1, cateto2):
        self.figuras.append(TrianguloRectangulo(cateto1, cateto2))
        
    def anadirCuadrado(self, base, altura):
        self.figuras.append(Rectangulo(base, altura))

    # Sumamos el total de las superficies de las figuras
    def superficieTotal(self):
        total = 0
        for figura in self.figuras:
            total += figura.superficie()
        return total
    
    # Indicamos el total de triangulos que hay en la lista
    def contarTriangulos(self):
        return sum(isinstance(figura, TrianguloRectangulo) for figura in self.figuras)
        

# Imprimimos el total de superficies
figuras = ListaDeFiguras()