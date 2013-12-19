'''
Created on Nov 20, 2013

@autores: Oscar Burguillos y Patricia Zambrano
@carnets: 09-10118 y 09-10919
'''

class Persona:
    '''
    classdocs
    '''
    def __init__(self, nombre=None,apellido=None,correo=None,dirpostal=None,
                 institucion=None,telefono=None,pagina=None,pais=None):
        '''
        Constructor
        '''
        self.nombre=nombre
        self.apellido=apellido
        self.correo=correo
        self.dirpostal=dirpostal
        self.institucion=institucion
        self.telefono=telefono
        self.pagina=pagina
        self.pais=pais
        
    # Definicion de los metodos get de todos los atributos de la clase
    def get_nombre(self):
        return self.nombre
    
    def get_apellido(self):
        return self.apellido
    
    def get_correo(self):
        return self.correo
    
    def get_dirpostal(self):
        return self.dirpostal
    
    def get_institucion(self):
        return self.institucion
    
    def get_telefono(self):
        return self.telefono
    
    def get_pagina(self):
        return self.pagina
    
    def get_pais(self):
        return self.pais

    # Definicion de todos los set de los atributos de la clase    
    def set_nombre(self,nombre=None):
        self.nombre=nombre
        
    def set_apellido(self,apellido=None):
        self.apellido=apellido
        
    def set_correo(self,correo=None):
        self.correo=correo
        
    def set_dirpostal(self,dirpostal=None):
        self.dirpostal=dirpostal
        
    def set_institucion(self,institucion=None):
        self.institucion=institucion
        
    def set_telefono(self,telefono=None):
        self.telefono=telefono
        
    def set_pagina(self,pagina=None):
        self.pagina=pagina
        
    def set_pais(self,pais=None):
        self.pais=pais
