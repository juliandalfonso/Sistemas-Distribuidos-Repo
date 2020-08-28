'''
XML-RPC is a Remote Procedure Call method that uses XML passed via HTTP(S) as a transport. With it, a client can call methods with parameters on a remote server (the server is named by a URI) and get back structured data.

'''
#Importamos la libreria del lado del cliente XML_RPC y la libreria OS para limpiar pantalla
import xmlrpc.client, os  

#A ServerProxy instance is an object that manages communication with a remote XML-RPC server.The required first argument is a URI
#Un proxy es un equipo informático que hace de intermediario entre las conexiones de un cliente y un servidor de destino
s = xmlrpc.client.ServerProxy('http://localhost:8001')

#creamos la funcion del menu
def menu():
    print("**********MENU DE LLAMADAS A RPC*******************")
    print("1. SUMAR")
    print("2. RESTAR")
    print("3. MULTIPLICAR")
    print("4 DIVIDIR")
    print("0 PARA SALIR")

#corremos el menu
menu()    


while True:

    p=eval(input("digite su opcion: "))
    
   
    if p==1:
        x=int(eval(input("ingrese el primer numero: ")))
        y=int(eval(input("ingrese el primer numero: ")))
        # invocamos las funciones de la clase funciones_rpc por medio del proxy creado previamente como "s"
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
     