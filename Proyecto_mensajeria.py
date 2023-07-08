'''
-Proyecto de mensajería programación
-Integrantes: 
HERNANDEZ HERNANDEZ KENNETH JESUS
CASTRO ROJAS EDUARDO FRANCISCO
VARELA DIAZ DITTER MAURICIO
ACUÑA BRENES JEREMY JESHUA
'''

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
numeroCedula = ''
pesoPaquete = 0
cobroContraEntrega = 0

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
        numeroCedula = str(input("\nIngrese el número de cédula del destinatario: "))
        pesoPaquete = float(input("\nIngrese el peso del paquete en kg: "))
        cobroContraEntrega = float(input("\nIngrese el monto en colones del costo de la entrega: "))  

    #Seguir preguntando por las opciones del menú
    try:
        menuPrincipal = int(input("\nMenú Principal: \n1) Registrar cuenta del usuario. \n2) Registrar una factura electrónica. \n3) Registrar el paquete. \n0-Salir.\nIngresa la opción: "))
    except:
        menuPrincipal = -1
        print ("\n---¡Digita una opción correcta!---")
