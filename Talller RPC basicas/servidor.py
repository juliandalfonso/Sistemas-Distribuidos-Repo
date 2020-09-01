
'''
XML-RPC is a Remote Procedure Call method that uses XML passed via HTTP(S) as a transport. With it, a client can call methods with parameters on a remote server (the server is named by a URI) and get back structured data.

The xmlrpc.server module provides a basic server framework for XML-RPC servers written in Python. Servers can either be free standing, using SimpleXMLRPCServer, or embedded in a CGI environment, using CGIXMLRPCRequestHandler.

'''
from xmlrpc.server import SimpleXMLRPCServer

#creamos la clase que contendra las funciones a las cuales puede acceder el cliente
class funciones_rpc:
    def __init__(self,direccion):
        self._datos_usuario = ('falcao','galatasaray2020')
        
    def Invertir_lista(self, p, q):
        return p+q
    def Repetido_lista(self, p, q):
        return p-q


#Creamos el servidor en el puerto 8001
server = SimpleXMLRPCServer(("localhost", 8001))

#registramos la clase funciones_rpc en el servidor para darle acceso al proxy del cliente
server.register_instance(funciones_rpc())

#enviamos un mensaje comprobando que iniciamos el servidor 
print("soy un servidor implementado con clases") 

#iniciamos el servidor
server.serve_forever()

