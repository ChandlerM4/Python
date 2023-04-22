class Triangulo:
    def inicializar(self):
        self.lado1 = input("Ingrese el valor del primer lado: ")
        self.lado2 = input("Ingrese el valor del segundo lado: ")
        self.lado3 = input("Ingrese el valor del tercer lado: ")

    def imprimir(self):
        print("Los siguientes son lo valores de cada lado del triangulo: ")
        print("Lado 1: " + self.lado1)
        print("Lado 2: " + self.lado2)
        print("Lado 3: " + self.lado3)

    def mayor(self):
        print("El lado mayor es: ")
        if self.lado1 > self.lado2 and self.lado1 > self.lado3:
            print("El lado 1 es el mayor: " + self.lado1)
        elif self.lado2 > self.lado3:
            print("El lado 2 es el mayor: " + self.lado2)
        else:
            print("El lado 3 es el mayor: " + self.lado3)
        
    def tipo(self):
        if self.lado1 == self.lado2 and self.lado1 == self.lado3:
            print("Este es un triangulo equilatero.")
        elif self.lado1 != self.lado2 and self.lado1 != self.lado3:
            print("Este es un triangulo escaleno.")
        else:
            print("Este es un triangulo isosceles")

triangulo1=Triangulo()
triangulo1.inicializar()
triangulo1.imprimir()
triangulo1.mayor()
triangulo1.tipo()