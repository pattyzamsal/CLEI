'''
Created on Nov 21, 2013

@autores: Oscar Burguillos y Patricia Zambrano
@carnets: 09-10118 y 09-10919
'''
from Evaluacion import *

class CLEI():
    '''
    classdocs
    '''
    def __init__(self, anio=None,duracion=None,pais=None,maxarticulos=None,aceptables=[]):

        '''
        Constructor
        '''
        self.anio=anio
        self.duracion=duracion
        self.pais=pais
        self.maxarticulos=maxarticulos
        self.aceptables=aceptables
        
    # Definicion de los metodos get de todos los atributos de la clase
    def get_anio(self):
        return self.anio
    
    def get_duracion(self):
        return self.duracion
    
    def get_pais(self):
        return self.pais
    
    def get_maxarticulos(self):
        return self.maxarticulos
    
    def get_aceptables(self):
        return self.aceptables
    
    # Definicion de todos los set de los atributos de la clase    
    def set_anio(self,anio=None):
        self.anio=anio
        
    def set_duracion(self,duracion=None):
        self.duracion=duracion
        
    def set_pais(self,pais=None):
        self.pais=pais
        
    def set_maxarticulos(self,maxarticulos=None):
        self.maxarticulos=maxarticulos

    # Aceptables es una lista de evaluaciones que contiene todos 
    # los articulos que poseen al menos 2 evaluaciones y que su 
    # promedio es mayor que 3.00
    def set_aceptables(self,evaluacion):
        if evaluacion.aprobado():
            self.aceptables.append(evaluacion)

    # Este metodo calcula cuantas veces aparece el promedio dentro de una lista de aceptados y de aceptables
    def calcular_ocurrencia(self,promedio,lista):
        ocurrencia=0
        for element in lista:
            if element.get_promedio()==promedio:
                ocurrencia+=1
        return ocurrencia

    # Este metodo retorna una lista con los articulos aceptados por CLEI
    def get_aceptados(self):
        #Se ordenan los elementos de la lista segun el promedio(mayor a menor)
        self.aceptables=sorted(self.aceptables,key= lambda element: element.promedio, reverse = True)
        # Se verifica si el maximo de articulos es mayor que la longitud de la lista de aceptables
        # si esto pasa entonces la lista de aceptables pasa a ser la lista de aceptados, sino se busca
        # cual es la nueva lista de aceptados
        if self.maxarticulos>=len(self.aceptables):
            return self.aceptables
        else:
            aceptados=[]
            i=0
            while i<self.maxarticulos:
                aceptados.append(self.aceptables[i])
                i+=1
            # ultimo es el promedio minimo contenido en la lista de aceptados
            ultimo=aceptados[self.maxarticulos-1]
            # se cuenta cuantas veces aparece el promedio en la lista de aceptados
            numvecesaccept=self.calcular_ocurrencia(ultimo.get_promedio(), aceptados)
            # se cuenta cuantas veces aparece el promedio en la lista de aceptables
            numvecesaceptables=self.calcular_ocurrencia(ultimo.get_promedio(), self.aceptables)
            # si el numero de veces de aceptados es distinto del numero de veces de aceptables
            # se procede a eliminar todos los valores que fueron admitidos en la lista de aceptados
            if numvecesaccept!=numvecesaceptables:
                while numvecesaccept>0:
                    aceptados.remove(ultimo)
                    numvecesaccept-=1
            return aceptados
    
    # Este metodo retorna una lista de los articulos que fueron aceptados por CLEI pero que se encuentran
    # dentro de la lista de empatados
    def get_empatados(self,aceptados):
        empatados=self.aceptables
        for element in aceptados:
            empatados.remove(element)
        return empatados
    