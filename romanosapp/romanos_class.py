from romanos_exception import RomanNumberError
from utils.utiles import *

class NumeroRomano:
    valor_numerico=0
    representacion_romano=""
    valor=None

    def __init__(self,valor):
        #self.valor = valor
        if isinstance(valor, str):#aqui ingresa si el valor es str
            self.valor=valor
            self.representacion_romano=valor
            self.valor_numerico=self.romano_a_entero(valor)
        elif isinstance(valor,int):#aqui ingresa si el valor es int   
            self.valor=valor
            self.valor_numerico=valor
            self.representacion_romano=self.entero_a_romano(valor)
        else:
            raise RomanNumberError("El valor debe ser cadena o entero")  
                    
            
    def entero_a_romano(self,numero:int)->str:
        if numero > 3999 or numero < 0:
            raise RomanNumberError("El limite es entre 0 y 3999")
        if numero == 0:
            return ""
    
        numero = "{:0>4d}".format(numero)#transforma el numero dado a un str de 4 digitos y si es menos lo complementa con ceros a la izquierda
        list_numero = list(numero)#transforma el string dado a una lista de string por cada caracter
        self.valor_romano =""

        cont = 0
        valor_num = 1000
        while cont < len(list_numero):
            list_numero[cont] = int(list_numero[cont])*valor_num
            self.valor_romano += dic_entero_a_romano.get(list_numero[cont],"")
            cont+=1
            valor_num /= 10

        return self.valor_romano
    
    def romano_a_entero(self,romano:str)->int:
        lista_romano = list(romano)
        self.valor_entero = 0
        cont_repes = 0
        caracter_anterior=""
        caracter_ante_anterior=""
        
        for caracter in lista_romano:
            if caracter == caracter_anterior:
                if caracter in "VLD":    
                    raise RomanNumberError("Los caracteres 'D', 'L' y 'V' no se pueden repetir.")

                cont_repes += 1
            else:
                cont_repes = 0    

            if cont_repes > 2:
                raise RomanNumberError("No se puede repetir el valor mas de tres veces")     
        
            if caracter_anterior and dic_romano_a_entero.get(caracter_anterior,0) < dic_romano_a_entero.get(caracter,0):

                if caracter_anterior == "V" or caracter_anterior == "L" or caracter_anterior =="D":
                    raise RomanNumberError("V, L y D nunca se pueden restar")

                if caracter not in restas[caracter_anterior]:
                    raise RomanNumberError(f"{caracter_anterior} se puede restar de { restas[ caracter_anterior][0] } y {restas[ caracter_anterior][1]} solamente")

                self.valor_entero -= dic_romano_a_entero.get(caracter_anterior,0)*2
                                                                                
                if (caracter_anterior == caracter_ante_anterior) and (caracter_anterior in "IXC"):
                    raise RomanNumberError("el valor no se puede restar")

            caracter_ante_anterior = caracter_anterior
            caracter_anterior = caracter
        
            self.valor_entero += dic_romano_a_entero.get(caracter,0)

        return self.valor_entero


    #devuelve un string de cualquier parametro de una clase
    def __repr__(self):
        if isinstance(self.valor, str):#aqui ingresa si el valor es str
            return str(self.valor_entero)
        elif isinstance(self.valor,int):#aqui ingresa si el valor es int    
            return self.valor_romano
        
    def __add__(self,otro):
        if isinstance(otro,NumeroRomano):
            return NumeroRomano(self.valor_numerico + otro.valor_numerico)
        


"""
prueba = NumeroRomano("XXVII")
print("Romano a entero:",prueba)
print("Valor Numerico:",prueba.valor_numerico)
print("Valor Romano",prueba.representacion_romano)
print("======================================")
prueba2 =NumeroRomano(34)
print("Entero a romano:",prueba2)
print("Valor Numerico:",prueba2.valor_numerico)
print("Valor Romano",prueba2.representacion_romano)
"""
