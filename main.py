'''
Created on Nov 22, 2013

@autores: Oscar Burguillos y Patricia Zambrano
@carnets: 09-10118 y 09-10919
'''
from CLEI import CLEI
from Evaluacion import Evaluacion
from Articulo import Articulo
from Persona import Persona
from Comite import Comite
from Autor import Autor
import sys

# Metodo que imprime las opciones del menu
def imprimirMenu():
    print "Seleccione una de las siguente opciones, presionando el numero correspondiente: "
    print "1)Crear Personas"
    print "2)Asignar Autores"
    print "3)Crear Articulos"
    print "4)Asignar miembros del Comite"
    print "5)Introducir Evaluaciones de un articulo"
    print "6)Obtener lista de ACEPTADOS"
    print "7)Obtener lista de EMPATADOS"
    print "0)Salir"

# Metodo que verifica si el usuario introduce un numero entero
def VerificacionNumero(texto):
    while True:
        try:
            numero=input(texto)
            if type(numero)==int:
                break
            else:
                print "Debe introducir numeros enteros"
                continue
        except:
            print "Debe introducir numeros"
    return numero

# Metodo que verifica si el usuario introduce un palabra vacia o un salto de linea
def VerificacionPalabra(texto):
    while True:
        valor=raw_input(texto)
        vacio=valor.replace(" " , "")
        if len(vacio)==0:
            print "Debe introducir una palabra no vacia"
            continue
        else:
            break
    return valor

# Metodo que devuelve al usuario a la opcion anterior
def Volver(centinela,texto):
    while centinela:
        continuar=raw_input(texto)
        if continuar=='1':
            break
        elif continuar=='0':
            centinela=False
        else:
            print("Debe introducir 0 'o' 1")
            continue
    return centinela

# Metodo que asigna los datos de las personas
def asignarDatosPersona(persona,correo):
    persona.setNombre(VerificacionPalabra(">>Introduzca el nombre de la persona: "))
    persona.setApellido(VerificacionPalabra(">>Introduzca el apellido de la persona: "))
    persona.setCorreo(correo)
    persona.setDirPostal(VerificacionNumero(">>Introduzca la direccion postal de la persona (numero entero): "))
    persona.setInstitucion(VerificacionPalabra(">>Introduzca la institucion a la que pertenece la persona: "))
    persona.setTelefono(VerificacionPalabra(">>Introduzca el telefono de la persona: "))
    persona.setPais(VerificacionPalabra(">>Introduzca el pais al que pertenece la persona: "))
    # Forma de asignarle al miembro la pagina web
    tienePag=True
    tienePag=Volver(tienePag,">>La persona tiene pagina web? Presione para agregarla 1 'o' 0 si no tiene: ")
    if tienePag==True:
        persona.setPagina(VerificacionPalabra(">>>Introduzca la pagina web de la persona: "))
    return persona

# Metodo que imprime los correos de los elementos de la lista de comite o de la lista de autores
def imprimirPersona(lista):
    for elemento in lista:
        print elemento.getCorreo()

#Dada una lista de personas y un correo verifica si la persona esta en la lista
def buscarPersona(lista,correo):
    for elemento in lista:
        if elemento.getCorreo()==correo:
            return True
    return False

# Metodo que asigna todos los valores de una subClase de persona
def asignarSubclase(lista,correo,subclase):
    for elemento in lista:
        if elemento.getCorreo()==correo:
            subclase.setNombre(elemento.getNombre())
            subclase.setApellido(elemento.getApellido())
            subclase.setCorreo(elemento.getCorreo())
            subclase.setDirPostal(elemento.getDirPostal())
            subclase.setInstitucion(elemento.getInstitucion())
            subclase.setTelefono(elemento.getTelefono())
            subclase.setPais(elemento.getPais())
            subclase.setPagina(elemento.getPagina())
            return subclase

# Metodo que asigna todos los datos de una instancia de articulo
def asignarArticulo(autores,articulo,titulo):
    articulo.setTitulo(titulo)
    articulo.setAutores(autores)
    # Se inicializa la lista de palabras claves
    palClaves=[]
    i=0
    # Manejo de las palabras claves por consola para verificar que la cantidad de palabras
    # claves este entre 1 y 5
    while True:
        if i>4:
            print("Usted no puede introducir mas palabras claves")
            break
        palClaves.append(VerificacionPalabra(">>Introduzca una palabra clave o presione 0 para salir: "))
        if palClaves[i]=='0':
            # Si introduce cero se saca dicho valor de la lista
            palClaves.pop()
            if i==0:
                print "Nota: Debe introducir al menos una palabra clave"
                continue
            break
        i+=1
    articulo.setPalabras(palClaves)
    articulo.setResumen(VerificacionPalabra(">>Introduzca el resumen: "))
    articulo.setTexto(VerificacionPalabra(">>Introduzca el texto: "))
    return articulo

