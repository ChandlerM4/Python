#Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. 
#Calcular después la suma, resta, multiplicación y división. Utilizar un método para cada una e imprimir lo 
#resultados obtenidos.
#Llamar a la clase Calculadora.

class Calcu:
    def __init__(self):
        self.n1 = int(input("Escriba un numero: "))
        self.n2 = int(input("Escriba otro numero: "))

    def suma(self):
        suma = self.n1 + self.n2
        print("El resultado de la suma es: ", suma)

    def resta(self):
        resta = self.n1 - self.n2
        print("El resultado de la resta es: ", resta)

    def multiplicacion(self):
        multi = self.n1 * self.n2
        print("El resultado de la multiplicacion es: ", multi)

    def division(self):
        division = self.n1 / self.n2
        print("El resultado de la division es: ", division)
    
    def imprimir(self):
        print("Los valores son: ")
        print("El numero uno es: ", self.n1)
        print("El numero dos es: ", self.n2)

results = Calcu()
results.imprimir()
results.suma()
results.resta()
results.multiplicacion()
results.division()