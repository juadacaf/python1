# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 06:48:17 2023

@author: 57321
"""
print ("Hola")



def area_rec(base,altura):#la funcion area de un rectángulo
    return base * altura#Retorna la multiplicacion 

a = int(input("Ingrese la altura: "))#Para ingresar por teclado la altura del obgeto
b = int(input("Ingrese la base: "))#Para ingresar por teclado la base del obgeto

c=area_rec(a,b)#Para la impresion 
print (c)#Imprime la funcion 