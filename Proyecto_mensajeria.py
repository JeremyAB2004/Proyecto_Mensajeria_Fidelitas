from datetime import datetime
import json

#El programa crea los archivos, si es que no existen
try:
    textFile = open('usuarios.txt', 'r')
    textFile.close()
except:
    textFile = open('usuarios.txt', 'w')
    textFile.close()

try:
    textFile = open('facturas.txt', 'r')
    textFile.close()
except:
    textFile = open('facturas.txt', 'w')
    textFile.close()

try:
    textFile = open('guias.txt', 'r')
    textFile.close()
except:
    textFile = open('guias.txt', 'w')
    textFile.close()

#Variables de Registrar cuenta del usuario
correoElectrónico = ''
nombreComercio = ''
telefonoComercio = ''
nombreDueno = ''
ubicacionLocal = ''

#Variables de Registrar una factura electronica
tipoDeCedula = -1
cedulaJuridica = ''
cedulaFisica = '' 
nombreRegistrado = ''
telefono = ''
correoElectronico = ''
provincia = ''
canton = ''
distrito = ''

#Variables de Registro de paquetes
nombreDestinatario = ''
telefonoDestinatario = ''
cedulaDestinatario = ''
pesoPaquete = 0
cobroContraEntrega = 0
listaGuias = []

#Variables de Cambio de estado de paquetes y Rastreo de paquetes

numeroGuiaEstado = ""
numeroGuiaRastreo = ""
estadoCompleto = ""
paquete = ""

#Variables de Menu Principal
menuPrincipal = -1

#Variables de estadistica
consultarTelefono = ""
consultarCedula = ""

#Función para registro de listas en TXT
def registroTXT(texto, file, message):

    textFile = open(file, 'r')
    contentFile = textFile.read()
    textFile.close()

    if contentFile == '':
        contentFile = '[]'

    lista = json.loads(contentFile.replace("'", "\""))
    lista.append(texto)

    textFile = open(file, 'w')
    textFile.write(str(lista))
    textFile.close()

    print(message)

#Función para obtener listas en TXT
def obtenerTXT(file):

    textFile = open(file, 'r')
    contentFile = textFile.read()
    textFile.close()

    if contentFile == '':
        contentFile = '[]'

    lista = json.loads(contentFile.replace("'", "\""))

    return lista

#Función para actualizar listas en TXT
def actualizarTXT(texto, file, message):

    textFile = open(file, 'w')
    textFile.write(str(texto))
    textFile.close()

    print(message)


#Funciones  para la estadistica.
def calcularEnvios():

    #Traemos los datos del txt de guias
    listaGuias = obtenerTXT('guias.txt')

    return len(listaGuias)

def listaPaquetes():

    #Traemos los datos del txt de guias
    listaGuias = obtenerTXT('guias.txt')

    paquetesEntregados = ''

    for guia in listaGuias:
        if guia[-2] == 'Entregado':
            paquetesEntregados += f'\nPaquete: {guia[0]}\n'


    return paquetesEntregados 

def calculoTotalRecolectado():

    #Traemos los datos del txt de guias
    listaGuias = obtenerTXT('guias.txt')

    montoTotal = .0

    for guia in listaGuias:
        try:
            montoTotal += float(guia[-3])
        except:
            continue

    return montoTotal

def paquetesPorTelefono(telefono):
    
    #Traemos los datos del txt de guias
    listaGuias = obtenerTXT('guias.txt')

    paquetesPorTel = 0

    for guia in listaGuias:
        try:
            if guia[4] == telefono:
                paquetesPorTel += 1
        except:
            continue

    return paquetesPorTel

def paquetesPorCedula(cedula):
    
    #Traemos los datos del txt de guias
    listaGuias = obtenerTXT('guias.txt')

    paquetesPorCed = 0

    for guia in listaGuias:
        try:
            if guia[5] == cedula:
                paquetesPorCed += 1
        except:
            continue

    return paquetesPorCed

validacionInicioSesion = 0

print ("***Bienvenido, primero debe iniciar sesión***")



menuPrincipalIngreso = -1

