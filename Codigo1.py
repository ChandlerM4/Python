class Persona:
    a = 0
    def __init__(self):
        self.nombre = ""
        self.edad = 0

per1 = Persona()
per1.nombre = "Jesus"
per1.edad = 24

print("Nombre: " + per1.nombre + " / " + "Edad: " + str(per1.edad))