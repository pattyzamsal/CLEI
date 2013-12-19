'''
Created on Nov 20, 2013

@autores: Oscar Burguillos y Patricia Zambrano
@carnets: 09-10118 y 09-10919
'''
import unittest
from Articulo import *
from Comite import *
from CLEI import *

class Test(unittest.TestCase):

    # Pruebas para la clase articulos
    def testArticulo(self):
        #a es un articulo cualquier para realizar la prueba
        a= Articulo('titulo',['patty@ldc','oscar@ldc'],['pal1','pal2'],'Resumen','Este es el texto')
        #Probando los get de la clase Articulos
        assert a.get_titulo()=='titulo'
        assert a.get_autores()==['patty@ldc','oscar@ldc']
        assert a.get_palabras()==['pal1','pal2']
        assert a.get_resumen()=='Resumen'
        assert a.get_texto()=='Este es el texto'
        
        #Probando los set de la clase Articulos
        a.set_titulo('Desarrollo de BD en una red con IA')
        assert a.get_titulo()=='Desarrollo de BD en una red con IA'
        a.set_autores(['loco@ldc','juan@ldc'])
        assert a.get_autores()==['loco@ldc','juan@ldc']
        a.set_palabras(['Redes','BD','IA'])
        assert a.get_palabras()==['Redes','BD','IA']
        a.set_resumen('Esto es un resumen')
        assert a.get_resumen()=='Esto es un resumen'
        a.set_texto('Hola bienvenido al texto, aqui hablaremos de cosas')
        assert a.get_texto()=='Hola bienvenido al texto, aqui hablaremos de cosas'

    # Pruebas para la clase persona
    def testPersona(self):
        # p es una persona cualquiera para realizar la prueba
        p = Persona('nombre','apellido','correo@dominio',1010,'USB','584121147980','pagina','Venezuela')
        # Probando los get de la clase Persona
        assert p.get_nombre()=='nombre'
        assert p.get_apellido()=='apellido'
        assert p.get_correo()=='correo@dominio'
        assert p.get_dirpostal()==1010
        assert p.get_institucion()=='USB'
        assert p.get_telefono()=='584121147980'
        assert p.get_pagina()=='pagina'
        assert p.get_pais()=='Venezuela'
        # Probando los set de la clase Persona
        p.set_nombre('patty')
        assert p.get_nombre()=='patty'
        p.set_apellido('zambrano')
        assert p.get_apellido()=='zambrano'
        p.set_correo('patty@dominio')
        assert p.get_correo()=='patty@dominio'
        p.set_dirpostal(1040)
        assert p.get_dirpostal()==1040
        p.set_institucion('UCV')
        assert p.get_institucion()=='UCV'
        p.set_telefono('584129904589')
        assert p.get_telefono()=='584129904589'
        p.set_pagina('pagina.usb.ve')
        assert p.get_pagina()=='pagina.usb.ve'
        p.set_pais('Venezuela')
        assert p.get_pais()=='Venezuela'
        
    # Pruebas para la clase Comite
    def testComite(self):
        # c es un miembro cualquiera del comite para realizar la prueba
        c = Comite(presidente=True,arbitro=True)
        # Probando los get de la clase Comite
        assert c.get_presidente()==True
        assert c.get_arbitro()==True
        
        #Probando los set de la clase Comite
        c.set_presidente(False)
        assert c.get_presidente()==False
        c.set_arbitro(False)
        assert c.get_arbitro()==False

    # Pruebas para la clase Evaluacion    
    def testEvaluacion(self):
        #e es un elemento de evaluacion2
        e1=Evaluacion([4,5],'Titulo Articulo',['arb1@algo.com','arb2@algo.com','arb3@algo.com'])
        #Probando los get de la clase Evaluacion
        assert e1.get_notas()==[4,5]
        assert e1.get_articulo()=='Titulo Articulo'
        assert e1.get_arbitro()==['arb1@algo.com','arb2@algo.com','arb3@algo.com']
        assert e1.get_promedio()==4.50
        
        #Probando los set de la clase
        e2=Evaluacion()
        e2.set_notas(4)
        assert e2.get_notas()==[4]
        e2.set_articulo('Juegos Locos')
        assert e2.get_articulo()=='Juegos Locos'
        e2.set_arbitro('patty@ldc')
        assert e2.get_arbitro()==['patty@ldc']
        # Probando los otros metodos de la clase
        e2.set_arbitro('oscar@ldc')
        e2.set_notas(5)
        e2.set_arbitro('loco@ldc')
        e2.set_notas(5)
        assert e2.promedio_notas()==4.67
        assert e2.aprobado()==True
        assert e2.arbitro_duplicado('patty@ldc')==True
        assert e2.arbitro_duplicado('tefi@ldc')==False
        e2.imprimir_arbitros()

    # Pruebas para la clase CLEI
    def testCLEI(self):
        #c es un elemento de clei
        c=CLEI(2013,4,'Venezuela',4)
        # Probando los get de la clase CLEI
        assert c.get_anio()==2013
        assert c.get_duracion()==4
        assert c.get_pais()=='Venezuela'
        assert c.get_maxarticulos()==4
        
        # Probando los set de la clase CLEI
        c.set_anio(2014)
        assert c.get_anio()==2014
        c.set_duracion(5)
        assert c.get_duracion()==5
        c.set_pais('Uruguay')
        assert c.get_pais()=='Uruguay'
        c.set_maxarticulos(3)
        assert c.get_maxarticulos()==3
        
        # Probando los otros metodos de la clase
        e1=Evaluacion([4,5],'Titulo Articulo',['arb1@algo.com','arb2@algo.com'])
        c.set_aceptables(e1)
        e2=Evaluacion([4,5,5],'Juegos Locos',['patty@ldc','oscar@ldc','loco@ldc'])
        c.set_aceptables(e2)
        e3=Evaluacion([3,3],'BD',['arb1@algo.com','patty@ldc'])
        c.set_aceptables(e3)
        e4=Evaluacion([3,3],'SO',['oscar@ldc','arb2@algo.com'])
        c.set_aceptables(e4)
        e5=Evaluacion([2,3],'Articulo malo',['arb1@algo.com','loco@ldc'])
        c.set_aceptables(e5)
        assert c.get_aceptables()==[e1,e2,e3,e4]
        assert c.calcular_ocurrencia(3.00,c.aceptables)==2
        assert c.get_aceptados()==[e2,e1]
        assert c.get_empatados([e2,e1])==[e3,e4]
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testp1']
    unittest.main()