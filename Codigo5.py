class Persona:
    def inicializar(self):
        self.nombre = input("Ingrese nombre: ")
        self.edad = input("Ingrese edad: ")
    
    def mostrar(self):
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)

persona1 = Persona()
persona1.inicializar()
persona1.mostrar()