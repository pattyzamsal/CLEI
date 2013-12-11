'''
Created on Dec 11, 2013

@author: leddkire
'''
from Evento import Evento

class Apertura(Evento):
    '''
    classdocs
    '''


    def __init__(self, titulo,duracion,fecha,horaInicio):
        
        Evento.__init__(self, titulo, duracion, fecha, horaInicio)
        