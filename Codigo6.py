class Alumno:
    def inicializar(self, nombre, calificacion):
        self.nombre = nombre
        self.calificacion = calificacion
    
    def imprimir(self):
        print("Nombre: " + self.nombre)
        print("Calificacion: " + str(self.calificacion))
    
    def resultados(self):
        if self.calificacion < 70:
            print("Estudiante Reprobado.")
        else:
            print("Estudiante Aprobado.")

alumno1 = Alumno()
alumno1.inicializar("Ivan", 80)
alumno1.imprimir()
alumno1.resultados()
print("===================================")
alumno2 = Alumno()
alumno2.inicializar("Juan",40)
alumno2.imprimir()
alumno2.resultados()