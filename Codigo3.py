class Persona:
    def inicializar(self, nombre): #Parametro nombre el cual tendra valor en el futuro
        self.nombre = nombre

    def mostrar(self):
        print("Nombre: ", self.nombre)

persona1 = Persona()
persona1.inicializar("Marcos")
persona1.mostrar()

persona2 = Persona()
persona2.inicializar("Jesus")
persona2.mostrar()