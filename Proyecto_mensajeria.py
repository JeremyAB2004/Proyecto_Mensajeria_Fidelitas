#creación de guías 
 elif menuPrincipal == 4:
    #Constantes
    
    vocales = "aeiouAEIOU"
    numeros = "0123456789"
    
    #Variables
    
    #creacion del numero
    import random
    unir = f"{vocales}{numeros}"
    longitud = 8
    extension = random.sample (unir, longitud)
    
    creacionDeGuia = "".join(extension)
    
    
    #Mostrar a pantalla
    print (creacionDeGuia)
    #Información del Comercio
    print (nombreComercio)
    print (telefonoComercio)
    #Informacion del destinatario
    print (nombreDestinatario)
    print (nombreDestinatario)
    #Cobro contra entrega
    print (cobroContraEntrega)


