'''
-Proyecto de mensajería programación
-Integrantes: 
HERNANDEZ HERNANDEZ KENNETH JESUS
CASTRO ROJAS EDUARDO FRANCISCO
VARELA DIAZ DITTER MAURICIO
ACUÑA BRENES JEREMY JESHUA
'''

#Menú
print ("***Este es el menu de Inicio***")
#Menu Principal
try:
    menuPrincipal = int(input("Menu Principal: \n 1-Registrar cuenta del usuario. \n 2-Registrar una factura electronica. \n 3-Registrar el paquete. \n 4-Creación de guías  \n 0-Salir.\n"))
except:
    menuPrincipal = -1
    print("Digita una opción correcta.")
while menuPrincipal !=0:
    if menuPrincipal == 1:
        #Registrar cuenta del usuario
        print("\n--- Registro cuenta de usuario ---\n")
        correoElectrónico = str(input("Ingresa el correo electrónico: "))
        nombreComercio = str(input("Ingresa el nombre del comercio: "))
        nombreComercio = nombreComercio.capitalize()
        telefonoComercio = str(input("Ingresa el teléfono del comercio: "))
        nombreDueno = str(input("Ingresa el nombre del dueño: "))
        nombreDueno = nombreDueno.capitalize()
        apellidoDueno = str(input("Ingresa el apellido del dueño: "))
        apellidoDueno = apellidoDueno.capitalize()
        ubicacionLocal = str(input("Ingresa la ubicación del local: "))
        menuPrincipal = int(input("Menu Principal: \n 1-Registrar cuenta del usuario. \n 2-Registrar una factura electronica. \n 3-Registrar el paquete. \n 4-Creación de guías  \n 0-Salir.\n"))
    
    elif menuPrincipal == 2:
        #Registrar una factura electronica
        print ("Registro de facturas:\n")
        
        try:
            tipoDeCedula = int(input("Ingrese el tipo de Cedula. \n1-Juridica.\n2-Fisica.\n"))
        except:
            tipoDeCedula = -1
            print("Digita una opción correcta.")
        while tipoDeCedula !=0:
            if tipoDeCedula == 1:
                cedulaJuridica = int(input("Ingrese el numero de la cedula Juridica:\n"))
                break
            elif tipoDeCedula == 2:
                cedulaFisica = int(input("Ingrese el numero de la cedula Fisica:\n"))
                break
            else: 
                print ("Digita una opcion correcta.")
            tipoDeCedula = input("Ingrese el tipo de Cedula. \n1-Juridica.\n2-Fisica.\n")
        
        nombreRegistrado =input("\nIngrese el Nombre registrado: ") 
        nombreRegistrado = nombreRegistrado.capitalize()
        telefono =int(input("\nIngrese el numero de telefono: "))
        correoElectronico =input("\nIngrese el correo electronico: ")
        provincia = input("\nIngrese la Provincia: ")
        provincia = provincia.capitalize()
        canton =input ("\nIngrese el Canton: ")
        canton = canton.capitalize()
        distrito =input("\nIngrese el Distrito: ")
        distrito = distrito.capitalize()
        menuPrincipal = int(input("Menu Principal: \n 1-Registrar cuenta del usuario. \n 2-Registrar una factura electronica. \n 3-Registrar el paquete. \n 4-Creación de guías  \n 0-Salir.\n"))
    elif menuPrincipal == 3:
        #Registro de paquetes
        print("Registro de paquetes: \n")
        nombreDestinatario =input("\nIngrese el Nombre del destinatario: ") 
        nombreDestinatario = nombreDestinatario.capitalize()
        telefonoDestinatario =int(input("\nIngrese el número de teléfono del destinatario: "))
        numeroCedula =int(input("\nIngrese el número de cédula del destinatario: "))
        pesoPaquete = float(input("\nIngrese el peso del paquete en kg: "))
        cobroContraEntrega = float(input("\nIngrese el el monto en colones del costo de la entrega: "))
        menuPrincipal = int(input("Menu Principal: \n 1-Registrar cuenta del usuario. \n 2-Registrar una factura electronica. \n 3-Registrar el paquete. \n 4-Creación de guías  \n 0-Salir.\n"))
    elif menuPrincipal == 4:
        #Creación de guías
        #día
        from datetime import datetime
        fechaActual = datetime.now()
        codigoFecha = datetime.strftime(fechaActual,'%d%m%y')

        codigoNumero = 0 
        codigoNumero += 1
        codigoNumero = str(codigoNumero).zfill(4)

        numeroGuia = (codigoFecha + str (codigoNumero))

        #Mostrar a pantalla
        print (numeroGuia, end="\n")

        #Información del Comercio
        print (nombreComercio, end="\n")
        print (telefonoComercio, end="\n")

        #Informacion del destinatario
        print (nombreDestinatario, end="\n")
        print (nombreDestinatario, end="\n")

        #Cobro contra entrega
        print (cobroContraEntrega, end="\n")
        menuPrincipal = int(input("Menu Principal: \n 1-Registrar cuenta del usuario. \n 2-Registrar una factura electronica. \n 3-Registrar el paquete. \n 4-Creación de guías  \n 0-Salir.\n"))

    else: 
        print ("Digita una opcion correcta.")
        menuPrincipal = int(input("Menu Principal: \n 1-Registrar cuenta del usuario. \n 2-Registrar una factura electronica. \n 3-Registrar el paquete. \n 0-Salir.\n"))
