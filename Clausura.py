'''
Created on Dec 11, 2013

@author: leddkire
'''
from Evento import Evento

class Clausura(Evento):
    '''
    classdocs
    '''


    def __init__(self, titulo=None, duracion=None, fecha=None, horaInicio=None):
        '''
        Constructor
        '''
        Evento.__init__(self, titulo, duracion, fecha, horaInicio)
        