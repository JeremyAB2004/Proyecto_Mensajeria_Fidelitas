'''
-Proyecto de mensajería programación
-Integrantes: 
HERNANDEZ HERNANDEZ KENNETH JESUS
CASTRO ROJAS EDUARDO FRANCISCO
VARELA DIAZ DITTER MAURICIO
ACUÑA BRENES JEREMY JESHUA
'''

from datetime import datetime

#Variables de Registrar cuenta del usuario
correoElectrónico = ''
nombreComercio = ''
telefonoComercio = ''
nombreDueno = ''
apellidoDueno = ''
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

#Menú
print ("***Bienvenido, este es el menú de Inicio***")

while menuPrincipal != 0:

    if menuPrincipal == 1:
        #Registrar cuenta del usuario

        print("\n--- Registro cuenta de usuario ---")

        correoElectrónico = str(input("\nIngrese el correo electrónico: "))
        nombreComercio = str(input("\nIngrese el nombre del comercio: "))
        nombreComercio = nombreComercio.capitalize()
        telefonoComercio = str(input("\nIngrese el teléfono del comercio: "))
        nombreDueno = str(input("\nIngrese el nombre del dueño: "))
        nombreDueno = nombreDueno.capitalize()
        apellidoDueno = str(input("\nIngrese el apellido del dueño: "))
        apellidoDueno = apellidoDueno.capitalize()
        ubicacionLocal = str(input("\nIngrese la ubicación del local: "))
    
    elif menuPrincipal == 2:
        #Registrar una factura electronica

        print ("\n--- Registro de facturas: ---")

        while tipoDeCedula !=0:

            if tipoDeCedula == 1:

                cedulaJuridica = str(input("\nIngrese el número de la cédula Juridica:"))
                break

            elif tipoDeCedula == 2:

                cedulaFisica = str(input("\nIngrese el número de la cédula Física:"))
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

    elif menuPrincipal == 3:
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

        #Agregar a un arreglo multidimensional con los datos del paquete
        listaGuias.append([numeroGuia,nombreComercio,telefonoComercio,nombreDestinatario,telefonoDestinatario,cedulaDestinatario,pesoPaquete,cobroContraEntrega,estadoPaquete])

    elif menuPrincipal == 4:

        print("\n--- Cambio de estado de paquetes: ---")

        while True:
            
            numeroGuiaEstado = input("\nIngrese el número de guía para cambiar el estado: ")

            paquete = 0

            estadoCompleto = 0

            for guia in listaGuias:

                # print("paquete[0]",guia[0], str(numeroGuiaEstado))

                if str(numeroGuiaEstado) == guia[0]:

                    nuevoEstado = input("\nIngrese el nuevo estado del paquete: \n *Creado \n *Recolectado \n *Entrega fallida \n *Entregado \nIngrese el nuevo estado:")
                    listaGuias[paquete][-1] = nuevoEstado
                    print("\nEstado actualizado correctamente. Se actualizó a",nuevoEstado)
                    estadoCompleto = 1
                    break

                paquete += 1

            if estadoCompleto == 1:
                break
            elif estadoCompleto == 0 and numeroGuiaEstado == "SALIR":
                break
            else:
                print("\nEl número de guía que ingresó no existe. Inténtelo denuevo. \nEscriba \"SALIR\" si quiere regresar al menú principal.")

    elif menuPrincipal == 5:

        print("\n--- Rastreo de los paquetes: ---")

        while True:
            
            numeroGuiaRastreo = input("\nIngrese el número de guía para observar el estado: ")

            paquete = 0

            estadoCompleto = 0

            for guia in listaGuias:

                # print("paquete[0]",guia[0], str(numeroGuiaRastreo))

                if str(numeroGuiaRastreo) == guia[0]:

                    print("\nEl estado del paquete de guía número",numeroGuiaRastreo,"es:",listaGuias[paquete][-1])
                    estadoCompleto = 1
                    break
                    
                paquete += 1

            if estadoCompleto == 1:
                break
            elif estadoCompleto == 0 and numeroGuiaRastreo == "SALIR":
                break
            else:
                print("\nEl número de guía que ingresó no existe. Inténtelo denuevo. \nEscriba \"SALIR\" si quiere regresar al menú principal.")


    #Seguir preguntando por las opciones del menú
    try:
        menuPrincipal = int(input("\nMenú Principal: \n1) Registrar cuenta del usuario. \n2) Registrar una factura electrónica. \n3) Registrar el paquete. \n4) Cambio de estado de los paquetes \n5) Rastreo de los paquetes \n0) Salir.\nIngresa la opción: "))
    except:
        menuPrincipal = -1
        print ("\n---¡Digita una opción correcta!---")
