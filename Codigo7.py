class Persona:
    def inicializar(self, nombre, edad):
        self.nom = nombre
        self.ed = edad
    
    def mostrar(self):
        print("Nombre: " + self.nom)
        print("Edad: " + str(self.ed))
    
    def indicar(self):
        if self.ed >= 18:
            print("Es mayor de edad.")
        else:
            print("Es menor de edad.")
    
    def bienvenida(self):
        print("Bienvenidos a mi programa.")

per1 = Persona()
per1.bienvenida()
per1.inicializar("Esmeralda", 23)
per1.mostrar()
per1.indicar()