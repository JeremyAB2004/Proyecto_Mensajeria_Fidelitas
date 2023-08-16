# Módulo de estadísticas

#Variables de estadistica
consultarTelefono = ""
consultarCedula = ""

#Funciones  para la estadistica.
def calcularEnvios(paquetes):
    return len(paquetes)

def listaPaquetes(paquetes):
    return [paquete[0] for paquete in paquetes]  

def calculoTotalRecolectado(paquetes):
    return sum(paquete[1] for paquete in paquetes)  

def paquetesPorTelefono(paquetes, telefono):
    return sum(1 for paquete in paquetes if paquete[2] == telefono)  

def paquetesPorCedula(paquetes, cedula):
    return sum(1 for paquete in paquetes if paquete[3] == cedula)  

#menu

elif menuPrincipal == 6:
        # Módulo de estadísticas

        print("\n--- Módulo de estadísticas ---")
        
        print("1) Cantidad de envíos \n2) Lista de paquetes enviados \n3) Monto de cobro \n4) Cantidad de paquetes por número de teléfono \n5) Cantidad de paquetes por número de cédula \n0) Volver al menú principal")
        
        try:
            estadistica = int(input("Ingresa la opción: "))

            if estadistica  == 1:
                print("Cantidad total de envíos:", calcularEnvios(listaGuias))
            elif estadistica  == 2:
                print("Lista de paquetes enviados:", listaPaquetes(listaGuias))
            elif estadistica  == 3:
                print("Monto total de cobro:", calculoTotalRecolectado(listaGuias))
            elif estadistica  == 4:
                consultarTelefono = input("Ingresa el número de teléfono: ")
                print("Cantidad de paquetes para el número de teléfono", consultarTelefono, ":", paquetesPorTelefono(listaGuias, consultarTelefono))
            elif estadistica  == 5:
                consultarCedula = input("Ingresa el número de cédula: ")
                print("Cantidad de paquetes para el número de cédula", consultarCedula, ":", paquetesPorCedula(listaGuias, consultarCedula))
            elif estadistica  == 0:
                pass
            else:
                print("Opción no válida")
        except ValueError:
            print("Por favor, ingresa un número válido")
