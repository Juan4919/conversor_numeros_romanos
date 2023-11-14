diccionario = {"jose":10,"carlos":23,"maria":33}
print(diccionario.get("maria"))

for c,v in diccionario.items():
    print( c+"-"+str(v) )