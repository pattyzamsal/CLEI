'''
Created on Nov 18, 2013

@autores: Oscar Burguillos y Patricia Zambrano
@carnets: 09-10118 y 09-10919
'''

class Articulo:
    '''
    classdocs
    '''
    def __init__(self, titulo=None,autores=None,palabrasclaves=None,resumen=None,texto=None):
        '''
        Constructor
        '''
        self.titulo=titulo
        self.autores=autores
        self.palabrasClaves=palabrasclaves
        self.resumen=resumen
        self.texto=texto
        
    # Definicion de los metodos get de todos los atributos de la clase
    def get_titulo(self):
        return self.titulo
    
    def get_autores(self):
        return self.autores
    
    def get_palabras(self):
        return self.palabrasclaves
    
    def get_resumen(self):
        return self.resumen
    
    def get_texto(self):
        return self.texto
    
    # Definicion de todos los set de los atributos de la clase    
    def set_titulo(self,titulo=None):
        self.titulo=titulo

    def set_autores(self,autores=None):
        self.autores=autores
    
    def set_palabras(self,palabrasclaves=None):
        self.palabrasclaves=palabrasclaves
    
    def set_resumen(self,resumen=None):
        self.resumen=resumen
    
    def set_texto(self,texto=None):
        self.texto=texto