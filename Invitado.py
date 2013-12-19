'''
Created on Nov 20, 2013

@autores: Oscar Burguillos y Patricia Zambrano
@carnets: 09-10118 y 09-10919
'''
from Persona import Persona

# Definimos la subclase asociada a la clase Persona
class Asistente(Persona):
    '''
    classdocs
    '''
    def __init__(self, nombre=None,apellido=None,correo=None,dirpostal=None,
                 institucion=None,telefono=None,pagina=None,pais=None,CV=None):

        '''
        Constructor
        '''
        Persona.__init__(self, nombre, apellido, correo, dirpostal, institucion, telefono, pagina, pais)
        self.CV=CV
        
    # Definicion de los metodos get de todos los atributos de la clase
    def get_CV(self):
        return self.CV

    # Definicion de todos los set de los atributos de la clase    
    def set_CV(self,CV=None):
        self.CV=CV