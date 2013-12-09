'''
Created on Nov 20, 2013

@autores: Oscar Burguillos y Patricia Zambrano
@carnets: 09-10118 y 09-10919
'''
from Persona import Persona

# Definimos la subclase asociada a la clase Persona
class Autor(Persona):
    '''
    classdocs
    '''
    def __init__(self, nombre=None,apellido=None,correo=None,dirPostal=None,
                 institucion=None,telefono=None,pagina=None,pais=None):

        '''
        Constructor
        '''
        Persona.__init__(self, nombre, apellido, correo, dirPostal, institucion, telefono, pagina, pais)
