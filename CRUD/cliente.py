from xmlrpc.client import ServerProxy

s= ServerProxy('http://localhost:20064', allow_none=True)

s.set('lenguaje','Python')
s.set('version', '3.2.3')
print(s.keys())
print (s.get('version'))
