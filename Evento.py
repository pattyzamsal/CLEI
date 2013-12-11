'''
Created on Dec 10, 2013

@author: leddkire
'''

class Evento(object):
    '''
    classdocs
    '''


    def __init__(self, titulo=None, duracion=None, fecha=None, horaInicio=None):
        '''
        Constructor
        '''
        self.titulo = titulo
        self.duracion = duracion
        self.fecha = fecha
        self.horaInicio = horaInicio



    def asignarLugar(self,lugar):
        self.lugar = lugar
        
