# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 07:08:57 2023

@author: 57321
"""

def area_rec(base,altura):#la funcion area de un rectángulo
    return base * altura#Retorna la multiplicacion 


print (area_rec(3,5))#Imprime la funcion 
print (area_rec(2,7))#Imprime la funcion 

def area_triangulo(base,altura):#la funcion area de un rectángulo
    salida=0
    salida=base*altura/2
    return salida#Retorna la multiplicacion 


print (area_triangulo(3,5))#Imprime la funcion 

def area_circulo(radio):#la funcion area de un rectángulo
    salida=0
    salida=3.14*(radio*radio)
    return salida#Retorna la multiplicacion 


print (area_circulo(10))#Imprime la funcion 

def mayor(edad):
    if edad >= 18:
        return True
    else:
        return False
edad = 17

if mayor(edad) >=18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")
