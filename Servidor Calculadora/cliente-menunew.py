# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 20:02:37 2018

@author: Cesar jaramillo

"""
import xmlrpc.client, os  
#import xmlrpc.client, os

s = xmlrpc.client.ServerProxy('http://localhost:8001')
def menu():
    print("**********MENU DE LLAMADAS A RPC*******************")
    print("1. SUMAR")
    print("2. RESTAR")
    print("3. MULTIPLICAR")
    print("4 DIVIDIR")
    print("0 PARA SALIR")

menu()    
while True:
    p=eval(input("digite su opcion: "))
    
   
    if p==1:
        x=int(eval(input("ingrese el primer numero: ")))
        y=int(eval(input("ingrese el primer numero: ")))
        print(("el resultado de la suma es: "+str(s.suma(x,y))))
        a=eval(input())
    elif p==2:
        x=int(eval(input("ingrese el primer numero: ")))
        y=int(eval(input("ingrese el primer numero: ")))
        print(("el resultado de la resta es: "+str(s.resta(x,y))))
    elif p==3:
        x=int(eval(input("ingrese el primer numero: ")))
        y=int(eval(input("ingrese el primer numero: ")))
        print(("el resultado de la multiplicacion es: "+str(s.multi(x,y))))
    elif p==4:
        x=int(eval(input("ingrese el primer numero: ")))
        y=int(eval(input("ingrese el primer numero: ")))
        print(("el resultado de la division es: "+str(s.divi(x,y))))
    elif p==0:
        print("que tengas un buen dia, hasta pronto")
        break
    else:
        os.system('cls')
     