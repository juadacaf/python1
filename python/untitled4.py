# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 08:08:52 2023

@author: 57321
"""

def convertir(valor, moneda):
    if moneda == 1:
        dolares = valor / 4068.83
        return dolares
    elif moneda == 2:
        pesos = valor * 4068.83
        return pesos
    else:
        return "Opción no válida"

parametro = int(input("¿Deseas convertir de pesos a dólares (1) o de dólares a pesos (2)? "))
cantidad = float(input("Ingresar la cantidad de doliente: "))

resultado = convertir(cantidad, parametro)

if resultado == "Opción no válida":
    print(resultado)
else:
    print(f"Esta es tu cantidad doliente: {resultado}")

        


