class A:

    def __init__(self):

        print("Soy de la clase A")



    def a(self):

        print("Este método lo heredo de A")



class B:

    def __init__(self):

        print("Soy de la clase B")



    def b(self):

        print("Este método lo heredo de B")



class C(B, A):

    def c(self):

        print("Este método es de C")



c=C()

c.a()

c.b()

c.c()