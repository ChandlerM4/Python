#En un banco tienen clientes que pueden hacer depósitos y extracciones de dinero. 
#El banco requiere también al final del día calcular la cantidad de dinero que se ha depositado.
#Se deberán crear dos clases, la clase Cliente y la Clase Banco.
#La clase Cliente tendrá los atributos nombre y cantidad y los métodos __init__, depositar, extraer, imprimir.
#La clase Banco tendrá como atributos 3 objetos de la clase Cliente y los métodos __init__, operar y depósitos.

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cantidad = 0
    
    def depositar(self, cantidad):
        self.cantidad += cantidad

    def extraer(self, cantidad):
        self.cantidad -= cantidad

    def devolver_cantidad(self):
        return self.cantidad
    
    def imprimir(self):
        print(self.nombre, "tiene la cantidad depositada de ", self.cantidad)

class Banco:
    def __init__(self):
        self.cliente1 = Cliente("Ivan")
        self.cliente2 = Cliente("Mark")
        self.cliente3 = Cliente("Ana")

    def operar(self):
        self.cliente1.depositar(300)
        self.cliente2.depositar(500)
        self.cliente3.depositar(800)
        self.cliente1.extraer(100)

    def depositos_finales(self):
        deposito = self.cliente1.devolver_cantidad() + self.cliente2.devolver_cantidad() + self.cliente3.devolver_cantidad()
        print("Total de dinero del banco ", deposito)
        self.cliente1.imprimir()
        self.cliente2.imprimir()
        self.cliente3.imprimir()

total = Banco()
total.operar()
total.depositos_finales()