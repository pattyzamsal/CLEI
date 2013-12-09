'''
Created on Nov 18, 2013

@autores: Oscar Burguillos y Patricia Zambrano
@carnets: 09-10118 y 09-10919
'''

class Articulo:
    '''
    classdocs
    '''
    def __init__(self, titulo=None,autores=None,palabrasClaves=None,resumen=None,texto=None):
        '''
        Constructor
        '''
        self.titulo=titulo
        self.autores=autores
        self.palabrasClaves=palabrasClaves
        self.resumen=resumen
        self.texto=texto
        
    # Definicion de los metodos get de todos los atributos de la clase
    def getTitulo(self):
        return self.titulo
    
    def getAutores(self):
        return self.autores
    
    def getPalabras(self):
        return self.palabrasClaves
    
    def getResumen(self):
        return self.resumen
    
    def getTexto(self):
        return self.texto
    
    # Definicion de todos los set de los atributos de la clase    
    def setTitulo(self,titulo=None):
        self.titulo=titulo

    def setAutores(self,autores=None):
        self.autores=autores
    
    def setPalabras(self,palabrasClaves=None):
        self.palabrasClaves=palabrasClaves
    
    def setResumen(self,resumen=None):
        self.resumen=resumen
    
    def setTexto(self,texto=None):
        self.texto=texto