# Metodo que imprime los titulos de los elementos de la lista de articulos
def imprimirArticulos(lista):
    for elemento in lista:
        print elemento.getTitulo()

#Dada una lista de articulos y un titulo verifica si el articulo esta en la lista
def buscarArticulo(lista,titulo):
    for elemento in lista:
        if elemento.getTitulo()==titulo:
            return True
    return False

# Metodo que asigna los arbitros y las notas de una evaluacion
def asignarEvaluacion(evaluacion,listaComite,autores):
    # Se inicializa la lista de arbitros del respectivo articulo
    arbitros=[]
    hayArb = True
    while hayArb:
        correo=VerificacionPalabra(">>Introduzca el correo del arbitro que evalua el articulo: ")
        # Se revisa si el correo del arbitro es autor del articulo a evaluar
        esAutor=VerificarAutor(autores,correo)
        esComite=buscarPersona(listaComite,correo)
        # Si es miembro del comite y es tambien es autor del articulo entonces este miembro 
        # no va a poder evaluar su propio articulo
        if esComite and esAutor:
            print "Este miembro del CP es autor del articulo, por lo tanto no se puede evaluar asi mismo."
            continue
        else:
            # Se verifica que el arbitro haya sido creado
            estaArbitro=buscarArbitro(listaComite,correo)
            if estaArbitro:
                duplicado=evaluacion.arbitroDuplicado(correo)
                # Se verifica que el arbitro no haya dado una nota previamente
                if duplicado:
                    # Si el arbitro dio una nota previamente se verifica que no haya evaluado el articulo que se esta dando
                    arbitros = evaluacion.getArbitro()
                    if arbitros.count(correo) != 0:
                        print "Este arbitro ya evaluo el articulo"
                        print "Los arbitros que han evaluado este articulo son: "
                        evaluacion.imprimirArbitros()
                        continue
                else:
                    evaluacion.setArbitro(correo)
                    # Si es un nuevo arbitro se procede a asignarle la nota al articulo
                    while True:
                        nota=VerificacionNumero(">>Introduzca la nota que dio el arbitro al articulo (numero entero): ")
                        if 1<=nota<=5:
                            evaluacion.setNotas(nota)
                            break
                        else:
                            print "Debe introducir un numero entre 1 y 5"
                            continue
            else:
                print "El arbitro correspondiente al correo no ha sido creado, los arbitros creados son:"
                imprimirPersona(listaComite)
                continue
            # Se verifica si el usuario quiere agregar otro arbitro
            hayArb=Volver(hayArb,">>Desea agregar un nuevo arbitro para este articulo? Presione para agregarlo 1 'o' 0 si no: ")
            if hayArb==False:
                break
    return evaluacion

# Metodo que busca una evaluacion que fue agregada previamente en la lista
def buscarEvaluacionPrevia(lista,articulo,evaluacion):
    for elemento in lista:
        if elemento.getArticulo()==articulo:
            evaluacion.setArticulo(elemento.getArticulo())
            for arbitro in elemento.getArbitro():
                evaluacion.setArbitro(arbitro)
            for nota in elemento.getNotas():
                evaluacion.setNotas(nota)
            return evaluacion

# Metodo que obtiene los autores de un articulo que esta dentro de la lista
def obtenerAutores(lista,titulo):
    for elemento in lista:
        if elemento.getTitulo()==titulo:
            autores=elemento.getAutores()
            return autores

# Metodo que imprime los titulos de los elementos de la lista de articulos
def imprimirEvaluaciones(lista):
    for elemento in lista:
        print elemento.getArticulo(), elemento.getArbitro(), elemento.getNotas(), elemento.getPromedio()

#Dada una lista de arbitros y un correo verifica si el arbitro esta en la lista
def buscarArbitro(lista,correo):
    for elemento in lista:
        if elemento.getCorreo()==correo:
            elemento.setArbitro(True)
            return True
    return False

