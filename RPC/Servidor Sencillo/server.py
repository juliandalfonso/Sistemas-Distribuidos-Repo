
'''
XML-RPC is a Remote Procedure Call method that uses XML passed via HTTP(S) as a transport. With it, a client can call methods with parameters on a remote server (the server is named by a URI) and get back structured data.

The xmlrpc.server module provides a basic server framework for XML-RPC servers written in Python. Servers can either be free standing, using SimpleXMLRPCServer, or embedded in a CGI environment, using CGIXMLRPCRequestHandler.

'''
import xmlrpc.client

from xmlrpc.server import SimpleXMLRPCServer

def	suma_remota(a, b):
	return a+b


#se crea una nueva instancia de servidor 
server = SimpleXMLRPCServer(("localhost", 8001))


'''
SimpleXMLRPCServer.register_function(function=None, name=None)
Register a function that can respond to XML-RPC requests. If name is given, it will be the method name associated with function, otherwise function.__name__ will be used. 
'''
#registra la funcion para que pueda responder solicitudes XML-RPC del cliente  y le asigna el alias "suma" a la funcion
server.register_function(suma_remota, "suma")

#Imprimimos un mensaje en pantalla que indica que el servidor esta corriendo
print ("soy el servidor y estoy corriendo por el puerto 8001")

#iniciamos el servidor
server.serve_forever()


