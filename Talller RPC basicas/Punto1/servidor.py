
'''
XML-RPC is a Remote Procedure Call method that uses XML passed via HTTP(S) as a transport. With it, a client can call methods with parameters on a remote server (the server is named by a URI) and get back structured data.

The xmlrpc.server module provides a basic server framework for XML-RPC servers written in Python. Servers can either be free standing, using SimpleXMLRPCServer, or embedded in a CGI environment, using CGIXMLRPCRequestHandler.

PRESENTADO POR: JUAN PABLO PEREZ SANTOS - JULIAN DAVID ALFONSO 2020

PYTHON 3

'''
from xmlrpc.server import SimpleXMLRPCServer

# creamos la clase que contendra las funciones a las cuales puede acceder el cliente


class funciones_rpc:
    """ def __init__(self):
        self._datos_usuario = ('falcao','galatasaray2020') """

    def Crear_lista(self,nombre):
        f = open(nombre, 'r')
        lista = []
        nums = f.readline()
        for i in nums:
            lista.append(i)
        f.close()
        return lista

    def guardar_datos(self,lista):
        f = open('lista.txt', 'w')
        for i in lista:
            f.write(str(i))
        f.close()

    def Invertir_lista(self, nombre):
        lista = self.Crear_lista(nombre)
        lista.reverse()
        self.guardar_datos(lista)
        return "lista.txt"

    def Repetido_lista(self, nombre):
        lista = self.Crear_lista(nombre)
        maximo = 0
        cont_max = 0
        for i in lista:
            cont = 0
            for j in lista:
                if (i == j):
                    cont += 1
            if(cont_max < cont): 
                cont_max = cont
                maximo = i
        return maximo,cont_max





# Creamos el servidor en el puerto 8001
server = SimpleXMLRPCServer(("localhost", 8001))

# registramos la clase funciones_rpc en el servidor para darle acceso al proxy del cliente
server.register_instance(funciones_rpc())

# enviamos un mensaje comprobando que iniciamos el servidor
print("soy un servidor implementado con clases")

# iniciamos el servidor
server.serve_forever()