#Dada una lista de evaluaciones y un articulo verifica si el articulo esta en la lista
def buscarEvaluacion(lista,articulo):
    for elemento in lista:
        if elemento.getArticulo()==articulo:
            return True
        return False

# Metodo que obtiene la posicion de la evaluacion dentro de la lista
def ObtenerPosicionEvaluacion(lista,articulo):
    i=0
    for elemento in lista:
        if elemento.getArticulo()==articulo:
            return i
        i+=1 
    return -1

# Metodo que revisa si en una lista de autores esta el correo de un autor en especifico
def VerificarAutor(autores,correo):
    for elemento in autores:
        if elemento==correo:
            return True
        return False

# Metodo que verifica que la lista no sea vacia
def VerificarLista(lista,texto):
    # Se verifica que la lista tenga al menos un elemento
    if len(lista)==0:
        print texto
        return True
    return False

if __name__ == '__main__':
    # Se crean las listas que se van a usar
    listaPersonas=[]
    listaAutores=[]
    listaArticulos=[]
    listaComite=[]
    listaEvaluaciones=[]
    listaAceptados=[]
    listaEmpatados=[]
    presidente=False
    print "Bienvenido al sistema del CLEI, por favor introduzca los datos para definir el nuevo CLEI"
    # Se piden todos los datos para formar el nuevo CLEI
    anio=VerificacionNumero("Introduzca el anio (numero entero): ")
    duracion=VerificacionNumero("Introduzca la duracion (dias): ")
    pais=VerificacionPalabra("Introduzca el pais: ")
    maximoArt=VerificacionNumero("Introduzca el maximo de articulos (numero entero): ")
    # Se crea el nuevo CLEI
    newCLEI=CLEI(anio,duracion,pais,maximoArt)
    while True:
        # Se imprime el menu del CLEI
        imprimirMenu()       
        opcion=raw_input(">")
        if opcion=='1':
            while True:
                # Se crea una nueva instancia de persona
                persona=Persona()
                # Se pide al usuario lo que seria la clave de la persona
                correo=VerificacionPalabra(">>Introduzca el correo de la persona: ")
                # Si la lista esta vacia entonces no hay ninguna persona que verificar que
                # ya se encuentre agregada en la lista
                estaPersona=False
                if len(listaPersonas)!=0:
                    # Se verefica si la persona no ha sido agregada previamente
                    estaPersona=buscarPersona(listaPersonas,correo)
                # Si la persona no esta se procede a agregarlo
                if not(estaPersona):
                    persona=asignarDatosPersona(persona,correo)
                else:
                    print "Esta persona ya fue agregada, los correos de las personas creadas son: "
                    imprimirPersona(listaPersonas)
                    continue                   
                # Se agrega la persona a la lista de personas
                listaPersonas.append(persona)
                # Se verifica si el usuario quiere volver al menu
                centinela=True
                centinela=Volver(centinela,">>Presione 1 si desea introducir otra persona, 0 si desea volver al menu: ")
                if centinela==False:
                    break
               
        elif opcion=='2':
            esVacia=VerificarLista(listaPersonas,"Debe crear las personas primero (opcion 1)")
            if esVacia:
                continue
            while True:
                # Se crea una nueva instancia de autor
                autor=Autor()
                # Se pide al usuario lo que seria la clave del autor
                correo=VerificacionPalabra(">>Introduzca el correo del autor: ")
                # Se verefica si el autor ya fue creado como una persona
                estaPersona=buscarPersona(listaPersonas,correo)
                # Si fue creado como persona se procede a agregarlo como autor
                if estaPersona:
                    # Si la lista esta vacia entonces no hay ningun autor que verificar que
                    # ya se encuentre agregado en la lista
                    estaAutor=False
                    # Si la lista de autores esta vacia se procede a crearlo
                    if len(listaAutores)!=0:
                        # Se verefica si el autor no ha sido agregado previamente
                        estaAutor=buscarPersona(listaAutores,correo)
                    # Si el autor no esta se procede a agregarlo
                    if not(estaAutor):
                        autor=asignarSubclase(listaPersonas,correo,autor)
                    else:
                        print "Este autor ya fue agregado, los autores creados son: "
                        imprimirPersona(listaAutores)
                        continue
                    # Se agrega el autor a la lista de autores
                    listaAutores.append(autor)
                    # Se verifica si el usuario quiere volver al menu
                    centinela=True
                    centinela=Volver(centinela,">>Presione 1 si desea introducir otro autor, 0 si desea volver al menu: ")
                    if centinela==False:
                        break
                else:
                    print "Este correo del autor no ha sido agregado como persona, creelo en la opcion 1 del menu."
                    print "Los correos de las personas creadas son: "
                    imprimirPersona(listaPersonas)
                    break

        elif opcion=='3':
            esVacia=VerificarLista(listaAutores,"Debe crear los autores primero (opcion 2)")
            if esVacia:
                continue
            while True:
                # Se crea una nueva instancia de articulo
                articulo=Articulo()
                # Se pide al usuario el titulo del articulo
                titulo=VerificacionPalabra(">>Introduzca el titulo del articulo: ")
                # Si la lista esta vacia entonces no hay ningun articulo que verificar que
                # ya se encuentre agregado en la lista
                estaArticulo=False
                if len(listaArticulos)!=0:
                    estaArticulo=buscarArticulo(listaArticulos,titulo)
                if not(estaArticulo):
                    # Se inicializa la lista de autores del respectivo articulo
                    autores=[]
                    hayAutor=True
                    # Forma de asignar los autores del articulo
                    while hayAutor:
                        # Se pide el correo del autor
                        correo=VerificacionPalabra(">>Introduzca el correo del autor del articulo: ")
                        # Se verefica si el autor no ha sido agregado como persona previamente
                        estaAutor=buscarPersona(listaAutores,correo)
                        if estaAutor:
                            autores.append(correo)
                            # Se verifica si el usuario quiere volver al menu
                            centinela=True
                            centinela=Volver(centinela,">>Presione 1 si desea introducir otro autor para el articulo, 0 si desea agregar los otros datos del articulo: ")
                            if centinela==False:
                                break                                           
                        else:
                            print "El autor no ha sido creado, creelo en la opcion 2 del menu."
                            print "Los autores creados son:"
                            imprimirPersona(listaAutores)
                            hayAutor=False
                    # Si el autor esta se procede a asignarlo como autor del articulo
                    if hayAutor:
                        # Se asignan todos los valores del articulo
                        articulo=asignarArticulo(autores,articulo,titulo)
                        # Se agrega el articulo a la listaArticulos
                        listaArticulos.append(articulo)
                        # Se verifica si el usuario quiere volver al menu
                        centinela=True
                        centinela=Volver(centinela,">>Presione 1 si desea introducir otro articulo, 0 si desea volver al menu: ")
                        if centinela==False:
                            break                    
                    else:
                        break
                else:
                    print "Este articulo ya ha sido agregado."
                    print "Los articulos creados son: "
                    imprimirArticulos(listaArticulos)
                    continue
                    
        elif opcion=='4':
            esVacia=VerificarLista(listaPersonas,"Debe crear las personas primero (opcion 1)")
            if esVacia:
                continue
            while True:
                # Se crea una nueva instancia de comite, osea un nuevo miembro
                miembroCP=Comite()
                # Se pide al usuario lo que seria la clave del miembro del comite
                correo=VerificacionPalabra(">>Introduzca el correo del miembro del comite: ")
                # Se verefica si el miembro del comite ya fue creado como una persona
                estaPersona=buscarPersona(listaPersonas,correo)
                # Si fue creado como persona se procede a agregarlo como miembro del comite
                if estaPersona:
                    # Si la lista esta vacia entonces no hay ningun miembro del comite que 
                    # verificar que ya se encuentre agregado en la lista
                    estaComite=False
                    # Si la lista de autores esta vacia se procede a crearlo
                    if len(listaComite)!=0:
                        # Se verefica si el miembro del comite no ha sido agregado previamente
                        estaComite=buscarPersona(listaComite,correo)
                    # Si el miembro del comite no esta se procede a agregarlo
                    if not(estaComite):
                        miembroCP=asignarSubclase(listaPersonas,correo,miembroCP)
                    else:
                        print "Este miembro del comite ya fue agregado, los miembros del comite creados son: "
                        imprimirPersona(listaComite)
                        continue
                    # Se pregunta si el miembro del comite va a ser el presidente del mismo, esto lo hara mientras no se haya asignado a alguien
                    # y cuando se asigne a alguien ya no se podra entrar a esta parte del codigo
                    while presidente==False:
                        print "Si elige a este miembro como el presidente debe tener en cuenta que ya no podra cambiarlo"
                        esPresi=raw_input(">>Este miembro es el presidente del comite? Presione para agregarlo 1 'o' 0 si no lo es: ")
                        if esPresi=='1':
                            miembroCP.setPresidente(True)
                            presidente=True
                            break
                        elif esPresi=='0':
                            break
                        else:
                            print("Debe introducir 0 'o' 1")
                            continue
                    #Se agrega el miebro del comite a la listaComite
                    listaComite.append(miembroCP)
                    # Se verifica si el usuario quiere volver al menu
                    centinela=True
                    centinela=Volver(centinela,">>Presione 1 si desea introducir otro miembro del comite, 0 si desea volver al menu: ")
                    if centinela==False:
                        break
                else:
                    print "Este miembro del comite no ha sido agregado como persona, creelo en la opcion 1 del menu."
                    print "Las personas creadas son: "
                    imprimirPersona(listaPersonas)
                    break
                
        elif opcion=='5':
            esVacia=VerificarLista(listaArticulos,"Debe crear los articulos primero (opcion 3)")
            if esVacia:
                continue
            esVacio=VerificarLista(listaComite,"Debe crear los miembros del comite primero (opcion 4)")
            if esVacio:
                continue
            while True:
                # Se crea una nueva instancia de una evaluacion para un articulo
                evaluacion=Evaluacion([],None,[])
                titulo=VerificacionPalabra(">>Introduzca el titulo del articulo: ")
                # Se verifica que el articulo haya sido creado
                estaTitulo=buscarArticulo(listaArticulos, titulo)
                if estaTitulo:
                    autores=[]
                    autores=obtenerAutores(listaArticulos,titulo)
                    # Si la lista esta vacia entonces no hay ninguna evaluacion que 
                    # verificar que ya se encuentre agregada en la lista
                    estaArticulo=False
                    # Si la lista de autores esta vacia se procede a crearlo
                    if len(listaEvaluaciones)!=0:
                        # Se verefica si la evaluacion no ha sido agregada previamente
                        estaArticulo=buscarEvaluacion(listaEvaluaciones,titulo)
                    # Si la evaluacion no esta se procede a agregarlo
                    if not(estaArticulo):
                        evaluacion.setArticulo(titulo)
                    else:
                        evaluacion=buscarEvaluacionPrevia(listaEvaluaciones,titulo,evaluacion)
                        # Se obtiene la posicion del elemento en la lista
                        posicion=ObtenerPosicionEvaluacion(listaEvaluaciones,titulo)
                        # Se elimina la evaluacion previa de la lista de evaluaciones
                        borrar=listaEvaluaciones.pop(posicion)
                    # Se asignan los valores restantes para la evaluacion
                    evaluacion=asignarEvaluacion(evaluacion,listaComite,autores)
                else:
                    print "El articulo no ha sido creado, los articulo disponibles son: "
                    imprimirArticulos(listaArticulos)
                    continue
                # Se agrega la evaluacion a la lista de evaluaciones
                listaEvaluaciones.append(evaluacion)
                # Se verifica si el usuario quiere volver al menu
                centinela=True
                centinela=Volver(centinela,">>Presione 1 si desea introducir otra evaluacion a otro articulo, 0 si desea volver al menu: ")
                if centinela==False:
                    break

        elif opcion=='6':
            esVacia=VerificarLista(listaEvaluaciones,"Debe crear las evaluaciones primero (opcion 5)")
            if esVacia:
                continue
            for elemento in listaEvaluaciones:
                newCLEI.setAceptables(elemento)
            listaAceptados=newCLEI.getAceptados()
            for elemento in listaAceptados:
                print elemento.getArticulo()
                
        elif opcion=='7':
            esVacia=VerificarLista(listaEvaluaciones,"Debe crear las evaluaciones primero (opcion 5)")
            if esVacia:
                continue
            esVacio=VerificarLista(listaAceptados,"Debe crear la lista de aceptados primero (opcion 6)")
            if esVacio:
                continue
            else:
                listaEmpatados=newCLEI.getEmpatados(listaAceptados)
                for elemento in listaEmpatados:
                    print elemento.getArticulo()
                    
        elif opcion=='0':
            print "Usted salio del sistema del CLEI"
            sys.exit()
            
        else:
            print "Usted debe presionar un numero entre 0 y 7"
            continue