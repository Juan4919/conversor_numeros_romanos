diccionario = {"jose":10,"carlos":23,"maria":33}
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

