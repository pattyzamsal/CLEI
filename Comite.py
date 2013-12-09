'''
Created on Nov 20, 2013

@autores: Oscar Burguillos y Patricia Zambrano
@carnets: 09-10118 y 09-10919
'''
from Persona import Persona

# Definimos la subclase asociada a la clase Persona
class Comite(Persona):
    '''
    classdocs
    '''
    def __init__(self, nombre=None,apellido=None,correo=None,dirPostal=None,
                 institucion=None,telefono=None,pagina=None,pais=None,presidente=False,arbitro=False):

        '''
        Constructor
        '''
        Persona.__init__(self, nombre, apellido, correo, dirPostal, institucion, telefono, pagina, pais)
        self.presidente=presidente
        self.arbitro=arbitro
        
    # Definicion de los metodos get de todos los atributos de la clase
    def getPresidente(self):
        return self.presidente
    
    def getArbitro(self):
        return self.arbitro

    # Definicion de todos los set de los atributos de la clase    
    def setPresidente(self,presidente=None):
        self.presidente=presidente
    
    def setArbitro(self,arbitro=None):
        self.arbitro=arbitro
