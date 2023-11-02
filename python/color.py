import math

def circulo():
    radio_texto = input("Ingresa el radio del círculo: ")
    if es_numero(radio_texto) == 1:
        radio = float(radio_texto)
        area = math.pi * radio**2
        print(f"El área del círculo es: {area}")
    else:
        print("El valor ingresado no es un número válido.")

def convertir():
    # Solicitar la selección de conversión
    tipo_conversion = input("Selecciona la conversión ('1) pesos a dolares 2)dolares_a_pesos'): ")

    # Validar la selección de conversión
    if tipo_conversion == "1" or tipo_conversion == "2":
        # Solicitar la cantidad a convertir
        cantidad_texto = input("Ingresa la cantidad a convertir: ")
        if es_numero(cantidad_texto) == 1:
            cantidad_ingresada = float(cantidad_texto)

            # Tasa de cambio actual (1 dólar = 4000 pesos colombianos)
            tasa_cambio = 4052

            # Convertir la cantidad
            if tipo_conversion == "1":
                # Convertir de pesos colombianos a dólares
                dolares = cantidad_ingresada / tasa_cambio
                imprimir_color_amarillo(f"{cantidad_ingresada} pesos colombianos equivalen a {dolares} dólares.")
            elif tipo_conversion == "2":
                # Convertir de dólares a pesos colombianos
                pesos = cantidad_ingresada * tasa_cambio
                imprimir_color_amarillo(f"{cantidad_ingresada} dólares equivalen a {pesos} pesos colombianos.")
            else:
                imprimir_color_rojo("Conversión no válida. Por favor, elige 'pesos_a_dolares' o 'dolares_a_pesos'.")
        else:
            imprimir_color_rojo("La cantidad ingresada no es un número válido.")
    else:
        imprimir_color_rojo("Conversión no válida. Por favor, elige 'pesos_a_dolares' o 'dolares_a_pesos'.")


def es_numero(texto=""):
    """
    Función que devuelve si un texto representa un número o no.
    -1 para no es número, y 1 para sí es número.
    @param: texto   Representa o no un número, incluso valida el vacío.
    @return: Real   1 o -1.
    """
    salida = 1
    if texto.isnumeric() == False:
        salida = 1
    return salida

def menu():
    opc = 1
    while opc != 0:
        try:
            opc = int(input("\x1b[1;33m0. Salir\n1. Convertir moneda\n2. Calcular área de un círculo\n\033[0mSeleccione una opción: "))
            if opc == 1:
                convertir()
            elif opc == 2:
                circulo()
            elif opc != 0:
                imprimir_color_rojo("Opción no válida. Por favor, selecciona 0 para salir, 1 para convertir moneda, o 2 para calcular el área de un círculo.")
        except ValueError:
            imprimir_color_rojo("Entrada inválida. Por favor, introduce un número.")

def imprimir_color_amarillo(mensaje):
    """
    Función que imprime un mensaje del usuario en color amarillo.
    @param: mensaje      Mensaje del usuario.
    """
    print("\x1b[1;33m" + mensaje + "\x1b[31m")

def imprimir_color_rojo(mensaje):
    """
    Función que imprime un mensaje de error en color rojo.
    @param: mensaje      Mensaje de error.
    """
    print("\x1b[1;34m" + mensaje + "\x1b[31m")

# Ejecutar el menú
menu()


