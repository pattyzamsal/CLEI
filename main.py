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
def imprimir_menu():
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
def verificacion_numero(texto):
    while True:
        try:
            numero=input(texto)
            if type(numero)==int and numero>=0:
                break
            else:
                print "Debe introducir numeros enteros positivos"
                continue
        except:
            print "Debe introducir numeros"
    return numero

# Metodo que verifica si el usuario introduce un palabra vacia o un salto de linea
def verificacion_palabra(texto):
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
def volver(centinela,texto):
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
def asignar_datos_persona(persona,correo):
    persona.set_nombre(verificacion_palabra(">>Introduzca el nombre de la persona: "))
    persona.set_apellido(verificacion_palabra(">>Introduzca el apellido de la persona: "))
    persona.set_correo(correo)
    persona.set_dirpostal(verificacion_numero(">>Introduzca la direccion postal de la persona (numero entero): "))
    persona.set_institucion(verificacion_palabra(">>Introduzca la institucion a la que pertenece la persona: "))
    persona.set_telefono(verificacion_palabra(">>Introduzca el telefono de la persona: "))
    persona.set_pais(verificacion_palabra(">>Introduzca el pais al que pertenece la persona: "))
    # Forma de asignarle al miembro la pagina web
    tienepag=True
    tienepag=volver(tienepag,">>La persona tiene pagina web? Presione para agregarla 1 'o' 0 si no tiene: ")
    if tienepag==True:
        persona.set_pagina(verificacion_palabra(">>>Introduzca la pagina web de la persona: "))
    return persona

# Metodo que imprime los correos de los elementos de la lista de comite o de la lista de autores
def imprimir_persona(lista):
    for elemento in lista:
        print elemento.get_correo()

#Dada una lista de personas y un correo verifica si la persona esta en la lista
def buscar_persona(lista,correo):
    for elemento in lista:
        if elemento.get_correo()==correo:
            return True
    return False

# Metodo que asigna todos los valores de una subClase de persona
def asignar_subclase(lista,correo,subclase):
    for elemento in lista:
        if elemento.get_correo()==correo:
            subclase.set_nombre(elemento.get_nombre())
            subclase.set_apellido(elemento.get_apellido())
            subclase.set_correo(elemento.get_correo())
            subclase.set_dirpostal(elemento.get_dirpostal())
            subclase.set_institucion(elemento.get_institucion())
            subclase.set_telefono(elemento.get_telefono())
            subclase.set_pais(elemento.get_pais())
            subclase.set_pagina(elemento.get_pagina())
            return subclase

# Metodo que asigna todos los datos de una instancia de articulo
def asignar_articulo(autores,articulo,titulo):
    articulo.set_titulo(titulo)
    articulo.set_autores(autores)
    # Se inicializa la lista de palabras claves
    palclaves=[]
    i=0
    # Manejo de las palabras claves por consola para verificar que la cantidad de palabras
    # claves este entre 1 y 5
    while True:
        if i>4:
            print("Usted no puede introducir mas palabras claves")
            break
        palclaves.append(verificacion_palabra(">>Introduzca una palabra clave o presione 0 para salir: "))
        if palclaves[i]=='0':
            # Si introduce cero se saca dicho valor de la lista
            palclaves.pop()
            if i==0:
                print "Nota: Debe introducir al menos una palabra clave"
                continue
            break
        i+=1
    articulo.set_palabras(palclaves)
    articulo.set_resumen(verificacion_palabra(">>Introduzca el resumen: "))
    articulo.set_texto(verificacion_palabra(">>Introduzca el texto: "))
    return articulo

# Metodo que imprime los titulos de los elementos de la lista de articulos
def imprimir_articulos(lista):
    for elemento in lista:
        print elemento.get_titulo()

#Dada una lista de articulos y un titulo verifica si el articulo esta en la lista
def buscar_articulo(lista,titulo):
    for elemento in lista:
        if elemento.get_titulo()==titulo:
            return True
    return False

