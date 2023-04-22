class Persona:
    def inicializar(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def mostrar(self):
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)

persona1 = Persona()
persona1.inicializar("Jesus", 24)
persona1.mostrar()