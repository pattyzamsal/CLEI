'''
Created on Dec 10, 2013

@author: leddkire
'''

class MyClass(object):
    '''
    classdocs
    '''


    def __init__(self, titulo, duracion, fecha, horaInicio):
        '''
        Constructor
        '''
        self.titulo = titulo
        self.duracion = duracion
        self.fecha = fecha
        self.horaInicio = horaInicio

    def get_titulo(self):
        return self.__titulo


    def get_duracion(self):
        return self.__duracion


    def get_fecha(self):
        return self.__fecha


    def get_hora_inicio(self):
        return self.__horaInicio


    def set_titulo(self, value):
        self.__titulo = value


    def set_duracion(self, value):
        self.__duracion = value


    def set_fecha(self, value):
        self.__fecha = value


    def set_hora_inicio(self, value):
        self.__horaInicio = value

    titulo = property(get_titulo, set_titulo, None, None)
    duracion = property(get_duracion, set_duracion, None, None)
    fecha = property(get_fecha, set_fecha, None, None)
    horaInicio = property(get_hora_inicio, set_hora_inicio, None, None)
        