while validacionInicioSesion == 0:

    if menuPrincipalIngreso == 1:
        correoIncioSesion = str(input('Ingrese su correo de usuario: '))

        #Traemos los datos del txt de usuarios
        listaUsuarios = obtenerTXT('usuarios.txt')

        for usuario in listaUsuarios:

            if usuario[1] == correoIncioSesion:

                validacionInicioSesion = 1
                idUsuario = usuario[0]
                break

            else:

                validacionInicioSesion = 0

        if validacionInicioSesion == 0:
            
            print('\n ---Correo de usuario no existe---')
    
    elif menuPrincipalIngreso == 2:
        
        #Registrar cuenta del usuario

        print("\n--- Registro cuenta de usuario ---")

        correoElectrónico = str(input("\nIngrese el correo electrónico: "))
        nombreComercio = str(input("\nIngrese el nombre del comercio: "))
        nombreComercio = nombreComercio.capitalize()
        telefonoComercio = str(input("\nIngrese el teléfono del comercio: "))
        nombreDueno = str(input("\nIngrese el nombre del dueño: "))
        nombreDueno = nombreDueno.capitalize()
        ubicacionLocal = str(input("\nIngrese la ubicación del local: "))

        #Traemos los datos del txt de usuarios
        listaUsuarios = obtenerTXT('usuarios.txt')

        registroUsuarioVariable = [len(listaUsuarios),correoElectrónico,nombreComercio,telefonoComercio,nombreDueno,ubicacionLocal]

        registroTXT(registroUsuarioVariable, 'usuarios.txt', 'Su registro ha sido exitoso')
    
    #Seguir preguntando por las opciones del menú
    if validacionInicioSesion == 0:
        try:
            menuPrincipalIngreso = int(input("\n¿Cómo desea ingresar?: \n1) Ingresar con cuenta de usuario. \n2) Registrar cuenta del usuario. \nIngresa la opción: "))
        except:
            menuPrincipalIngreso = -1
            print ("\n---¡Digita una opción correcta!---")


#Menú
print ("***Bienvenido, este es el menú de Inicio***")

