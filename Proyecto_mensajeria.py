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
    
    elif menuPrincipal == 2:
        #Registrar una factura electronica

    elif menuPrincipal == 3:
        #Registro de paquetes
        
    else: 
        print ("Digita una opcion correcta.")
    menuPrincipal = int(input("Menu Principal: \n 1-Ingresar una edad. \n 2-Ver la estadistica. \n 0-Salir.\n"))
