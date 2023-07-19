#Creacion de numero guia 
#día
from datetime import datetime
fechaActual = datetime.now()
codigoFecha = datetime.strftime(fechaActual,'%d%m%y')

codigoNumero = 0 
codigoNumero += 1
codigoNumero = str(codigoNumero).zfill(4)
numeroGuia = (codigoFecha + str (codigoNumero))

#Mostrar a pantalla
print (numeroGuia)

#Información del Comercio
print (nombreComercio)
print (telefonoComercio)

#Informacion del destinatario
print (nombreDestinatario)
print (nombreDestinatario)

#Cobro contra entrega
print (cobroContraEntrega)