while menuPrincipal != 0:

    if menuPrincipal == 1:
        #Registrar una factura electronica

        print ("\n--- Registro de facturas: ---")

        tipoDeCedula = -1

        while tipoDeCedula !=0:

            if tipoDeCedula == 1:

                cedulaJuridica = str(input("\nIngrese el número de la cédula Jurídica:"))
                cedulaInsert = cedulaJuridica
                tipoCedulaInsert = 'Jurídica'
                break

            elif tipoDeCedula == 2:

                cedulaFisica = str(input("\nIngrese el número de la cédula Física:"))
                cedulaInsert = cedulaFisica
                tipoCedulaInsert = 'Física'
                break

            try:
                tipoDeCedula = int(input("Tipos de cédula:\n1) Jurídica.\n2) Física.\nIngrese el tipo de Cédula: "))
            except:
                tipoDeCedula = -1
                print ("\n---¡Digita una opción correcta!---")
        
        nombreRegistrado = str(input("\nIngrese el Nombre registrado: "))
        nombreRegistrado = nombreRegistrado.capitalize()

        telefono = str(input("\nIngrese el número de telefono: "))
        correoElectronico = str(input("\nIngrese el correo electronico: "))

        provincia = input("\nIngrese la Provincia: ")
        provincia = provincia.capitalize()

        canton = str(input("\nIngrese el Cantón: "))
        canton = canton.capitalize()

        distrito = str(input("\nIngrese el Distrito: "))
        distrito = distrito.capitalize()

        registroFacturasVariable = [cedulaInsert,tipoCedulaInsert,nombreRegistrado,telefono,correoElectronico,provincia,canton,distrito,idUsuario]

        registroTXT(registroFacturasVariable, 'facturas.txt', 'Factura guardada con éxito')

    elif menuPrincipal == 2:
        #Registro de paquetes

        print("\n--- Registro de paquetes: ---")

        nombreDestinatario = str(input("\nIngrese el Nombre del destinatario: "))
        nombreDestinatario = nombreDestinatario.capitalize()
        telefonoDestinatario = str(input("\nIngrese el número de teléfono del destinatario: "))
        cedulaDestinatario = str(input("\nIngrese el número de cédula del destinatario: "))
        pesoPaquete = float(input("\nIngrese el peso del paquete en kg: "))
        cobroContraEntrega = float(input("\nIngrese el monto en colones del costo de la entrega: ₡ "))
        estadoPaquete = "Creado"  

        #Creación de guías

        print("\n--- Creación de guías: ---")

        #Traer el total de guias en el txt
        listaGuias = obtenerTXT('guias.txt')
        
        fechaActual = datetime.now()
        codigoFecha = datetime.strftime(fechaActual,'%d%m%y')

        codigoNumero = len(listaGuias)
        codigoNumero = str(codigoNumero).zfill(4)

        numeroGuia = (codigoFecha + str (codigoNumero))
 
        #Mostrar a pantalla
        print ("\nEl número de guía para el paquete es: ",numeroGuia)

        #Información del Comercio
        print ("El nombre del comercio es: ",nombreComercio)
        print ("El teléfono del comercio es: ",telefonoComercio)

        #Informacion del destinatario
        print ("El nombre del destinatario es: ",nombreDestinatario)
        print ("El teléfono del destinatario es: ",telefonoDestinatario)

        #Cobro contra entrega
        print ("El cobro contra entrega es: ₡ ",cobroContraEntrega)

        listaUsuarios = obtenerTXT('usuarios.txt')
        nombreComercio = listaUsuarios[idUsuario][2]
        telefonoComercio = listaUsuarios[idUsuario][3]
        listaUsuarios = []

        #Agregar a un arreglo multidimensional con los datos del paquete
        listaGuias.append([numeroGuia,nombreComercio,telefonoComercio,nombreDestinatario,telefonoDestinatario,cedulaDestinatario,pesoPaquete,cobroContraEntrega,estadoPaquete])

        registroGuiasVariable = [numeroGuia,nombreComercio,telefonoComercio,nombreDestinatario,telefonoDestinatario,cedulaDestinatario,pesoPaquete,cobroContraEntrega,estadoPaquete,idUsuario]

        registroTXT(registroGuiasVariable, 'guias.txt', 'Paquete guardado con éxito')

    elif menuPrincipal == 3:

        print("\n--- Cambio de estado de paquetes: ---")

        while True:
            
            numeroGuiaEstado = input("\nIngrese el número de guía para cambiar el estado: ")

            paquete = 0

            estadoCompleto = 0

            #Traemos los datos del txt de guias
            listaGuias = obtenerTXT('guias.txt')

            for guia in listaGuias:

                # print("paquete[0]",guia[0], str(numeroGuiaEstado))

                if str(numeroGuiaEstado) == guia[0]:

                    nuevoEstado = input("\nIngrese el nuevo estado del paquete: \n *Creado \n *Recolectado \n *Entrega fallida \n *Entregado \nIngrese el nuevo estado:")
                    listaGuias[paquete][-2] = nuevoEstado

                    actualizarEstadoVariable = listaGuias
                    actualizarTXT(actualizarEstadoVariable, 'guias.txt', f'Estado actualizado correctamente. Se actualizó a {nuevoEstado}')

                    estadoCompleto = 1
                    break

                paquete += 1

            if estadoCompleto == 1:
                break
            elif estadoCompleto == 0 and numeroGuiaEstado == "SALIR":
                break
            else:
                print("\nEl número de guía que ingresó no existe. Inténtelo denuevo. \nEscriba \"SALIR\" si quiere regresar al menú principal.")

    elif menuPrincipal == 4:

        print("\n--- Rastreo de los paquetes: ---")

        while True:
            
            numeroGuiaRastreo = input("\nIngrese el número de guía para observar el estado: ")

            paquete = 0

            estadoCompleto = 0

            #Traemos los datos del txt de guias
            listaGuias = obtenerTXT('guias.txt')

            for guia in listaGuias:

                # print("paquete[0]",guia[0], str(numeroGuiaRastreo))

                if str(numeroGuiaRastreo) == guia[0]:

                    print("\nEl estado del paquete de guía número",numeroGuiaRastreo,"es:",listaGuias[paquete][-2])
                    estadoCompleto = 1
                    break
                    
                paquete += 1

            if estadoCompleto == 1:
                break
            elif estadoCompleto == 0 and numeroGuiaRastreo == "SALIR":
                break
            else:
                print("\nEl número de guía que ingresó no existe. Inténtelo denuevo. \nEscriba \"SALIR\" si quiere regresar al menú principal.")
    
    elif menuPrincipal == 5:
        # Módulo de estadísticas

        print("\n--- Módulo de estadísticas ---")
        
        print("1) Cantidad de envíos \n2) Lista de paquetes enviados \n3) Monto de cobro \n4) Cantidad de paquetes por número de teléfono \n5) Cantidad de paquetes por número de cédula \n0) Volver al menú principal")
        
        try:
            estadistica = int(input("Ingresa la opción: "))

            if estadistica  == 1:
                print("\nCantidad total de envíos:", calcularEnvios())
            elif estadistica  == 2:
                print("\nLista de paquetes enviados:\n", listaPaquetes())
            elif estadistica  == 3:
                print("\nMonto total de cobro:", calculoTotalRecolectado())
            elif estadistica  == 4:
                consultarTelefono = input("Ingresa el número de teléfono: ")
                print("\nCantidad de paquetes para el número de teléfono", consultarTelefono, ":", paquetesPorTelefono(consultarTelefono))
            elif estadistica  == 5:
                consultarCedula = input("Ingresa el número de cédula: ")
                print("\nCantidad de paquetes para el número de cédula", consultarCedula, ":", paquetesPorCedula(consultarCedula))
            elif estadistica  == 0:
                pass
            else:
                print("Opción no válida")
        except ValueError:
            print("Por favor, ingresa un número válido")

    #Seguir preguntando por las opciones del menú
    try:
        menuPrincipal = int(input("\nMenú Principal: \n1) Registrar una factura electrónica. \n2) Registrar el paquete. \n3) Cambio de estado de los paquetes \n4) Rastreo de los paquetes \n5) Módulo de estadística \n0) Salir.\nIngresa la opción: "))
    except:
        menuPrincipal = -1
        print ("\n---¡Digita una opción correcta!---")