# Metodo que asigna los arbitros y las notas de una evaluacion
def asignar_evaluacion(evaluacion,listacomite,autores):
    # Se inicializa la lista de arbitros del respectivo articulo
    arbitros=[]
    hayarb = True
    while hayarb:
        correo=verificacion_palabra(">>Introduzca el correo del arbitro que evalua el articulo: ")
        # Se revisa si el correo del arbitro es autor del articulo a evaluar
        esautor=verificar_autor(autores,correo)
        escomite=buscar_persona(listacomite,correo)
        # Si es miembro del comite y es tambien es autor del articulo entonces este miembro 
        # no va a poder evaluar su propio articulo
        if escomite and esautor:
            print "Este miembro del CP es autor del articulo, por lo tanto no se puede evaluar asi mismo."
            continue
        else:
            # Se verifica que el arbitro haya sido creado
            estaarbitro=buscar_arbitro(listacomite,correo)
            if estaarbitro:
                duplicado=evaluacion.arbitro_duplicado(correo)
                # Se verifica que el arbitro no haya dado una nota previamente
                if duplicado:
                    # Si el arbitro dio una nota previamente se verifica que no haya evaluado el articulo que se esta dando
                    arbitros = evaluacion.get_arbitro()
                    if arbitros.count(correo) != 0:
                        print "Este arbitro ya evaluo el articulo"
                        print "Los arbitros que han evaluado este articulo son: "
                        evaluacion.imprimir_arbitros()
                        continue
                else:
                    evaluacion.set_arbitro(correo)
                    # Si es un nuevo arbitro se procede a asignarle la nota al articulo
                    while True:
                        nota=verificacion_numero(">>Introduzca la nota que dio el arbitro al articulo (numero entero): ")
                        if 1<=nota<=5:
                            evaluacion.set_notas(nota)
                            break
                        else:
                            print "Debe introducir un numero entre 1 y 5"
                            continue
            else:
                print "El arbitro correspondiente al correo no ha sido creado, los arbitros creados son:"
                imprimir_persona(listacomite)
                continue
            # Se verifica si el usuario quiere agregar otro arbitro
            hayarb=volver(hayarb,">>Desea agregar un nuevo arbitro para este articulo? Presione para agregarlo 1 'o' 0 si no: ")
            if hayarb==False:
                break
    return evaluacion

# Metodo que busca una evaluacion que fue agregada previamente en la lista
def buscar_evaluacion_previa(lista,articulo,evaluacion):
    for elemento in lista:
        if elemento.get_articulo()==articulo:
            evaluacion.set_articulo(elemento.get_articulo())
            for arbitro in elemento.get_arbitro():
                evaluacion.set_arbitro(arbitro)
            for nota in elemento.get_notas():
                evaluacion.set_notas(nota)
            return evaluacion

# Metodo que obtiene los autores de un articulo que esta dentro de la lista
def obtener_autores(lista,titulo):
    for elemento in lista:
        if elemento.get_titulo()==titulo:
            autores=elemento.get_autores()
            return autores

# Metodo que imprime los titulos de los elementos de la lista de articulos
def imprimir_evaluaciones(lista):
    for elemento in lista:
        print elemento.get_articulo(), elemento.get_arbitro(), elemento.get_notas(), elemento.get_promedio()

#Dada una lista de arbitros y un correo verifica si el arbitro esta en la lista
def buscar_arbitro(lista,correo):
    for elemento in lista:
        if elemento.get_correo()==correo:
            elemento.set_arbitro(True)
            return True
    return False

#Dada una lista de evaluaciones y un articulo verifica si el articulo esta en la lista
def buscar_evaluacion(lista,articulo):
    for elemento in lista:
        if elemento.get_articulo()==articulo:
            return True
        return False

# Metodo que obtiene la posicion de la evaluacion dentro de la lista
def obtener_posicion_evaluacion(lista,articulo):
    i=0
    for elemento in lista:
        if elemento.get_articulo()==articulo:
            return i
        i+=1 
    return -1

# Metodo que revisa si en una lista de autores esta el correo de un autor en especifico
def verificar_autor(autores,correo):
    for elemento in autores:
        if elemento==correo:
            return True
        return False

