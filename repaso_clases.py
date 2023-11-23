#clase plantilla de bloque de codigo que contiene atributos(variables) y metodos(funciones) que pueden ser
#utilizados tantas veces se requiera
import datetime

class Persona:
    #self seria una referencia a las variables y funciones de la clase
    def __init__(self,nombre:str,email:str):
        self.nombre = nombre
        self.email = email
        self.fecha = datetime.datetime.now()
       

    #metodo magico para mostrar la representacion de un objeto en string
    def __repr__(self):
        return f"Nombre: {self.nombre}, Email: {self.email}, Fecha: {self.fecha}"
    #metodo magico para mostrar datos de un objeto en string
    def __str__(self):
        return f"Nombre: {self.nombre}, Email: {self.email}, Fecha: {self.fecha}"
    #metodo magico para sumar atributos de objetos
    def __add__(self,valor):
        return f"un objeto de fuera: {10 + valor.valor_inicial}"

class Numero:
    def __init__(self,valor):
        self.valor_inicial=valor        

#invoco a una clase
#al invocar una clase se nombra crear un objeto de la clase, instanciar una clase
objetoPersona = Persona("Maria","maria@email.com")
objetoNumero = Numero(25)

resultado = objetoPersona + objetoNumero
print(resultado)



#print("metodo str:",str(datetime.datetime.now()) )
#print("metodo repr:",repr(datetime.datetime.now()))
