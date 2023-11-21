#diccionario = {"jose":10,"carlos":23,"maria":33}
#print(diccionario.get("maria"))

#for c,v in diccionario.items():
#    print( c+"-"+str(v) )



#string format .format

#valor = 333
#valor = "{:0>4d}".format(valor)

#print(valor)

#valor = int(10**(len('333')-1))
#print(valor)

#nombre="antonio"
#print("esto mide:",len(nombre))


"""
#repaso diccionarios

d1 = { "nombre" : "Carlos",
      "edad" : 45,
       "dni" : "X245454",
        10 : "X" }

print(d1)

d2 = (dict [
    ('nombre','Dulce'),
    ('edad',25),
    ('dni','T232323')
] )
print(d2)

#funciones para diccionarios
print("funcion get()" ,d1.get(100,True) )

#if d1.get(100) == None:
#    print("No existe esta clave en el diccionario")

#funcion clear, elimina todo el diccionario
#d1.clear()
#print("funcion clear: ",d1)

#funcion items devuelve una lista con los keys y values del diccionario
valores =d1.items()
print(valores)

for key,value in valores:
    print(str(key)+" - "+str(value))

#obtener solo claves
llaves = d1.keys()

#obtener solo los valores
values = d1.values()

#eliminar un item especifico
d1.pop(10)
#para cargar nuevos valores a un diccionario
d1.update({'a':100,'b':20})
#para eliminar de manera aleatoria
d1.popitem()
"""

"""
dic_entero_a_romano={
    1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX',
    10:'X',20:'XX',30:'XXX',40:'XL',50:'L',60:'LX',70:'LXX',80:'LXXX',90:'XC',
    100:'C',200:'CC',300:'CCC',400:'CD',500:'D',600:'DC',700:'DCC',800:'DCCC',900:'CM',
    1000:'M',2000:'MM',3000:'MMM'
}

dic_romano_a_entero={
    'I':1, 'V':5, 'X':10,
    'L':50, 'C':100, 'D':500,
    'M':1000
}

for i in "III":
    print(i)
    """
"""
pruebas= [1,2,3]
try:
    print(pruebas[6])
except IndexError:
    print("La longitud no existe")
try:
    division = 10/0
except ZeroDivisionError:
    print("No se puede dividir entre Cero '0' ") 
    """   
"""
try:
    division = 10/0
except Exception as e:
    print("No se puede dividir entre Cero '0' ")
    """
"""
def miExcepcion():
    raise Exception("Esto es mi propia excepcion") #generar una excepcion


miExcepcion()
"""
"""
from main import RomanNumberError

def pruebaException():
    raise RomanNumberError("Esto es mi excepcion")

pruebaException()
"""
"""
frutas = ["fresa","manzana","pera","platano"]

if 'melon' in frutas:
    print("si existe esta fruta")

if 'piña' not in frutas:
    print("no se encuentra piña en frutas")    



dia = "martes"

if dia =='sabado':
    print("Es sabado")
else:
    print("No es sabado")

if dia =='domingo':
    print("Es domingo")
else:
    print("No es domingo")



restas ={'I':('V','X'), 'X':('L','C'), 'C':('D','M') }

print(restas['C'][0])
"""
"""
frutas = ["fresa","manzana","pera","platano"]

if 'melon' not in frutas:
    print("si existe esta fruta")
"""
"""
valor =""

if valor:
    print("no esta vacio")
else:
    print("si esta vacio")    


"""
"""
nombre = "joseantonioparra"
if 'pepe' in nombre:
    print("si se encuentra") 
else:
    print("no se encuentra")     
"""

num=4545


if type (num) == int:
    print("si")
else:
    print("no")