# Metodo que verifica que la lista no sea vacia
def verificar_lista(lista,texto):
    # Se verifica que la lista tenga al menos un elemento
    if len(lista)==0:
        print texto
        return True
    return False

if __name__ == '__main__':
    # Se crean las listas que se van a usar
    listapersonas=[]
    listaautores=[]
    listaarticulos=[]
    listacomite=[]
    listaevaluaciones=[]
    listaaceptados=[]
    listaempatados=[]
    presidente=False
    print "Bienvenido al sistema del CLEI, por favor introduzca los datos para definir el nuevo CLEI"
    # Se piden todos los datos para formar el nuevo CLEI
    anio=verificacion_numero("Introduzca el anio (numero entero): ")
    duracion=verificacion_numero("Introduzca la duracion (dias): ")
    pais=verificacion_palabra("Introduzca el pais: ")
    maximoart=verificacion_numero("Introduzca el maximo de articulos (numero entero): ")
    # Se crea el nuevo CLEI
    newCLEI=CLEI(anio,duracion,pais,maximoart)
    while True:
        # Se imprime el menu del CLEI
        imprimir_menu()       
        opcion=raw_input(">")
        if opcion=='1':
            while True:
                # Se crea una nueva instancia de persona
                persona=Persona()
                # Se pide al usuario lo que seria la clave de la persona
                correo=verificacion_palabra(">>Introduzca el correo de la persona: ")
                # Si la lista esta vacia entonces no hay ninguna persona que verificar que
                # ya se encuentre agregada en la lista
                estapersona=False
                if len(listapersonas)!=0:
                    # Se verefica si la persona no ha sido agregada previamente
                    estapersona=buscar_persona(listapersonas,correo)
                # Si la persona no esta se procede a agregarlo
                if not(estapersona):
                    persona=asignar_datos_persona(persona,correo)
                else:
                    print "Esta persona ya fue agregada, los correos de las personas creadas son: "
                    imprimir_persona(listapersonas)
                    continue                   
                # Se agrega la persona a la lista de personas
                listapersonas.append(persona)
                # Se verifica si el usuario quiere volver al menu
                centinela=True
                centinela=volver(centinela,">>Presione 1 si desea introducir otra persona, 0 si desea volver al menu: ")
                if centinela==False:
                    break
               
        elif opcion=='2':
            esvacia=verificar_lista(listapersonas,"Debe crear las personas primero (opcion 1)")
            if esvacia:
                continue
            while True:
                # Se crea una nueva instancia de autor
                autor=Autor()
                # Se pide al usuario lo que seria la clave del autor
                correo=verificacion_palabra(">>Introduzca el correo del autor: ")
                # Se verefica si el autor ya fue creado como una persona
                estapersona=buscar_persona(listapersonas,correo)
                # Si fue creado como persona se procede a agregarlo como autor
                if estapersona:
                    # Si la lista esta vacia entonces no hay ningun autor que verificar que
                    # ya se encuentre agregado en la lista
                    estaautor=False
                    # Si la lista de autores esta vacia se procede a crearlo
                    if len(listaautores)!=0:
                        # Se verefica si el autor no ha sido agregado previamente
                        estaautor=buscar_persona(listaautores,correo)
                    # Si el autor no esta se procede a agregarlo
                    if not(estaautor):
                        autor=asignar_subclase(listapersonas,correo,autor)
                    else:
                        print "Este autor ya fue agregado, los autores creados son: "
                        imprimir_persona(listaautores)
                        continue
                    # Se agrega el autor a la lista de autores
                    listaautores.append(autor)
                    # Se verifica si el usuario quiere volver al menu
                    centinela=True
                    centinela=volver(centinela,">>Presione 1 si desea introducir otro autor, 0 si desea volver al menu: ")
                    if centinela==False:
                        break
                else:
                    print "Este correo del autor no ha sido agregado como persona, creelo en la opcion 1 del menu."
                    print "Los correos de las personas creadas son: "
                    imprimir_persona(listapersonas)
                    break

        elif opcion=='3':
            esvacia=verificar_lista(listaautores,"Debe crear los autores primero (opcion 2)")
            if esvacia:
                continue
            while True:
                # Se crea una nueva instancia de articulo
                articulo=Articulo()
                # Se pide al usuario el titulo del articulo
                titulo=verificacion_palabra(">>Introduzca el titulo del articulo: ")
                # Si la lista esta vacia entonces no hay ningun articulo que verificar que
                # ya se encuentre agregado en la lista
                estaarticulo=False
                if len(listaarticulos)!=0:
                    estaarticulo=buscar_articulo(listaarticulos,titulo)
                if not(estaarticulo):
                    # Se inicializa la lista de autores del respectivo articulo
                    autores=[]
                    hayautor=True
                    # Forma de asignar los autores del articulo
                    while hayautor:
                        # Se pide el correo del autor
                        correo=verificacion_palabra(">>Introduzca el correo del autor del articulo: ")
                        # Se verefica si el autor no ha sido agregado como persona previamente
                        estaautor=buscar_persona(listaautores,correo)
                        if estaautor:
                            autores.append(correo)
                            # Se verifica si el usuario quiere volver al menu
                            centinela=True
                            centinela=volver(centinela,">>Presione 1 si desea introducir otro autor para el articulo, 0 si desea agregar los otros datos del articulo: ")
                            if centinela==False:
                                break                                           
                        else:
                            print "El autor no ha sido creado, creelo en la opcion 2 del menu."
                            print "Los autores creados son:"
                            imprimir_persona(listaautores)
                            hayautor=False
                    # Si el autor esta se procede a asignarlo como autor del articulo
                    if hayautor:
                        # Se asignan todos los valores del articulo
                        articulo=asignar_articulo(autores,articulo,titulo)
                        # Se agrega el articulo a la listaArticulos
                        listaarticulos.append(articulo)
                        # Se verifica si el usuario quiere volver al menu
                        centinela=True
                        centinela=volver(centinela,">>Presione 1 si desea introducir otro articulo, 0 si desea volver al menu: ")
                        if centinela==False:
                            break                    
                    else:
                        break
                else:
                    print "Este articulo ya ha sido agregado."
                    print "Los articulos creados son: "
                    imprimir_articulos(listaarticulos)
                    continue
                    
        elif opcion=='4':
            esvacia=verificar_lista(listapersonas,"Debe crear las personas primero (opcion 1)")
            if esvacia:
                continue
            while True:
                # Se crea una nueva instancia de comite, osea un nuevo miembro
                miembroCP=Comite()
                # Se pide al usuario lo que seria la clave del miembro del comite
                correo=verificacion_palabra(">>Introduzca el correo del miembro del comite: ")
                # Se verefica si el miembro del comite ya fue creado como una persona
                estapersona=buscar_persona(listapersonas,correo)
                # Si fue creado como persona se procede a agregarlo como miembro del comite
                if estapersona:
                    # Si la lista esta vacia entonces no hay ningun miembro del comite que 
                    # verificar que ya se encuentre agregado en la lista
                    estacomite=False
                    # Si la lista de autores esta vacia se procede a crearlo
                    if len(listacomite)!=0:
                        # Se verefica si el miembro del comite no ha sido agregado previamente
                        estacomite=buscar_persona(listacomite,correo)
                    # Si el miembro del comite no esta se procede a agregarlo
                    if not(estacomite):
                        miembroCP=asignar_subclase(listapersonas,correo,miembroCP)
                    else:
                        print "Este miembro del comite ya fue agregado, los miembros del comite creados son: "
                        imprimir_persona(listacomite)
                        continue
                    # Se pregunta si el miembro del comite va a ser el presidente del mismo, esto lo hara mientras no se haya asignado a alguien
                    # y cuando se asigne a alguien ya no se podra entrar a esta parte del codigo
                    while presidente==False:
                        print "Si elige a este miembro como el presidente debe tener en cuenta que ya no podra cambiarlo"
                        espresi=raw_input(">>Este miembro es el presidente del comite? Presione para agregarlo 1 'o' 0 si no lo es: ")
                        if espresi=='1':
                            miembroCP.set_presidente(True)
                            presidente=True
                            break
                        elif espresi=='0':
                            break
                        else:
                            print("Debe introducir 0 'o' 1")
                            continue
                    #Se agrega el miebro del comite a la listaComite
                    listacomite.append(miembroCP)
                    # Se verifica si el usuario quiere volver al menu
                    centinela=True
                    centinela=volver(centinela,">>Presione 1 si desea introducir otro miembro del comite, 0 si desea volver al menu: ")
                    if centinela==False:
                        break
                else:
                    print "Este miembro del comite no ha sido agregado como persona, creelo en la opcion 1 del menu."
                    print "Las personas creadas son: "
                    imprimir_persona(listapersonas)
                    break
                
        elif opcion=='5':
            esvacia=verificar_lista(listaarticulos,"Debe crear los articulos primero (opcion 3)")
            if esvacia:
                continue
            esvacio=verificar_lista(listacomite,"Debe crear los miembros del comite primero (opcion 4)")
            if esvacio:
                continue
            while True:
                # Se crea una nueva instancia de una evaluacion para un articulo
                evaluacion=Evaluacion([],None,[])
                titulo=verificacion_palabra(">>Introduzca el titulo del articulo: ")
                # Se verifica que el articulo haya sido creado
                estatitulo=buscar_articulo(listaarticulos, titulo)
                if estatitulo:
                    autores=[]
                    autores=obtener_autores(listaarticulos,titulo)
                    # Si la lista esta vacia entonces no hay ninguna evaluacion que 
                    # verificar que ya se encuentre agregada en la lista
                    estaarticulo=False
                    # Si la lista de autores esta vacia se procede a crearlo
                    if len(listaevaluaciones)!=0:
                        # Se verefica si la evaluacion no ha sido agregada previamente
                        estaarticulo=buscar_evaluacion(listaevaluaciones,titulo)
                    # Si la evaluacion no esta se procede a agregarlo
                    if not(estaarticulo):
                        evaluacion.set_articulo(titulo)
                    else:
                        evaluacion=buscar_evaluacion_previa(listaevaluaciones,titulo,evaluacion)
                        # Se obtiene la posicion del elemento en la lista
                        posicion=obtener_posicion_evaluacion(listaevaluaciones,titulo)
                        # Se elimina la evaluacion previa de la lista de evaluaciones
                        borrar=listaevaluaciones.pop(posicion)
                    # Se asignan los valores restantes para la evaluacion
                    evaluacion=asignar_evaluacion(evaluacion,listacomite,autores)
                else:
                    print "El articulo no ha sido creado, los articulo disponibles son: "
                    imprimir_articulos(listaarticulos)
                    continue
                # Se agrega la evaluacion a la lista de evaluaciones
                listaevaluaciones.append(evaluacion)
                # Se verifica si el usuario quiere volver al menu
                centinela=True
                centinela=volver(centinela,">>Presione 1 si desea introducir otra evaluacion a otro articulo, 0 si desea volver al menu: ")
                if centinela==False:
                    break

        elif opcion=='6':
            esvacia=verificar_lista(listaevaluaciones,"Debe crear las evaluaciones primero (opcion 5)")
            if esvacia:
                continue
            for elemento in listaevaluaciones:
                newCLEI.set_aceptables(elemento)
            listaaceptados=newCLEI.get_aceptados()
            for elemento in listaaceptados:
                print elemento.get_articulo()
                
        elif opcion=='7':
            esvacia=verificar_lista(listaevaluaciones,"Debe crear las evaluaciones primero (opcion 5)")
            if esvacia:
                continue
            esvacio=verificar_lista(listaaceptados,"Debe crear la lista de aceptados primero (opcion 6)")
            if esvacio:
                continue
            else:
                listaempatados=newCLEI.get_empatados(listaaceptados)
                for elemento in listaempatados:
                    print elemento.get_articulo()
                    
        elif opcion=='0':
            print "Usted salio del sistema del CLEI"
            sys.exit()
            
        else:
            print "Usted debe presionar un numero entre 0 y 7"
            continue