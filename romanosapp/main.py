from romanos_class import NumeroRomano

continuar = True
seguir=""
operacion =""
valor=""

while continuar:
    print("Inicio del programa")
    operacion= input("Que desea realizar Romano_a_entero:presione 'r' \n Entero_a_romano: presione: 'e' ")

    print("Ejecucion del programa")
    if operacion == "r":
        try:
            valor = input("ingrese el valor en romano: ")
            obj1 = NumeroRomano(valor)
            print(f"El valor de {obj1.representacion_romano} es igual a {obj1.valor_numerico}")
        except Exception as e:
            print(e)

    elif operacion == "e":
        try:
            valor = int(input("ingrese el valor entero: "))
            obj2 = NumeroRomano(valor)
            print(f"El valor de {obj2.valor_numerico} es igual a {obj2.representacion_romano}")    
        except Exception as e:
                    print(e)

    seguir = input("Si desea salir del programa precione 'n' :")
    if seguir == "n":
        continuar = False
        print("Fin del programa")