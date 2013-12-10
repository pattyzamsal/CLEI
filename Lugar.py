'''
Created on Dec 10, 2013

@author: leddkire
'''

class MyClass(object):
    '''
    classdocs
    '''


    def __init__(self, nombre, ubicacion, capMax):
        '''
        Constructor
        '''
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.capMax = capMax

    def get_nombre(self):
        return self.__nombre


    def get_ubicacion(self):
        return self.__ubicacion


    def get_cap_max(self):
        return self.__capMax


    def set_nombre(self, value):
        self.__nombre = value


    def set_ubicacion(self, value):
        self.__ubicacion = value


    def set_cap_max(self, value):
        self.__capMax = value

    nombre = property(get_nombre, set_nombre, None, None)
    ubicacion = property(get_ubicacion, set_ubicacion, None, None)
    capMax = property(get_cap_max, set_cap_max, None, None)
        