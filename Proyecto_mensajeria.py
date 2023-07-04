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
    menuPrincipal = int(input("Menu Principal: \n 1-Registrar cuenta del usuario. \n 2-Registrar una factura electronica. \n 3-Registrar el paquete. \n 0-Salir.\n"))
except:
    menuPrincipal = -1
    print("Digita una opción correcta.")
while menuPrincipal !=0:
    if menuPrincipal == 1:
        #Registrar cuenta del usuario

        print("Registro de cuenta de usuario \n")
        correo = str(input("Ingrese su correo electronico: "))
        nComercio = str(input("Ingrese el nombre del comercio: "))
        tComercio = int(input("Ingrese el numero telefonico del comercio: "))
        nDueño =  str(input("Ingrese el nombre y apellidos del dueño del comercio: "))
        uComercio = str(input("Ingrese la ubicacion del comercio: "))
    
    elif menuPrincipal == 2:
        #Registrar una factura electronica
        #RegistroDeFacturas
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
        telefono =int(input("\nIngrese el numero de telefono: "))
        correoElectronico =input("\nIngrese el correo electronico: ")
        provincia = input("\nIngrese la Provincia: ")
        canton =input ("\nIngrese el Canton: ")
        Distrito =input("\nIngrese el Distrito: ")

    elif menuPrincipal == 3:
        #Registro de paquetes
        print("Registro de paquetes: \n")

        try:
            cobroContraEntrega = int(input("Realizar cobro contra entrega?. \n1-Si.\n2-No.\n"))
        except:
            cobroContraEntrega = -1
            print("Digita una opción correcta.")
        while cobroContraEntrega !=0:
            if cobroContraEntrega == 1:
                cedulaJuridica = int(input("Ingrese el monto por cobrar en (colones):\n"))
                break
            elif cobroContraEntrega == 2:
                break
            else: 
                print ("Digita una opcion correcta.")
            cobroContraEntrega = input("Realizar cobro contra entrega?. \n1-Si.\n2-No.\n")
        
        nombreDestinatario =input("\nIngrese el Nombre del destinatario: ") 
        telefonoDestinatario =int(input("\nIngrese el número de teléfono del destinatario: "))
        numeroCedula =input("\nIngrese el número de cédula del destinatario: ")
        pesoPaquete = input("\nIngrese el peso del paquete en kg: ")
    
    else: 
        print ("Digita una opcion correcta.")
    menuPrincipal = int(input("Menu Principal: \n 1-Registrar cuenta del usuario. \n 2-Registrar una factura electronica. \n 3-Registrar el paquete. \n 0-Salir.\n"))
