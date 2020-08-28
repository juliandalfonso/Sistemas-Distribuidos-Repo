'''
XML-RPC is a Remote Procedure Call method that uses XML passed via HTTP(S) as a transport. With it, a client can call methods with parameters on a remote server (the server is named by a URI) and get back structured data.

'''
#Importamos la libreria del lado del cliente
import xmlrpc.client


#Solicitamos los datos al usuario
a =eval(input(str('Ingrese el primer numero: ')))
b=eval(input(str('Ingrese el segundo numero: ')))

#A ServerProxy instance is an object that manages communication with a remote XML-RPC server.The required first argument is a URI
proxy = xmlrpc.client.ServerProxy("http://localhost:8001/")

#invocamos la funcion "suma_remota" con el alias de "suma" desde el cliente y le pasamos los parametros a y b para mostrar el resultado en pantalla
print("La suma es: " +str(proxy.suma(a,b)))



