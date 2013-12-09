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
    def __init__(self, anio=None,duracion=None,pais=None,maxArticulos=None,aceptables=[]):

        '''
        Constructor
        '''
        self.anio=anio
        self.duracion=duracion
        self.pais=pais
        self.maxArticulos=maxArticulos
        self.aceptables=aceptables
        
    # Definicion de los metodos get de todos los atributos de la clase
    def getAnio(self):
        return self.anio
    
    def getDuracion(self):
        return self.duracion
    
    def getPais(self):
        return self.pais
    
    def getMaxArticulos(self):
        return self.maxArticulos
    
    def getAceptables(self):
        return self.aceptables
    
    # Definicion de todos los set de los atributos de la clase    
    def setAnio(self,anio=None):
        self.anio=anio
        
    def setDuracion(self,duracion=None):
        self.duracion=duracion
        
    def setPais(self,pais=None):
        self.pais=pais
        
    def setMaxArticulos(self,maxArticulos=None):
        self.maxArticulos=maxArticulos

    # Aceptables es una lista de evaluaciones que contiene todos 
    # los articulos que poseen al menos 2 evaluaciones y que su 
    # promedio es mayor que 3.00
    def setAceptables(self,evaluacion):
        if evaluacion.aprobado():
            self.aceptables.append(evaluacion)

    # Este metodo calcula cuantas veces aparece el promedio dentro de una lista de aceptados y de aceptables
    def calcularOcurrencia(self,promedio,lista):
        ocurrencia=0
        for element in lista:
            if element.getPromedio()==promedio:
                ocurrencia+=1
        return ocurrencia

    # Este metodo retorna una lista con los articulos aceptados por CLEI
    def getAceptados(self):
        #Se ordenan los elementos de la lista segun el promedio(mayor a menor)
        self.aceptables=sorted(self.aceptables,key= lambda element: element.promedio, reverse = True)
        # Se verifica si el maximo de articulos es mayor que la longitud de la lista de aceptables
        # si esto pasa entonces la lista de aceptables pasa a ser la lista de aceptados, sino se busca
        # cual es la nueva lista de aceptados
        if self.maxArticulos>=len(self.aceptables):
            return self.aceptables
        else:
            aceptados=[]
            i=0
            while i<self.maxArticulos:
                aceptados.append(self.aceptables[i])
                i+=1
            # ultimo es el promedio minimo contenido en la lista de aceptados
            ultimo=aceptados[self.maxArticulos-1]
            # se cuenta cuantas veces aparece el promedio en la lista de aceptados
            numVecesAccept=self.calcularOcurrencia(ultimo.getPromedio(), aceptados)
            # se cuenta cuantas veces aparece el promedio en la lista de aceptables
            numVecesAceptables=self.calcularOcurrencia(ultimo.getPromedio(), self.aceptables)
            # si el numero de veces de aceptados es distinto del numero de veces de aceptables
            # se procede a eliminar todos los valores que fueron admitidos en la lista de aceptados
            if numVecesAccept!=numVecesAceptables:
                while numVecesAccept>0:
                    aceptados.remove(ultimo)
                    numVecesAccept-=1
            return aceptados
    
    # Este metodo retorna una lista de los articulos que fueron aceptados por CLEI pero que se encuentran
    # dentro de la lista de empatados
    def getEmpatados(self,aceptados):
        empatados=self.aceptables
        for element in aceptados:
            empatados.remove(element)
        return empatados
    