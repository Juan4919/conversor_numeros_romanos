class Heroe:
    #variables o atributos de la clase Heroe
    nombre = ""
    poder = ""
    apodo = ""
    edad = 20

    #funcion o metodo de la clase Heroe
    #funcion inicial o constructor
    #se ejecuta de manera automatica al crear un objeto de la clase
    def __init__(self,name,power,nickname):
        self.nombre = name
        self.poder = power
        self.apodo = nickname

    def saludar(self):
        print(f"Hola {self.nombre} tu edad es: {self.edad}")

    def datos(self):
        return f"Nombre:{self.nombre}, Poder:{self.poder}, Apodo: {self.apodo}, Edad:{self.edad}"      


#como invocamos
#un objeto de la clase heroe, un instancia de la clase heroe
spyderman = Heroe("Peter Parker","Super fuerza","Hombre araña")
print(spyderman.datos())

iroman = Heroe("Tony Stark","Millonario","Hombre de acero")
iroman.edad=40
print(iroman.datos())

hulk = Heroe("Bruce Banner","Nervios","Increible")
hulk.edad=45
print(hulk.datos())



