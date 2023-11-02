# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 07:37:55 2023

@author: 57321
"""

def convertir_hora(hora):

    if hora >= 12 and hora <24:
        if hora > 12 :
            hora -= 12
        periodo = "PM"
    else:
        if hora == 0 and hora <12:
            hora = 12  
        periodo = "AM"
    
    return hora, periodo


hora = int(input("Ingrese la hora (formato de 24 horas): "))


hora_12, am_pm = convertir_hora(hora)

print(f"La hora en formato de 12 horas es: {hora_12}:{am_pm}")

def convertir(hora, am_pm):
    if am_pm == "AM" and hora == 12:
        hora_24 = 0
    elif am_pm == "AM":
        hora_24 = hora
    elif am_pm == "PM" and hora == 12:
        hora_24 = 12
    else:
        hora_24 = hora + 12
    return hora_24


hora_12 = int(input("Ingrese la hora en formato de 12 horas: "))
periodo = input("Ingrese AM o PM: ")

hora_24 = convertir(hora_12, periodo)

print(f"La hora en formato de 24 horas es: {hora_24}:00")





