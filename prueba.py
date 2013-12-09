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
        assert a.getTitulo()=='titulo'
        assert a.getAutores()==['patty@ldc','oscar@ldc']
        assert a.getPalabras()==['pal1','pal2']
        assert a.getResumen()=='Resumen'
        assert a.getTexto()=='Este es el texto'
        
        #Probando los set de la clase Articulos
        a.setTitulo('Desarrollo de BD en una red con IA')
        assert a.getTitulo()=='Desarrollo de BD en una red con IA'
        a.setAutores(['loco@ldc','juan@ldc'])
        assert a.getAutores()==['loco@ldc','juan@ldc']
        a.setPalabras(['Redes','BD','IA'])
        assert a.getPalabras()==['Redes','BD','IA']
        a.setResumen('Esto es un resumen')
        assert a.getResumen()=='Esto es un resumen'
        a.setTexto('Hola bienvenido al texto, aqui hablaremos de cosas')
        assert a.getTexto()=='Hola bienvenido al texto, aqui hablaremos de cosas'

    # Pruebas para la clase persona
    def testPersona(self):
        # p es una persona cualquiera para realizar la prueba
        p = Persona('nombre','apellido','correo@dominio',1010,'USB','584121147980','pagina','Venezuela')
        # Probando los get de la clase Persona
        assert p.getNombre()=='nombre'
        assert p.getApellido()=='apellido'
        assert p.getCorreo()=='correo@dominio'
        assert p.getDirPostal()==1010
        assert p.getInstitucion()=='USB'
        assert p.getTelefono()=='584121147980'
        assert p.getPagina()=='pagina'
        assert p.getPais()=='Venezuela'
        # Probando los set de la clase Persona
        p.setNombre('patty')
        assert p.getNombre()=='patty'
        p.setApellido('zambrano')
        assert p.getApellido()=='zambrano'
        p.setCorreo('patty@dominio')
        assert p.getCorreo()=='patty@dominio'
        p.setDirPostal(1040)
        assert p.getDirPostal()==1040
        p.setInstitucion('UCV')
        assert p.getInstitucion()=='UCV'
        p.setTelefono('584129904589')
        assert p.getTelefono()=='584129904589'
        p.setPagina('pagina.usb.ve')
        assert p.getPagina()=='pagina.usb.ve'
        p.setPais('Venezuela')
        assert p.getPais()=='Venezuela'
        
    # Pruebas para la clase Comite
    def testComite(self):
        # c es un miembro cualquiera del comite para realizar la prueba
        c = Comite(presidente=True,arbitro=True)
        # Probando los get de la clase Comite
        assert c.getPresidente()==True
        assert c.getArbitro()==True
        
        #Probando los set de la clase Comite
        c.setPresidente(False)
        assert c.getPresidente()==False
        c.setArbitro(False)
        assert c.getArbitro()==False

    # Pruebas para la clase Evaluacion    
    def testEvaluacion(self):
        #e es un elemento de evaluacion2
        e1=Evaluacion([4,5],'Titulo Articulo',['arb1@algo.com','arb2@algo.com','arb3@algo.com'])
        #Probando los get de la clase Evaluacion
        assert e1.getNotas()==[4,5]
        assert e1.getArticulo()=='Titulo Articulo'
        assert e1.getArbitro()==['arb1@algo.com','arb2@algo.com','arb3@algo.com']
        assert e1.getPromedio()==4.50
        
        #Probando los set de la clase
        e2=Evaluacion()
        e2.setNotas(4)
        assert e2.getNotas()==[4]
        e2.setArticulo('Juegos Locos')
        assert e2.getArticulo()=='Juegos Locos'
        e2.setArbitro('patty@ldc')
        assert e2.getArbitro()==['patty@ldc']
        # Probando los otros metodos de la clase
        e2.setArbitro('oscar@ldc')
        e2.setNotas(5)
        e2.setArbitro('loco@ldc')
        e2.setNotas(5)
        assert e2.promedioNotas()==4.67
        assert e2.aprobado()==True
        assert e2.arbitroDuplicado('patty@ldc')==True
        assert e2.arbitroDuplicado('tefi@ldc')==False
        e2.imprimirArbitros()

    # Pruebas para la clase CLEI
    def testCLEI(self):
        #c es un elemento de clei
        c=CLEI(2013,4,'Venezuela',4)
        # Probando los get de la clase CLEI
        assert c.getAnio()==2013
        assert c.getDuracion()==4
        assert c.getPais()=='Venezuela'
        assert c.getMaxArticulos()==4
        
        # Probando los set de la clase CLEI
        c.setAnio(2014)
        assert c.getAnio()==2014
        c.setDuracion(5)
        assert c.getDuracion()==5
        c.setPais('Uruguay')
        assert c.getPais()=='Uruguay'
        c.setMaxArticulos(3)
        assert c.getMaxArticulos()==3
        
        # Probando los otros metodos de la clase
        e1=Evaluacion([4,5],'Titulo Articulo',['arb1@algo.com','arb2@algo.com'])
        c.setAceptables(e1)
        e2=Evaluacion([4,5,5],'Juegos Locos',['patty@ldc','oscar@ldc','loco@ldc'])
        c.setAceptables(e2)
        e3=Evaluacion([3,3],'BD',['arb1@algo.com','patty@ldc'])
        c.setAceptables(e3)
        e4=Evaluacion([3,3],'SO',['oscar@ldc','arb2@algo.com'])
        c.setAceptables(e4)
        e5=Evaluacion([2,3],'Articulo malo',['arb1@algo.com','loco@ldc'])
        c.setAceptables(e5)
        assert c.getAceptables()==[e1,e2,e3,e4]
        assert c.calcularOcurrencia(3.00,c.aceptables)==2
        assert c.getAceptados()==[e2,e1]
        assert c.getEmpatados([e2,e1])==[e3,e4]
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testp1']
    unittest.main()