'''
Created on Nov 21, 2013

@autores: Oscar Burguillos y Patricia Zambrano
@carnets: 09-10118 y 09-10919
'''

class Evaluacion:
    '''
    classdocs
    '''
    def __init__(self,notas=[],articulo=None,arbitro=[]):
        '''
        Constructor
        '''
        self.notas=notas
        self.articulo=articulo
        self.arbitro=arbitro
        self.promedio=self.promedioNotas()
        
    # Definicion de los metodos get de todos los atributos de la clase
    def getNotas(self):
        return self.notas
    
    def getArticulo(self):
        return self.articulo
    
    def getArbitro(self):
        return self.arbitro
    
    def getPromedio(self):
        return self.promedio
    
    # Definicion de todos los set de los atributos de la clase    
    def setNotas(self,evaluacion=None):
        self.notas.append(evaluacion)
        #Al agregar una nueva nota se recalcula el promedio de notas    
        self.promedio=self.promedioNotas()
        
    def setArticulo(self,articulo=None):
        self.articulo=articulo
        
    def setArbitro(self,persona=None):
        self.arbitro.append(persona)

    # Este metodo se encarga de modificar el promedio que tiene un articulo en una evaluacion
    def promedioNotas(self):
        promedio=0.0
        if len(self.notas)==0:
            return promedio
        # Calculo del promedio de notas
        for element in self.notas:
            promedio=element+promedio
        # Es la suma de todas las notas entre el numero total de notas
        promedio=promedio/len(self.notas)
        # Se le pone la funcion round para que de dos decimales con el uso del redondeo
        return round(promedio,2)
    
    # Este metodo se encarga de verificar que la evaluacion sea aprobada
    def aprobado(self):
        # Si el promedio de notas es mayor que 3.00 y si se tienen al menos 2 notas
        # entonces el articulo es aceptado
        if self.promedioNotas()>=3.00 and len(self.notas)>=2:
            return True
        else:
            return False

    # Este metodo se encarga de verificar si un arbitro en especifico ha realizado 
    # una evaluacion sobre el articulo y si es asi retorna true
    def arbitroDuplicado(self,correo):
        numVeces=self.arbitro.count(correo)
        if numVeces==1:
            return True
        return False

    # Este metodo imprime por pantalla todos los arbitros que han evaluado un articulo en especifico
    def imprimirArbitros(self):
        for elemento in self.arbitro:
            print elemento        