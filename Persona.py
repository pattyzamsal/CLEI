'''
Created on Nov 20, 2013

@autores: Oscar Burguillos y Patricia Zambrano
@carnets: 09-10118 y 09-10919
'''

class Persona:
    '''
    classdocs
    '''
    def __init__(self, nombre=None,apellido=None,correo=None,dirPostal=None,
                 institucion=None,telefono=None,pagina=None,pais=None):
        '''
        Constructor
        '''
        self.nombre=nombre
        self.apellido=apellido
        self.correo=correo
        self.dirPostal=dirPostal
        self.institucion=institucion
        self.telefono=telefono
        self.pagina=pagina
        self.pais=pais
        
    # Definicion de los metodos get de todos los atributos de la clase
    def getNombre(self):
        return self.nombre
    
    def getApellido(self):
        return self.apellido
    
    def getCorreo(self):
        return self.correo
    
    def getDirPostal(self):
        return self.dirPostal
    
    def getInstitucion(self):
        return self.institucion
    
    def getTelefono(self):
        return self.telefono
    
    def getPagina(self):
        return self.pagina
    
    def getPais(self):
        return self.pais

    # Definicion de todos los set de los atributos de la clase    
    def setNombre(self,nombre=None):
        self.nombre=nombre
        
    def setApellido(self,apellido=None):
        self.apellido=apellido
        
    def setCorreo(self,correo=None):
        self.correo=correo
        
    def setDirPostal(self,dirPostal=None):
        self.dirPostal=dirPostal
        
    def setInstitucion(self,institucion=None):
        self.institucion=institucion
        
    def setTelefono(self,telefono=None):
        self.telefono=telefono
        
    def setPagina(self,pagina=None):
        self.pagina=pagina
        
    def setPais(self,pais=None):
        self.pais=pais
