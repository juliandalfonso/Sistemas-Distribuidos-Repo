'''
XML-RPC is a Remote Procedure Call method that uses XML passed via HTTP(S) as a transport. With it, a client can call methods with parameters on a remote server (the server is named by a URI) and get back structured data.

PRESENTADO POR: JUAN PABLO PEREZ SANTOS - JULIAN DAVID ALFONSO 2020

PYTHON 3

'''
# Importamos la libreria del lado del cliente XML_RPC y la libreria OS para limpiar pantalla
import xmlrpc.client
import os

# A ServerProxy instance is an object that manages communication with a remote XML-RPC server.The required first argument is a URI
# Un proxy es un equipo informático que hace de intermediario entre las conexiones de un cliente y un servidor de destino
s = xmlrpc.client.ServerProxy('http://localhost:8001')

# creamos la funcion del menu


def menu():
    print("**********MENU DE LLAMADAS A RPC*******************")
    print("1. Invertir lista")
    print("2. Repetir lista")
    print("0. Salir")


def pedir_datos():
    usuario = input("Ingrese usuario: ")
    clave = input("Ingrese clave: ")
    return usuario, clave


def llenar_lista():
    print("** Llenar listas **")
    lista = []
    for i in range(6):
        num = int(input("Ingrese datos: "))
        lista.append(num)
    return lista


def guardar_archivo(lista):
    f = open('lista.txt', 'w')
    for i in lista:
        f.write(str(i))
    f.close()

# corremos el menu


lista = llenar_lista()
guardar_archivo(lista)
autenticado = False


while True:

    os.system('cls')
    if(not autenticado): usuario, clave = pedir_datos()
    
    if(s.validar_datos(usuario, clave)):
        menu()
        autenticado = True

        p = eval(input("digite su opcion: "))

        if p == 1:
            archivo = s.Invertir_lista('lista.txt')
            f = open(archivo, 'r')
            lista = []
            nums = f.readline()
            for i in nums:
                lista.append(i)
            f.close()
            print("Lista invertida: ", lista)
            x = input()
        elif p == 2:
            maximo, cont_max = s.Repetido_lista('lista.txt')
            print("El numero que mas se repite es: {} una cantidad {} de veces ".format(
                maximo, cont_max))
            x = input()
        elif p == 0:
            print("que tengas un buen dia, hasta pronto")
            break
        else:
            os.system('cls')
    else: 
        print("Datos incorrestos Intentar de nuevo")
        op = int(input("Volver a intentar \n1)SI\n2)NO"))
        if (op == 2): break